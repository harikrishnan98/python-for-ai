# Advance filter Logging
import logging

logger = logging.getLogger("Test")


# Custom format logging

logging.basicConfig(
    filename="logger-details.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

console = logging.StreamHandler()  # Console logger
logger.addHandler(console)

file = logging.FileHandler("error.log")
file.setLevel(logging.ERROR)
logger.addHandler(file)

file_handler_db = logging.FileHandler("db.log")  # Logs in File
file_handler_db.setLevel(logging.CRITICAL)
logger.addHandler(file_handler_db)

file_info = logging.FileHandler("info-examp.log")
file_info.setLevel(logging.INFO)
logger.addHandler(file_info)

logger.info("Hello")


logger.info("WORLD TEST")
logger.error("ERROR_TEST")
logger.critical("DB: ERROR BIG ISSUE")
