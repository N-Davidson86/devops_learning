import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test_1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('TestLogger')

logger.debug('это режим отладки')
logger.info("Это информационное сообщение")
logger.warning("Это предупреждение")
logger.error("Это ошибка")
