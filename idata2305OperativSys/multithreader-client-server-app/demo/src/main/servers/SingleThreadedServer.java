import java.io.IOException;

import ntnu.no.ejhasler.computation.SearchSimulator;

/**
 * Represents a siglethreaded server. 
 */
public class SingleThreadedServer implements Runnable {
    
    protected int serverPort = 8080;
    protected ServerSocket serverSocket = null;
    protected boolean isStopped = false;

    public SingleThreadedServer(int port) {
        this.serverPort = port;
    }

    public void run() {
        openServerSocket();

        while (!isStopped()) {
            // wait for a connection
            // on receiving a request, execute the heavy computation
            Socket clientSocket = null;
            try {
                clientSocket = this.serverSocket.accept();
                SearchSimulator.processClientRequest(clientSocket, "Single threaded");
            } catch (Exception e) {
                System.out.println("Error accepting client connection", e.getMessage());
            }
        }

        System.out.println("Server stopped.");
    }

    private synchronized boolean isStopped() {
        return this.isStopped;
    }

    public synchronized void stop() {
        this.isStopped = true;
        try {
            this.serverSocket.close();
        } catch (IOException e) {
            throw new RuntimeException("Error closing server", e);
        }
    }

    private void openServerSocket() {
        try {
            this.serverSocket = new ServerSocket(this.serverPort);
        } catch (IOException e) {
            throw new RuntimeException("Cannot open port 8080", e.getMessage());
        }
    }
}
