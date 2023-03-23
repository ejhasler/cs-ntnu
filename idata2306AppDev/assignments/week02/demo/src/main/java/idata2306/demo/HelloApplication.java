package idata2306.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * This is the main application class.
 * It calls SprintApplication.run() where
 * all the magic starts to happen.
 * 
 * @author  Even Johan Pereira Haslerud
 * @version 23.03.2023
 * @since   23.03.2023
 */
@SpringBootApplication
public class HelloApplication {

    /**
     * The run method of the Hello Application class.
     * 
     * @param args  method name of the String array.
     */
    public static void main(String[] args) {
        SpringApplication.run(HelloApplication.class, args);
    }
    
}
