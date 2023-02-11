package ntnu.no.ejhasler.computation;

import java.io.PrintWriter;
import java.net.Socket;

import ntnu.no.ejhasler.utils.ResponseGenerator;

public class SearchSimulator {

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
