package idata2302.exercise03;

/**
 * Data structure storing author data.
 * 
 * @param id            Unique ID
 * @param firstName     Firstname of the author
 * @param lastName      Lastname of the author
 * @param birthYear     Birth year of the author
 */
public record Author(int id, String firstName, String lastName, int birthYear) {
}
