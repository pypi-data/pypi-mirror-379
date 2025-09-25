import os
import sys
import logging
from datetime import datetime
import json
import socket
import threading
import queue
import time
from logging.handlers import TimedRotatingFileHandler

from dotenv import load_dotenv


load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))


LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = os.getenv('LOG_FORMAT', '%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s')
LOG_DATE_FORMAT = os.getenv('LOG_DATE_FORMAT', '%Y-%m-%d %H:%M:%S')
LOG_FILE_MAX_BYTES = int(os.getenv('LOG_FILE_MAX_BYTES', '10485760'))  # 10MB
LOG_FILE_BACKUP_COUNT = int(os.getenv('LOG_FILE_BACKUP_COUNT', '7'))
LOG_FILENAME = os.getenv('LOG_FILENAME', './logs/app.log')

LOGSTASH_HOST = os.getenv('LOGSTASH_HOST', '127.0.0.1')
LOGSTASH_PORT = int(os.getenv('LOGSTASH_PORT', '5045'))
LOGSTASH_MAX_QUEUE_SIZE = int(os.getenv('LOGSTASH_MAX_QUEUE_SIZE', '10000'))
LOGSTASH_BATCH_SIZE = int(os.getenv('LOGSTASH_BATCH_SIZE', '50'))
LOGSTASH_FLUSH_INTERVAL = float(os.getenv('LOGSTASH_FLUSH_INTERVAL', '1.0'))

APP_NAME = os.getenv('APP_NAME', 'app')
ENCODING = os.getenv('ENCODING', 'utf-8')


logFormatter = logging.Formatter(LOG_FORMAT)
rootLogger = logging.getLogger()
rootLogger.setLevel(getattr(logging, LOG_LEVEL.upper()))

if os.getenv('ENABLE_FILE_LOG', '0') == '1':
    log_filename = LOG_FILENAME
    log_dir = os.path.dirname(log_filename)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    fileHandler = TimedRotatingFileHandler(log_filename, when="d", interval=1, backupCount=LOG_FILE_BACKUP_COUNT)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

if os.getenv('ENABLE_CONSOLE_LOG', '0') == '1':
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)


class AsyncLogstashHandler(logging.Handler):

    def __init__(self, host=None, port=None, max_queue_size=None, batch_size=None, flush_interval=None):
        super().__init__()
        self.host = host or LOGSTASH_HOST
        self.port = port or LOGSTASH_PORT
        self.max_queue_size = max_queue_size or LOGSTASH_MAX_QUEUE_SIZE
        self.batch_size = batch_size or LOGSTASH_BATCH_SIZE
        self.flush_interval = flush_interval or LOGSTASH_FLUSH_INTERVAL

        self.log_queue = queue.Queue(maxsize=self.max_queue_size)
        self.worker_thread = None
        self.stop_event = threading.Event()
        self.sock = None
        self.lock = threading.Lock()

        self.start_worker()
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __del__(self):
        self.close()

    def start_worker(self):
        if self.worker_thread is None or not self.worker_thread.is_alive():
            self.worker_thread = threading.Thread(target=self._worker, daemon=True)
            self.worker_thread.start()

    def _connect(self):
        try:
            if self.sock:
                self.sock.close()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((self.host, self.port))
            self.sock = sock
        except Exception as e:
            self.sock = None
            sys.stderr.write(f"Logstash connection failed: {e}\n")

    def _send_batch(self, batch):
        if not batch:
            return True
        try:
            if not self.sock:
                self._connect()
            if self.sock:
                data = "".join(batch).encode(ENCODING)
                self.sock.sendall(data)
                return True
            return False
        except Exception as e:
            sys.stderr.write(f"Send logs to Logstash failed: {e}\n")
            self._connect()  # re-connect
            return False

    def _worker(self):
        buffer = []
        last_flush = time.time()

        # drain remaining items before exit
        while not self.stop_event.is_set() or not self.log_queue.empty():
            try:
                record = self.log_queue.get(timeout=0.5)
                log_entry = self._format_record(record)
                buffer.append(log_entry)
                # mark item handled from the queue perspective
                self.log_queue.task_done()

                # flush conditions
                if len(buffer) >= self.batch_size or (time.time() - last_flush) >= self.flush_interval:
                    if self._send_batch(buffer):
                        buffer.clear()
                        last_flush = time.time()

            except queue.Empty:
                # flush if timeout
                if buffer and (time.time() - last_flush) >= self.flush_interval:
                    if self._send_batch(buffer):
                        buffer.clear()
                        last_flush = time.time()
                continue
            except Exception as e:
                sys.stderr.write(f"Logstash thread error: {e}\n")

        # empty the queue
        if buffer:
            self._send_batch(buffer)

    def _format_record(self, record):
        log_entry = {
            '@timestamp': datetime.fromtimestamp(record.created).isoformat() + "Z",
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'thread': record.threadName,
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
            'host': socket.gethostname(),
            'app': APP_NAME,
        }
        # include exception stack if present
        if record.exc_info:
            import traceback
            log_entry['exception'] = ''.join(traceback.format_exception(*record.exc_info))
        if hasattr(record, 'custom_fields'):
            log_entry.update(record.custom_fields)
        return json.dumps(log_entry, ensure_ascii=False) + "\n"

    def emit(self, record):
        try:
            if not self.log_queue.full():
                self.log_queue.put_nowait(record)
            else:
                # queue is full, discard the oldest log
                try:
                    _ = self.log_queue.get_nowait()
                    self.log_queue.task_done()  # balance unfinished task count
                    self.log_queue.put_nowait(record)
                    sys.stderr.write("The log queue is full, discarded the oldest log.\n")
                except queue.Empty:
                    pass
        except Exception as e:
            sys.stderr.write(f"Add logs to queue failed: {e}\n")

    def close(self):
        self.stop_event.set()
        if self.worker_thread and self.worker_thread.is_alive():
            self.worker_thread.join(timeout=5)
        if self.sock:
            self.sock.close()
        super().close()


def setup_logstash_logger(logger_name=None, logstash_host=None, logstash_port=None):
    if logger_name:
        logger = logging.getLogger(logger_name)
    else:
        logger = rootLogger

    # avoid duplicate AsyncLogstashHandler
    if any(isinstance(h, AsyncLogstashHandler) for h in logger.handlers):
        return logger

    logstash_handler = AsyncLogstashHandler(
        host=logstash_host or LOGSTASH_HOST,
        port=logstash_port or LOGSTASH_PORT
    )
    logstash_handler.setLevel(getattr(logging, LOG_LEVEL.upper()))

    logger.addHandler(logstash_handler)
    return logger
