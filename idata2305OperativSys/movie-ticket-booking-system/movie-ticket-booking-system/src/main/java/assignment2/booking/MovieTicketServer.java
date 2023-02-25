package assignment2.booking;

public class MovieTicketServer {

    private String movieName;
    private int availableSeats;
    
    public MovieTicketServer(String movieName, int availableSeats) {
        this.movieName = movieName;
        this.availableSeats = availableSeats;
	}

	public synchronized void bookTicket(String customerName, int numberOfSeats) {
        System.out.println("Hi, " + customerName + " : " + availableSeats + " : Seats available for " + movieName);

        if ((availableSeats - numberOfSeats) < 0) {
            System.out.println("Hi, " + customerName + " : Seats not available for " + movieName);
            return;
        }

        availableSeats -= numberOfSeats;
        System.out.println("Hi, " + customerName + " : " + numberOfSeats + " Seats booked successfully for " + movieName);
    }
}
