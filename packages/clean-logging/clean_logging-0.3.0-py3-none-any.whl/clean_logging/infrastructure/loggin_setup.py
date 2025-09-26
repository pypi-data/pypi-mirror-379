import logging

import coloredlogs
import queue
import threading
from clean_logging.core.interfaces.log_repository_interface import ILogRepository


# ایجاد یک کیو برای ذخیره موقت لاگ‌ها
log_queue = queue.Queue()


def setup_logging(log_repository: ILogRepository):
    """تنظیم Logger برای نمایش رنگی در ترمینال و ذخیره در دیتابیس."""

    if log_repository is None:
        raise ValueError("Log repository must be provided for logging setup.")

    if not logging.getLogger().hasHandlers():
        logger = logging.getLogger()  # Logger اصلی
        logger.setLevel(logging.DEBUG)

        # نمایش لاگ با رنگ در ترمینال
        coloredlogs.install(
            level='DEBUG',
            logger=logger,
            fmt='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level_styles={
                'debug': {'color': 'green'},
                'info': {'color': 'blue'},
                'warning': {'color': 'yellow'},
                'error': {'color': 'red'},
                'critical': {'color': 'red', 'bold': True},
            },
            field_styles={
                'asctime': {'color': 'cyan'},
                'name': {'color': 'white'},
                'levelname': {'color': 'white', 'bold': True},
                'funcName': {'color': 'magenta'},
            }
        )

       
        import re
        def remove_ansi_codes(text: str) -> str:
            
            ansi_escape = re.compile(r'\x1b\[[0-?]*[ -/]*[@-~]')
            return ansi_escape.sub('', text)
        class QueueLogHandler(logging.Handler):
            def emit(self, record):
                try:
                    message = record.getMessage()
                    clean_message = remove_ansi_codes(message)  
                    # اضافه کردن لاگ به کیو
                    log_repository.log_queue.put({
                        'level': record.levelname,
                        'message': clean_message,
                        'function_name': record.funcName,
                        'filename': record.pathname,
                        'lineno': record.lineno
                    })
                except Exception as e:
                    print(f"[QueueLogHandler] خطا در افزودن به کیو: {str(e)}")

        # اضافه کردن هندلر کیو
        queue_handler = QueueLogHandler()
        logger.addHandler(queue_handler)
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        #logging.getLogger("requests").setLevel(logging.WARNING)
        logging.getLogger("charset_normalizer").setLevel(logging.WARNING)
        logging.getLogger("asyncio").setLevel(logging.WARNING)
      
        class StaticFileFilter(logging.Filter):
            def filter(self, record):
                if record.name == 'werkzeug':
                    msg = record.getMessage()
                    if ' /static/' in msg:  # فاصله قبل از /static/ برای جلوگیری از false positive
                        return False
                return True

        logging.getLogger('werkzeug').addFilter(StaticFileFilter())
        # شروع ترد برای ذخیره لاگ‌ها از کیو به دیتابیس
        log_repository.start_queue_processor()
