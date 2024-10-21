import socket
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 15000         
operators = ("+","-","*","/")

client_socket.connect((host, port))        

def operations_menu():
    
    operation: str = input('Escolha uma das operações abaixo ou digite \'bye\' para sair.\n + Soma\n - Subtração\n * Multiplicação\n / Divisão.\n -> ').strip()
    
    while not operation in operators:
        if operation =='bye':
            return 'bye'
        print('Operador inválido.\n')
        operation: str = input('Escolha uma das operações abaixo ou digite \'bye\' para sair.\n + Soma\n - Subtração\n * Multiplicação\n / Divisão.\n -> ').strip()
        
    return operation

def operands_menu(): 
        
    operands: list[str] = input('Digite até 20 números separados por espaço.\n -> ').strip().split()
    
    while not all(operand.isnumeric() for operand in operands) or len(operands)>20 or len(operands)<2:
        if 'bye' in operands:
            return ['bye']
        
        print('Operando não numérico identificado ou quantidade de operandos é menor que 2 ou maior que 20.\n')
        operands: list[str] = input('Digite 2 a 20 números separados por espaço.\n -> ').strip().split()
        
    return operands
    
def recursive_connection():
    
    with client_socket:
        while True:    
            operation: str = operations_menu()
            client_socket.send(operation.encode('utf-8'))
            
            server_response = client_socket.recv(1024).decode('utf-8')
            
            if server_response == 'Bye!':
                print(server_response)
                break
            
            operands = operands_menu()
            operands = json.dumps(operands).encode('utf-8')
            
            client_socket.send(operands)
            
            server_response = client_socket.recv(1024).decode('utf-8')
            
            if server_response == 'Bye!':
                server_response = 'Bye!'
                print(server_response, end='\n\n')
                break
            
            print(server_response, end='\n\n')
                
        client_socket.close()
            
        
if __name__ == '__main__':
    recursive_connection()
