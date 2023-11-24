import socket

transmissor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

transmissor.connect(('localhost', 1111))

while True:
    mensagem_Transmissor = input('Digite uma mensagem: ')
    if not mensagem_Transmissor:
        print("\nEncerrando conexão...")
        transmissor.close()
        break
    transmissor.send(mensagem_Transmissor.encode())
