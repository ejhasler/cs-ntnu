#ifndef SOME_HEADER_FILE_GUARD
#define SOME_HEADER_FILE_GUARD

// Defining the value of pi
const double pi = 3.141592;

// Circle class declaration
class Circle {
public:
  // Constructor that initializes the Circle with a given radius
  Circle(double radius_);

  // Function to calculate and return the circumference of the Circle.
  // Circumference is calculated as 2 * pi * radius.
  double get_circumference();

  // Function to calculate and return the area of the Circle.
  // Area is calculated as pi * radius^2.
  double get_area() const { return pi * radius * radius; };

  // Getter for the radius of the Circle.
  double get_radius() const { return radius; };

private:
  double radius;
};

#endif
