import socket
import threading

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Criação do socket do servidor utilizando os protocolos TCP/IP

HOST = '127.0.0.1'
PORTA = 7777

servidor.bind((HOST, PORTA)) #Vincula o endereço IP e a porta ao socket do servidor e configura o chat para ouvir conexões
servidor.listen()
print("\nChat iniciado!")

#Criação de duas listas para armazenar os sockets e nomes dos clientes
clientes = []
apelidos = []
 
def enviarMensagem(mensagem): #Função que envia uma mensagem para todos os clientes conectados
    for cliente in clientes:
        cliente.send(mensagem)
 
def manipular(cliente, apelido): #Função que lida com a comunicação de um cliente específico
    while True:
        try:
            mensagem = cliente.recv(1024).decode('utf-8')
            if mensagem == "Sair":
                cliente.close()
                indice = clientes.index(cliente)
                clientes.remove(cliente)
                apelido = apelidos[indice]
                apelidos.remove(apelido)
                enviarMensagem(f"{apelido} saiu do chat".encode('utf-8'))
                print(f"{apelido} saiu do chat")
                break
            else:
                enviarMensagem(f"[{apelido}]: {mensagem}".encode('utf-8'))
        except:
            indice = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            apelido = apelidos[indice]
            apelidos.remove(apelido)
            enviarMensagem(f"{apelido} desconectou do chat.".encode('utf-8'))
            break

def receber(): #Função que aceita novas conexões de clientes
    while True:
        cliente, endereco = servidor.accept()
        cliente.send("apelido".encode('utf-8'))
        apelido = cliente.recv(1024).decode('utf-8')
        apelidos.append(apelido)
        print(f"O usuário {apelido} se conectou no chat! Endereço: {endereco}")
        clientes.append(cliente)
        cliente.send("Conectado ao chat!".encode('utf-8'))
        thread = threading.Thread(target=manipular, args=(cliente, apelido))
        thread.start()

receber()
