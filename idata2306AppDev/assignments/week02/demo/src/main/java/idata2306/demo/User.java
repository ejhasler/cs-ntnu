package idata2306.demo;

/**
 * Represents a simple user.
 * 
 * @author  Even Johan Pereira Haslerud
 * @version 23.03.2023
 * @since   23.03.2023
 */
public class User {

    /** The firstname of the User */
    private final String firstName;

    /** The lastname of the User */
    private final String lastName;

    /**
     * Creates an instance of the User.
     * 
     * @param firstName The firstname of the User.
     * @param lastName  The lastname of the User.
     */
    public User(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    /**
     * Returns the firstname of the User.
     * 
     * @return the firstname of the User.
     */
    public String getFirstName() {
        return firstName;
    }

    /**
     * Returns the lastname of the User.
     * 
     * @return the lastname of the User.
     */
    public String getLastName() {
        return lastName;
    }
}
