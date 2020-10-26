from suds.client import Client

url = "http://192.168.100.87:80/calc?wsdl"

try:
    # O serviço é uma calculadora em que todos seus métodos recebem apenas dois números.
    x, y = map(float, input("Enter 'x' and 'y': ").split(' ')[:2])
    print(x, y)
    client = Client(url)
    # Exibindo as informações do serviço.
    print(client)
    # Consumindo o método "resto" fornecido pelo serviço.
    print(client.service.resto(x, y))

except:
    print("Error.")
