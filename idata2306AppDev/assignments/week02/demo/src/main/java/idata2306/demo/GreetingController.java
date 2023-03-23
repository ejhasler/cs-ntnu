package idata2306.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * A REST API controller which responds to HTTP
 * requests for /hello.
 * 
 * @author  Even Johan Pereira Haslerud
 * @version 23.03.2023
 * @since   23.03.2023
 */
@RestController
public class GreetingController {
    
    /**
     * Returns string "Hello, World", when
     * mapping /hello is requested.
     * 
     * @return the string when /hello is requested.
     */
    @GetMapping("/hello")
    public String greeting() {
        return "Hello, World";
    }
}
