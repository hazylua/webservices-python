package calc;

import javax.xml.ws.Endpoint;

public class CalculadoraServerPublisher {

  public static void main(String[] args) {
    System.out.print("Server running.");
    Endpoint.publish("http://192.168.100.87:80/calc", new CalculadoraServerImpl());
  }
}