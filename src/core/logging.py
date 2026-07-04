import sys
from loguru import logger
from pathlib import Path


LOG_DIR = Path('logs')
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / 'app.log'

logger.remove()
logger.add(sys.stdout, level="INFO", )
logger.add(LOG_FILE, level="INFO")