package ntnu.no.ejhasler.computation;

import java.net.Socket;

public class AsyncSearchSimulator implements Runnable{
    
    protected Socket clientSocket = null;
    protected String serverText = null;

    public AsyncSearchSimulator(Socket clienSocket, String serverText) {
        this.clientSocket = clientSocket;
        this.serverText = serverText;
    }

    public void run() {
        try {
            SearchSimulator.processClientRequest(clientSocket, "Multithreaded");
        } catch (Exception e) {
            System.out.println("Error processing client request: " + e.getMessage());
        }
    }
}
