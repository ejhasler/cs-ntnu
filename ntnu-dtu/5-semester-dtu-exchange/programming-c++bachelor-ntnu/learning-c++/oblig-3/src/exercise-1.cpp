#include "exercise-1.h" // Include the header for exercise 1

const double pi = 3.141592;

Circle::Circle(double radius_) : radius(radius_) {}

int Circle::get_area() const {
    return pi * radius * radius;
}

double Circle::get_circumference() const {
    return 2.0 * pi * radius;
}
