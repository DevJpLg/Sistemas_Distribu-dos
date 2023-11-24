import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

porta = 1111
servidor.bind(('localhost', porta))
servidor.listen(1)

print("\nServidor inicializado na porta", porta)

while True:
    print("Aguardando mensagem...\n")
    transmissor, addr = servidor.accept()
    while True:
        mensagem = transmissor.recv(1024).decode('utf-8')
        if not mensagem:
            print("\nO cliente encerrou a conexão!")
            transmissor.close()
            break
        print("Mensagem recebida do cliente:", mensagem)
    if not mensagem:
        print("Encerrando o servidor...")
        servidor.close()
        break
