package ntnu.no.ejhasler.utils;

/**
 * Class for generating HTTP responses for the server.
 * 
 * @author Even Johan Pereira Haslerud
 * @version 12.02.2023
 */
public class ResponseGenerator {

    /**
     * Generates an HTML response for the client.
     * 
     * @param title The title of the response
     * @param time1 The first time value to include in the reponse
     * @param time2 The second time value to include in the response
     * @return      The generated HTML response as a string
     */
    public static String generatorResponseHTML(String title, long time1, long time2) {
      return ("<html><body>" + title +
          "Singlethreaded Server: " +
          time1 + " - " + time2 +
          "</body></html>");
    }
  
    /**
     * Generates a header for the HTTP response.
     * 
     * @param contentLength The length of the content of the response
     * @return              The generated header as a string
     */
    public static String generatorResponseHeader(int contentLength) {
      return ("HTTP/1.1 200 OK\r\n" +
          "Content-Type: text/html; charset=UTF-8\r\n" +
          "Content-Length: " + contentLength +
          "\r\n\r\n");
    }
  }
