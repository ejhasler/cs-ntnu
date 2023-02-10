# <div align="center"> Full Stack Application with Spring Boot and React </div>

## Table of content:

*[Backend Programming with Spring Boot](#backend-programming-with-spring-boot)*

1. [Setting Up the Environment and Tools](#setting-up-the-environment-and-tools)
2. [Dependency Injection](#dependency-injection)
3. [Using JPA to Create and Access a Database](#using-jpa-to-create-and-access-a-database)
4. [Creating a RESTful Web Service with Spring Boot](#creating-a-restful-web-service-with-spring-boot)
5. [Securing and Testing the Backend](#securing-and-testing-the-backend)

*[Frontend Programming with React](#frontend-programming-with-react)*

6. [Setting Up the Environment and Tools](#setting-up-the-enironment-and-tools)
7. [Programming using React](#programming-using-react)
8. [Consuming the REST API with React](#consuming-the-rest-api-with-react)
9. [Useful Third-Party Components for React](#useful-third-party-components-for-react)

*[Full Stack Development](#full-stack-development)*

10. [Setting Up the Frontend for the Spring Boot RESTful Web Service](#setting-up-the-frontend-for-the-spring-boot-restful-web-service)
11. [Adding CRUD Functionalities](#adding-crud-functionalities)
12. [Styling the Frontend with React MUI](#styling-the-frontend-with-react-mui)
13. [Testing the Frontend](#testing-the-frontend)
14. [Securing the Application](#securing-the-application)
15. [Deploying the Application](#deploying-the-application)
16. [New practcises](#new-practises)

## Backend Programming with Spring Boot

In the first section i will install the software needed for backend development and create the first Spring application. Spring Boot is a modern Java-based backend framework that makes development faster than with traditional Java-based frameworks. With Spring boot, we can male a standalone web application that has an embedded application server.

### Setting Up the Environment and Tools

There are a lot of different **integrated development evironment (IDE)** tools that we can use to develop Spring Boot applications. I personally will use Visual Studio Code, which is an open source IDE for multiple programming languages. I will create the first Spring Boot project by using the Spring Initializr project starter function. 

**What is Spring Boot?**

Spring Boot provides a good platform for Java developers to develop a stand-alone and production-grade spring application that you can just run. You can get started with minimum configurations without need for an entire Spring configuration setup. Spring Boot automatically configures your application based on the dependencies you have added to the project by using @EnableAutoConfiguration annotation. For example, if MySQL database is on your classpath, but you have not configured any database connection, then Spring Boot auto-configures an in-memory database. The entry point of the Spring Boot application is the class contains @SpringBootApplication annotation and the main method. Spring Boot automatically scans all the components included in the project by using @ComponentScan annotation.

**What is Visual Studio Code?**

Visual Studio Code is a streamlined code editor with support for development operations like debugging, task running, and version control. 

**What is Maven?**

Apache Maven is a software project management tool that makes the software development process simpler and also unifies the development process. The basis of Maven is the **Project Object Model (POM)**. The POM is a pom.xml file that contains basic information about a project. There are also all the dependencies that Maven should download to be able to build a project. Basic information about a particular project can be found at the beginning of the pom.xml file, which defines - for example - the version of the application, the packaging format, and so on. The minimum version of the pom.xml file should contain the following:
* project root
* modelVersion
* groupId - **Identifier (ID)** of the project group
* artifactId - ID of the project (artifact)
* version - Version of the project (artifact)

**How do we create a Spring Boot project?**

We can create a Spring Boot project using Spring Initializr, which is a web-based tool that's used to create Spring Boot projects. 

**How do we use logging with Spring Boot?**

Logging can be used to monitor our application flow, and it is a good way to capture unexpected errors in your program code. Spring Boot packages provide a logback that we can use for logging without any configuration. The following sample code shoes how you can use logging:

```
@SpringBootApplication
public class CardatabaseApplication {
    private static final Logger logger =
            LoggerFactory.getLogger
                (CardatabaseApplication.class);
  
    private static void main(String[] args) {
        SpringApplication.run
                        (CardatabaseApplication.class, args);
        logger.info("Application started");
        
    }
    
}
```

The logger.info method prints a logging message in the console. 

**How do we find error and log messages in Visual Studio?**

We can find error and log messages with using the seven levels of logging: TRACE, DEBUG, INFO, WARN, ERROR, FATAL, and OFF. And you can configure that the level of logging in your Spring Boot application.properties file. 

### Dependency Injection

The Spring Boot framework provides DI. DI reduces component dependencies and makes our code easier to test and maintain. 

**What is DI?**
DI is a software development technique where we can create objects that depend on other objects. DI helps with interaction between classes but at the same time keeps the classes independent.

There are three types of classes in DI:
* A **service** is a class that can be used (this is the dependency)
* The **client** is a class that uses the dependency.
* The **injector** passes the dependency (the service) to the dependent class (the client).

DI makes classes loosely coupled. This means that the creation of client dependencies is separated from the client's behavior, which makes unit testing easier.

**How does the @Autowired annotation work in Spring Boot?**

Spring Boot scans your application classes and registers classes with certain annotations (@Service, @Repository, and @Controller) as Spring beans. These beans can then be injected using an @Autowired annotation:

```
public class Car {
    @Autowired
    private Owner owner;
    ...
}
```

**How do you inject resources in Spring Boot?**

Java(javafx.annotation) also provides an @Resource annotation that can be used to inject resources. We can define the name or type of the injected bean when using the @Resource annotation. For example, the following code shows some use cases. If we have a resource defined as follow:

```
@Configuration
public class ConfigFileResource {
    @Bean (name="configFile")
    public File configFile() {
      File configFile = new File ("configFile.xml");
      return configFile;
    }
}
```

We can then inject the bean using an @Resource annotation:

```
// By bean name
@Resource(name"configFile")
private ConfigFile cFile

OR

// Without name
@Resource
private ConfigFile cFile
```

### Using JPA to Create and Access a Database

In this section the project is going to dive in on how to use **Java Persistent API (JPA)** with Spring Boot and how to define a database by using entity classes. In the first part we will be using the H2 in-memory database for development. H2 is an in-memory SQL database that is good for fast development. In the second phase, we will move from H2 to use **Maria DB**. This section will also show the creation of CRUD repositories and a one-to-many connection between database tables.

Contains:
* Basic of ORM, JPA, and Hibernate
* Creating the entity class
* Creating CRUD repositories
* Adding relationships between tables
* Setting up the MariaDB database

**What are ORM, JPA, and Hibernate?**

**Object Relational Mapping (ORM)** is a technique that allow us to fetch from and manipulate a database by using object-oriented programming paradigm. ORM is really good for programmers because it relies on object-oriented concepts rather than database structures. It also makes development much faster and reduces the amount of sourde code. ORM is mostly independent of databases, and developers don't have to worry about vendor-specific SQL statements.

**Java Persistent API (JPA)** provides object-relational mapping for Java developers. The JPA entity is a Java class that presents the structure of a database table. The fields of an entity class present columns of the database tables.

**Hibernate** is the most popular Java-based JPA implementation and is used in Spring Boot by default. Hibernate is a mature product and is widely used in large-scale applications. 

**How can you create an entity class?**

An **entity** class is a simple Java class that is annotated with JPA's @Entity annotation. Entity classes use the standard javaBean naming convention and have proper getter and setter methods. To create an entity class in Spring Boot, you must create a package for entites.

**How can you create a CRUDRepository?**

**What does CrudRepository provide for your application?**

**How can you create a one-to-many relationship between tables?**

**How can you add demo data to a database with Spring Boot?**

**How can you connect your Spring Boot application to MariaDB?**
