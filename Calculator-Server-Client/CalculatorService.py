class Calculator:
    
    operators: tuple[str] = ("+","-","*","/")
    
    @staticmethod
    def receive_expression(userInput='') -> str:
        operation = userInput[0]
        operands = userInput[1]
                    
        result = Calculator.calculate_expression(operation, operands)
        return result

            
    @staticmethod
    def calculate_expression(operation, operands)-> str:
       joined_operands = f" {operation} ".join(map(str, operands))
       result = eval(f"{operation}(*{operands})")  # Ensure operands are unpacked correctly
       return f'\n{joined_operands} = {result}'
        
