import logging

## logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"), # To define the name where logs are saved
        logging.StreamHandler() # To sure the logs are been writed in the log file
    ]
)

logger=logging.getLogger("ArithmethicApp")

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def substract(a, b):
    result = a - b
    logger.debug(f"Substract {a} - {b} = {result}")
    return result 

def multiply(a, b):
    result = a * b
    logger.debug(f"Multipliying {a} * {b} = {result}")
    return result 

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Substract {a} / {b} = {result}")
        return result
    except ZeroDivisionError as e:
        logger.error("Division by zero error")
        return None
    
add(10,15)
substract(15,10)
multiply(10,20)
divide(20,5)