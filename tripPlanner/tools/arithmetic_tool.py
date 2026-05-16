from utils.calculator import Calculator
from langchain.tools import tool

class ArithmeticTool:
    def __init__(self):
        self.calculator = Calculator()
        self.tools_list = self._setup_tools()

    def _setup_tools(self):
        @tool
        def sum_expense(*x: float) -> float:
            """Add multiple numbers"""
            return self.calculator.calculate_total(*x)
        
        @tool
        def multiply(*x: float) -> float:
            """Multiply multiple numbers"""
            return self.calculator.multiply(*x)
        
        @tool
        def calculate_average(total:float, days:float) -> float:
            """Calculate average of multiple numbers"""
            return self.calculator.calcuate_average(total, days)
        
        return [sum_expense, multiply, calculate_average]