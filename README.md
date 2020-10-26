# Python Webservices

Exemplo de um cliente em python acessando e consumindo serviços SOAP por WSDL fornecido por um servidor em java. O cliente consome os métodos SOAP por meio do pacote `suds-community` (SUDS).

# Instruções - Windows

Para compilador o servidor (utiliza a versão 8 do JDK):

`javac --release 8 ./*.java -d bin`

Para executar o servidor:

`java -cp .\bin calc.CalculadoraServerPublisher`

Para executar o código do cliente:

`python Client.py`
