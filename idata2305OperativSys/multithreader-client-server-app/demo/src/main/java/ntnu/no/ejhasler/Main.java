package ntnu.no.ejhasler;

import ntnu.no.ejhasler.servers.*;
/**
 * Main class for starting the server.
 * 
 * @author Even Johan Pereira Haslerud
 * @version 12.02.2023
 */
public class Main {

    /*
     * Flag to determine if the server should run in single-threaded or multi-threaded
     * If set to true, the server will run in single-threaded mode.
     * If set to false, the server will run in multi-threaded mode.
     */
    private static boolean singleThread = false;

    /*
     * Port number for the server to listen on.
     */
    private static int serverPort = 8080;

    /**
     * Starts the application.
     * 
     * @param args 
     */
    public static void main(String[] args) {
        System.out.println("Starting server");

        // Start the server in single-threaded mode.
        if (singleThread) new SingleThreadedServer(serverPort).run();
        // Start the server in multi-threaded mode.
        else new MultiThreadedServer(serverPort).run();
    }


}
