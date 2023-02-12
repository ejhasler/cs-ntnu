package ntnu.no.ejhasler.computation;


import java.io.PrintWriter;
import java.net.Socket;

import ntnu.no.ejhasler.utils.ResponseGenerator;

/**
 * A class that implements a multithreaded search simulator.
 * This class implement the Runnable interface, allowing
 * for asynchronous processing of client requests.
 * 
 * @author Even Johan Pereira Haslerud
 * @version 12.02.2023
 */
public class AsyncSearchSimulator implements Runnable {

    /*
     * The socket that the client request is received on
     */
    protected Socket clientSocket = null;

    /*
     * The type of server being used for the request.
     */
    protected String serverText = null;
  
    /**
     * Constructor
     * 
     * @param clientSocket The socket that the client request is received on
     * @param serverText   The type of server being used for the request
     */
    public AsyncSearchSimulator(Socket clientSocket, String serverText) {
      this.clientSocket = clientSocket;
      this.serverText = serverText;
    }
  
    /**
     * Processes the client request asynchronously.
     */
    public void run() {
        try {
            SearchSimulator.processClientRequest(clientSocket, "Multithreaded");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
