import logging

logger = logging.getLogger(__name__)

class Calculator:
    def __init__(self):
        logger.debug("Initializing Calculator")
        pass

    @staticmethod      
    def calculate_total(self, *x: float) -> float:
        """Add multiple numbers"""
        logger.debug(f"calculate_total called with {len(x)} values")
        result = sum(x)
        logger.debug(f"calculate_total result: {result}")
        return result    
    
    @staticmethod
    def multiply(self, *x: float) -> float:
        """Multiply multiple numbers"""
        logger.debug(f"multiply called with {len(x)} values")
        result = 1
        for num in x:
            result *= num
        logger.debug(f"multiply result: {result}")
        return result
    
    @staticmethod
    def calcuate_average(self, total:float, days:float) -> float:
        """Calculate average of multiple numbers"""
        logger.debug(f"calcuate_average called with total={total}, days={days}")
        
        if days>0 :
            result = total/days
            logger.debug(f"calcuate_average result: {result}")
            return result
        
        logger.debug("calcuate_average: days is 0, returning 0")
        return 0                        