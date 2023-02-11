package ntnu.no.ejhasler.servers;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import ntnu.no.ejhasler.computation.AsyncSearchSimulator;

/**
 * MultiThreadedServer
 */
public class MultiThreadedServer implements Runnable {

  protected int serverPort = 8080;
    protected ServerSocket serverSocket = null;
    protected boolean isStopped = false;

    public MultiThreadedServer(int port) {
        this.serverPort = port;
        this.isStopped = false;
    }

    public void run() {
        openServerSocket();
        Socket clientSocket = null;

        while (!isStopped()) {
          try {
            clientSocket = this.serverSocket.accept();
          } catch (IOException e) {
            throw new RuntimeException("Error accepting client connection", e);
          }

            new Thread(
              new AsyncSearchSimulator(
                clientSocket, 
                "Multithreaded Server"
              )
            ).start();
        }

        System.out.println("Server Stopped.");
    }

    private synchronized boolean isStopped() {
        return this.isStopped;
    }

    public synchronized void stop() {
        // implementation to stop the server from the main thread if needed
    }

    private void openServerSocket() {
        // open server socket here
    }
}