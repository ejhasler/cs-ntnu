# <div align="center"> OS Assignment 1 - IDATA2305</div>

## Table of Content:
1. [About the assignment](#about-the-assignment)
2. [Getting started](#getting-started)
    1. [Directory Structure](#directory-structure)
    2. [How to start the application](#how-to-start-the-application)
3. [Questions and Answers](#questions-and-answers)
4. [Assignment Results](#assignment-results)

## About the assignment

This assigment in the course IDATA 2305 - Operating System is about observing and understanding difference between single-threaded and multi-threaded processes in terms of performance in the context of a simple client-server program. The goal of the assignment is to compare the performance of a single-threaded process with that of a multi-threaded processes and to understand the benefits of using multi-threading in such scenarios.

In the assignment, a simple client-server program was implemented, and the performance was measured in both single-threaded and multi-threaded modes. By comparing the time taken to complete all tasks in each mode, the assignment provides insight into the advantages of using multi-threading in a client-server program.

The results of the assignment demonstrates the importance of considering the use of multithreading in our programs and provide a pracitcal example of how it can improve efficiency and speed of a program. By understanding the difference between single-threading and multi-threading processes and the benefits of multi-threading, we can make informed decisions about the design and implementation of our programs, leading to improved performance and scalability.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting started

### Directory Structure

```
.
├── computation
│   ├── AsyncSearchSimulator.java
│   └── SearchSimulator.java
├── Main.java
├── servers
│   ├── MultiThreadedServer.java
│   └── SingleThreadedServer.java
└── utils
    └── ResponseGenerator.java
```

### How to start the application

Here's a step-by-step guide on how to set up and run the program:

1. Open the *Main.java* class in your preferred Java development environment.
2. Set the desired port number by assigning a value to the *Main.serverPort* variable. For example:

```
serverPort = 8080;
```

3. Choose the desired server mode by setting the value of *Main.singleThread* variable. If you want to run the program in single-thread, set it to true:

```
singleThread = true;
```

If you want to run the program in multi-threaded mode, set it to false:

```
singleThread = false;
```

4. Run the Main Application.
5. Send an HTTP GET request using a tool like Postman, specifying the localhost and the choosen port number in the URL. For example:

```
localhost:8080
```

6. Check the results of the request in the terminal window. You should see the response from the server indicating the completion of the request.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Questions and Answers

**Question:** Why do we want to run the server on it's own thread? Can we not run it on the main thread itself?

**Answer:** It is possible to run a server on the main thread, but it's generally not recommneded. There are several reasons why running a server on a separate thread is desirable

1. Responsivness: Running a server on the main thread can block the main thread, which means that the user interface will not be responsive until the server finishes it's work. This can result in poor user experiences, especially if the server is performin a time-consuming task.

2. Scalability: When a server runs on the main thread, it's performance is limited by the performance of the main thread. If the server receives a large number of request simultaneously, it can cause the main thread to become overloaded and result in poor performance. Running the server on it's own thread allows it to handle multiple requests concurrently, improving scalability.

3. Isolation: Running a server on a separate thread provides isolation from the main thread. This means that any issues or crashes in the server will not affect the main thread and vice versa. This can improve the stability of the application and make it easier to debug.

In conclusion, while it is possible to run a server on the main thread, runnin it on a separate thread is a more robust and scalable solution.

## Assignment Results

The results of the assignment serve as an illustration of the difference in performance between single-threaded and multi-threaded processes in a simple client-server program. By comparing the time taken to complete all tasks in each mode, the results provide valuable insight into the benefits of using multi-threading in such scenarios. By understanding the advantages of multi-threading, we can make informed decisions about the design and implementation of our programs, leading to improved performance and scalability. The results of this assignment demonstrate the importane of considering the use of multi-threading in our programs, and provide a practical example of how it can improve efficiency and speed of a program.

### SingleThread V.S. MultiThread

**Single-Threaded**

Single-threaded processes run on a single thread, meaning that only one task can be executed at a time. This can result in slow performance if the task takes a long time to complete, as the program must wait for it to finish before moving on to the next task. Single-threaded processes are typically used in simple applications where the workload is small and does not require parallel processing. The resulst obtained in the assignment for the single-threaded process (20.02 seconds) may have been affected by the time taken to complete a single task and the lack of parallel processing capabilities. In general, single-threaded processes are less efficient than multi-threaded processes, especially for complex or resource-intensive tasks.

Output:
* Time: 20.2s
* Status: 200 OK

**Multi-Threaded**

Multi-threaded processes, on the other hand, can run multiple tasks simultaneously by dividing the workload into multiple threads. Each thread operates independently and can run a separate task at the same time, allowing for parallel processing and improved performance. In multi-threaded processes, tasks can be executed concurrently, reducing the total time taken to complete all tasks. This can result in faster performance and improved scalability, especially when dealing with a large number of requests. The results obtained in the assignment for the multi-threaded process (10.02 seconds) demonstrate the benefits of multi-threading, as the program was able to complete all tasks in less time compared to the single-threaded process. In general, multi-threading is a powerful technique that can greatly improve the performance and efficiency of a program.

Output:
* Time: 10.02s
* Status: 200 OK

The assignment aimed to study the difference in performance between single-threaded and multi-threaded processes in a simple client-server program. The results showed that the multi-threaded process took 10.02 seconds to complete, while the single-threaded process took 20.02 seconds. This indicates that the multi-threaded process was more efficient and performed faster than the single-threaded process.

This highlights the importance of using multi-threading in such scenarios where multiple requests need to be handled simultaneously, as it can lead to significant improvements in performance. The results of this assignment provide insight into how multi-threading can improve the speed and efficiency of a program, especially when dealing with a large number of requests.
