package ntnu.no.ejhasler.servers;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

import javax.management.RuntimeErrorException;

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
        System.out.println("Single-threaded server listening on port: " + serverPort);
        openServerSocket();
        Socket clientSocket;

        while (!isStopped()) {
            try {
                clientSocket = this.serverSocket.accept();
                SearchSimulator.processClientRequest(clientSocket, "SingleThreaded");
            } catch (Exception e) {
                System.out.println("Error accepting client connection");
            }
        }

        System.out.println("Server Stopped.");
    }

    private synchronized boolean isStopped() {
        return this.isStopped;
    }

    /**
     * Checks if it's stopped and if true,
     * it will close the server socket.
     */
    public synchronized void stop() {
        this.isStopped = true;
        try {
            this.serverSocket.close();
        } catch (IOException e) {
            throw new RuntimeException("Error closing server", e);
        }
    }

    /**
     * Opens the server socket.
     */
    private void openServerSocket() {
        try {
            this.serverSocket = new ServerSocket(this.serverPort);
        } catch (IOException e) {
            throw new RuntimeException("Cannot open port 8080", e);
        }
    }

}
