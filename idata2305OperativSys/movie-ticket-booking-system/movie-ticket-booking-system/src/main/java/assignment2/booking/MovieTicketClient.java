package assignment2.booking;

public class MovieTicketClient extends Thread{

    private String customerName;
    private int numberOfTickets;
    private MovieTicketServer server;

    public MovieTicketClient(String customerName, int numberOfTickets, MovieTicketServer server) {
        this.customerName = customerName;
        this.numberOfTickets = numberOfTickets;
        this.server = server;
    }

    public void run() {
        server.bookTicket(customerName, numberOfTickets);
    }
}
