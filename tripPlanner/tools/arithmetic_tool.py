from utils.calculator import Calculator
from langchain.tools import tool
import logging

logger = logging.getLogger(__name__)

class ArithmeticTool:
    def __init__(self):
        logger.debug("Initializing ArithmeticTool")
        self.calculator = Calculator()
        self.tools_list = self._setup_tools()
        logger.debug(f"ArithmeticTool initialized with {len(self.tools_list)} tools")

    def _setup_tools(self):
        logger.debug("Setting up arithmetic tools...")
        @tool
        def sum_expense(*x: float) -> float:
            """Add multiple numbers"""
            logger.debug(f"sum_expense called with {len(x)} values")
            result = self.calculator.calculate_total(*x)
            logger.debug(f"sum_expense result: {result}")
            return result
        
        @tool
        def multiply(*x: float) -> float:
            """Multiply multiple numbers"""
            logger.debug(f"multiply called with {len(x)} values")
            result = self.calculator.multiply(*x)
            logger.debug(f"multiply result: {result}")
            return result
        
        @tool
        def calculate_average(total:float, days:float) -> float:
            """Calculate average of multiple numbers"""
            logger.debug(f"calculate_average called with total={total}, days={days}")
            result = self.calculator.calcuate_average(total, days)
            logger.debug(f"calculate_average result: {result}")
            return result
        
        return [sum_expense, multiply, calculate_average]