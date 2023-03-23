package idata2306.demo;

import java.util.LinkedList;
import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * A REST API controller which responds to HTTP requests
 * for /users.
 * 
 * @author  Even Johan Pereira Haslerud
 * @version 23.03.2023
 * @since   23.03.2023
 */
@RestController
@RequestMapping("users")
public class UserController {

    /**
     * This method is called when an HTTP request to /user/list
     * is received. P.S. We need to specify only /list as the path
     * (URL part) here, becuase the controller is already mapped to
     * /user.
     * 
     * @return  A list of users.
     */
    @GetMapping("/list")
    public List<User> listUsers() {
        List<User> users = new LinkedList<>();
        users.add(new User("Jørgen", "Finsveen"));
        users.add(new User("Håvard", "Vestbø"));
        return users;
    }
    
}
