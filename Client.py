import socket
import threading

# Endereço IP do servidor e porta
SERVER = 'Endereço_IP_do_Servidor'
PORT = 12345

# Nome de usuário do cliente
username = input("Digite seu nome de usuário: ")

# Conectando-se ao servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

# Função para enviar mensagens ao servidor
def send_message():
    while True:
        msg = input()
        message = f'{len(msg)}:{username}:{msg}'
        client.send(message.encode('utf-8'))

# Função para receber mensagens do servidor
def receive_message():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            print(msg)
        except socket.error as e:
            print("[ERRO]", e)
            break

# Threads para enviar e receber mensagens simultaneamente
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()