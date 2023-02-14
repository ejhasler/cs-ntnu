package com.packt.cardatabase.domain;

import java.util.List;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

/**
 * CarRepository extends the Spring Boot JPA CrudRepository interface.
 * The <Car, Long> type arguments define that this is the repository for the Car
 * entity class and that the type of the ID field is Long.
 * 
 * @author Even Johan Pereira Haslerud
 * @version 14.02.2023
 */
public interface CarRepository extends CrudRepository<Car, Long> {
}