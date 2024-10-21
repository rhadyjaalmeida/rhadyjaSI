import socket
import json
from CalculatorService import Calculator

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8081

server_socket.bind((host, port))

server_socket.listen(2)

print(f"Server listening on {host}:{port}")

def maintain_server_connection():
    client_socket, address = server_socket.accept()
    print(f"conexão de {address} estabelecida")
    
    with client_socket:
        while True:
            print('Nova consulta:')
            operation = client_socket.recv(1024).decode('utf-8')
            
            if operation == 'bye':
                server_response = 'Bye!'
                client_socket.send(server_response.encode('utf-8'))
                break 
            
            client_socket.send(operation.encode('utf-8'))
            
            print('operator:', operation)
            _operands = client_socket.recv(1024)
            operands = json.loads(_operands.decode('utf-8'))
            print('operands:',operands)
            
            if 'bye' in operands:
                server_response = 'Bye!'
                client_socket.send(server_response.encode('utf-8'))
                break 
            
            expression_result: str = Calculator.receive_expression([operation, operands])
            print(expression_result)
            client_socket.send(expression_result.encode('utf-8'))
                
        
        client_socket.close()
    

                
        
if __name__=='__main__':
    maintain_server_connection()