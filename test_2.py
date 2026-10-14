import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('disk_check.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('DiskChecker')

logger.info("this is information message")
logger.warning("IT's Warning")
logger.error("This is an error")
