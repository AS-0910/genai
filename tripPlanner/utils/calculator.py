class Calculator:
    def __init__(self):
        pass

    @staticmethod      
    def calculate_total(self, *x: float) -> float:
        """Add multiple numbers"""
        return sum(x)    
    
    @staticmethod
    def multiply(self, *x: float) -> float:
        """Multiply multiple numbers"""
        result = 1
        for num in x:
            result *= num
        return result
    
    @staticmethod
    def calcuate_average(self, total:float, days:float) -> float:
        """Calculate average of multiple numbers"""
        
        if days>0 :
            return total/days
        
        return 0                        