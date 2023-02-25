# Movie Ticket Booking System

This is a simple command-line application that demonstrates thread synchronization in Java. The application simulates a movie ticket booking system where multiple users can book tickets for a movie concurrently.

## Table of Content:

- [Getting Started](#getting-started)
- [Observation](#observation)
- [Built With](#built-with)
- [Authors](#authors)

## Getting Started

### Prerequisities

- Java 9 or higher installed on your system.
- An IDE (Integrated Development Environment) like Eclipse or IntelliJ IDEA.

### Installing

1. Clone the repository or download the zip file.
2. Extract the files to a directory of your choice.
3. Open the project in your IDE.

### Running the Application

1. Open the **Main.java** file
2. Run the **main** method
3. Observe the order and content of logs
4. Make a note of the _Available tickets_ value for each user.

## Observation

When you run the application, you will notice that the order and content of the logs is not what you would expect. You will also notice that some users are able to book more tickets than the number of available tickets.

This is because multiple threads are accessing the shared **MovieTicketServer** object concurrently without synchronization, resulting in race condition and data inconsistencies.

To fix this issue the **bookTicket** method in **MovieTicketServer** has been synchronized, which ensures that only one thread can access the shared object at any given time. With this change, the logs should now show that users are able to book tickets correctly without exceeding the number of available tickets.

## Built With

- Java - Programming languaged used
- Visual Studio Code - Integrated Development Environment used

## Authors

- Even Johan Pereira Haslerud
- Teacher teaching the subject Operating System.
