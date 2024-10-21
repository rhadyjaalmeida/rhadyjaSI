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
        return f'\n{f' {operation} '.join(operands)} = {eval(f'{operation}'.join(operands))}'
        