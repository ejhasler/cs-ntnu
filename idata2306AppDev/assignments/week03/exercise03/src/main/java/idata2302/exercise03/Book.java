package idata2302.exercise03;

import org.springframework.stereotype.Indexed;

/**
 * Data structure for storing book data.
 * 
 * @param id                Unique ID
 * @param title             Title of the book
 * @param year              The year when the book was published
 * @param numberOfPages     Number of pages
 * 
 * @author Even Johan Pereira Haslerud
 * @version 18.02.2023
 */
public record Book(int id, String title, int year, int numberOfPages) {
}
