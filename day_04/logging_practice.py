import logging

# logging.basicConfig(filename='logfile.log', level=logging.DEBUG)

logger = logging.getLogger("kenny")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("kenny_logger.log")
file_handler.setLevel(logging.ERROR)
# Create a formatter to specify output
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Add the formatter to the handlers
file_handler.setFormatter(file_formatter)


stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
# Create a formatter to specify output
strm_formatter = logging.Formatter('%(levelname)s : %(message)s')
# Add the formatter to the handlers
stream_handler.setFormatter(strm_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.debug("There are lost of bugs")
logger.error("Something bad happened")
logger.warning("Danger, Will Robinson")
logger.critical("No more spam!")
logger.debug("Squash the bugs")