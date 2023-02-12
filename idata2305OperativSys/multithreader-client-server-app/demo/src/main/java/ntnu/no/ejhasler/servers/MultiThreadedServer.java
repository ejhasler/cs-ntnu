package ntnu.no.ejhasler.servers;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import ntnu.no.ejhasler.computation.AsyncSearchSimulator;

/**
 * A class that implements a multithreaded server.
 * 
 * @author Even Johan Pereira Haslerud
 * @version 12.02.2023
 */
public class MultiThreadedServer implements Runnable {

    /*
     * The port that the server listens to
     */
    protected int serverPort = 8080;

    /*
     * The server socket that listens for incoming client requests
     */
    protected ServerSocket serverSocket = null;

    /*
     * A flag indicating wether the server is stopped
     * or running
     */
    protected boolean isStopped = false;

    /**
     * Constructor for the MultiThreadedServer class.
     * 
     * @param port The port that the server listens on
     */
    public MultiThreadedServer(int port) {
        this.serverPort = port;
    }

    /**
     * Starts the multithreaded server.
     */
    public void run() {
      System.out.println("Multithreaded server listening to port: " + serverPort);

        openServerSocket();

        while (!isStopped()) {
          Socket clienSocket = null;
          try {
            clienSocket = this.serverSocket.accept();

            new Thread(
              new AsyncSearchSimulator(
                clienSocket, 
                "Multithreaded Server: "
              )
            ).start();

          } catch (Exception e) {
            stop();
            e.printStackTrace();
          }
        }

        System.out.println("Server Stopped.");
    }

    /**
     * A synchronized method to check if the server is stopped.
     * 
     * @return Wether the server is stopped or not
     */
    private synchronized boolean isStopped() {
        return this.isStopped;
    }

    /**
     * A synchronized method to stop the server.
     */
    public synchronized void stop() {
      this.isStopped = true;
      try {
        this.serverSocket.close();
      } catch (IOException e) {
        throw new RuntimeException("Error closing the server", e);
      }
    }

    /**
     * A method to open the server socket on the specified part.
     */
    private void openServerSocket() {
        try {
          this.serverSocket = new ServerSocket(this.serverPort);
        } catch (IOException e) {
          throw new RuntimeException("Can not open port 8080", e);
        }
    }
}