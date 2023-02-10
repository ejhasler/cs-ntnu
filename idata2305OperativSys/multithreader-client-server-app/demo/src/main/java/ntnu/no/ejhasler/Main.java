package ntnu.no.ejhasler;

/**
 * Hello world!
 *
 */
public class Main 
{
    private static boolean singleThreaded = true;

    private static int serverPort = 8080;

    /**
     * 
     * @param args
     */
    public static void main(String[] args )
    {
        System.out.println("\n");
        if (singleThreaded) new SingleThreadedServer(serverPort).run();
        else new MultiThreadedServer(serverPort).run(); 
    }
}
