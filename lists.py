clients = []

clients.append("john")
clients.append("Mary")

new_client = input("new client name: ")
clients.append(new_client)

for client in clients:
    print(client)