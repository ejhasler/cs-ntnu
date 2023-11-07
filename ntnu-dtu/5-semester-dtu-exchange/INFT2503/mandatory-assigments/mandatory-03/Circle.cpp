#include "Circle.hpp"

// Returns the circumference of the circle.
// The circumference is calculated as 2 * pi * radius.
double Circle::get_circumference() {
  return 2.0 * pi * radius;
}

// Constructs for the Circle class.
// Initializes a new instance of the Circle class with the specified radius.
Circle::Circle(double radius_) : radius(radius_){};
