from logger import logger

def test(a,b):
    logger.info('add two int')
    return a+b

test(4,5)