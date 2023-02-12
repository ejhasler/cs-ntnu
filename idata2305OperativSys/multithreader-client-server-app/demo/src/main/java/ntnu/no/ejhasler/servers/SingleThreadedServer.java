package ntnu.no.ejhasler.servers;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

import javax.management.RuntimeErrorException;

import ntnu.no.ejhasler.computation.SearchSimulator;

/**
 * Responsible for creating and runnig the single-threaded server.
 * 
 * @author Even Johan Pereira Haslerud
 * @version 12.02.2023
 */
public class SingleThreadedServer implements Runnable {

    /*
     * Port number where the server listens to incoming connections
     */
    protected int serverPort = 8080;

    /*
     * Server socket instance for creating a socket for the
     * server to listen to incoming connections
     */
    protected ServerSocket serverSocket = null;

    /*
     * Flag to check if the server is stopped.
     */
    protected boolean isStopped = false;

    /**
     * Constructor for SingleThreadServer, sets the server
     * port number.
     * 
     * @param port Port number for the server to listen to
     *              incoming connections.
     */
    public SingleThreadedServer(int port) {
        this.serverPort = port;
    }

    /**
     * Overriden run method of the Runnable Interface, it opens
     * the server socket, listens to incoming connections
     * and processes them using SearchSimulator.processClientRequest.
     * 
     * If any errors occurs while accepting the client connection,
     * it stops the server.
     */
    public void run() {
        System.out.println("Single-threaded server listening on port: " + serverPort);
        openServerSocket();
        Socket clientSocket;

        while (!isStopped()) {
            try {
                clientSocket = this.serverSocket.accept();
                SearchSimulator.processClientRequest(clientSocket, "SingleThreaded");
            } catch (Exception e) {
                stop();
                System.out.println("Error accepting client connection");
            }
        }

        System.out.println("Server Stopped.");
    }

    /**
     * Synchronized method to check if the server
     * is stopped.
     * 
     * @return boolean value indicating if the 
     *         server is stopped.
     */
    private synchronized boolean isStopped() {
        return this.isStopped;
    }

    /**
     * Synchronized method to stop the server
     * and close the server socket.
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
     * Method to open the server socket.
     */
    private void openServerSocket() {
        try {
            this.serverSocket = new ServerSocket(this.serverPort);
        } catch (IOException e) {
            throw new RuntimeException("Cannot open port 8080", e);
        }
    }

}
