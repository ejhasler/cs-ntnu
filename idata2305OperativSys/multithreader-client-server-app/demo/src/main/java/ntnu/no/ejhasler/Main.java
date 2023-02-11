package ntnu.no.ejhasler;

import ntnu.no.ejhasler.servers.*;
/**
 * Main class of the application.
 */
public class Main {

    private static boolean singleThread = true;

    private static int port = 8080;
    public static void main(String[] args) {
        System.out.println("Starting server");

        if (singleThread) new SingleThreadedServer(port).run();
        else new MultiThreadedServer(port).run();
    }


}
