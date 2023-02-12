package ntnu.no.ejhasler.computation;

import java.io.PrintWriter;
import java.net.Socket;

import ntnu.no.ejhasler.utils.ResponseGenerator;

/**
 * Processes client requests and simulates a search operation.
 * 
 * @author Even Johan Pereira Haslerud
 * @version 12.02.2022
 */
public class SearchSimulator {

    /**
     * Calculates the start and end time of the request processing.
     * 
     * @param socket        The socket that the client request is received on
     * @param serverType    The type of server being used for the request
     * @throws Exception    If there is an error during the processing of the request
     */
    public static void processClientRequest(Socket socket, String serverType) throws Exception {
          long time1 = System.currentTimeMillis();
          System.out.println("Request processing started at: " + time1);
          Thread.sleep(10 * 1000);
          long time2 = System.currentTimeMillis();
          System.out.println("Request processing ended at: " + time2);

          String body = ResponseGenerator.generatorResponseHTML(serverType, time1, time2);
          String header = ResponseGenerator.generatorResponseHeader(body.length());
 
          new PrintWriter(socket.getOutputStream(), true).println(header + body);
    }
}
