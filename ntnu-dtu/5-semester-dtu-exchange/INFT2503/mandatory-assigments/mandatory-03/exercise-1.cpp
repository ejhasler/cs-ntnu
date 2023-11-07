#include "Circle.hpp"
#include <iostream>

using namespace std;

// Prototype for function exercise1 which takes a Circle object.
void exercise1(Circle circle);

// Struct to hold computed values of area and circumference.
struct {
  double area;
  double circumference;
} computed, actual;

// Struct to hold boolean flags indicating correctness of computed values.
struct {
  bool area;
  bool circumference;
} is_correct;

int main() {
  double radius = 5.0;   // Set radius of the circle.
  Circle circle(radius); // Create Circle object with specified radius.

  exercise1(circle); // Call exercise1 with the Circle object.
  return 0;
}

// Function to compute and compare the area and circumference of a circle.
void exercise1(Circle circle) {

  cout << "\n\tExercise 1)" << endl;

  // Retrieve the radius from the Circle object.
  double radius = circle.get_radius();

  // Compute area and circumference using Circle's methods.
  computed.area = circle.get_area();
  computed.circumference = circle.get_circumference();

  // Calculate actual area and circumference for comparison.
  actual.area = pi * radius * radius;
  actual.circumference = 2.0 * pi * radius;

  // Check if computed values are equal to the actual values.
  is_correct.area = (computed.area == actual.area);
  is_correct.circumference = (computed.circumference == actual.circumference);

  // Output the results.
  cout << boolalpha;
  cout << "Radius of circle: " << radius << endl;
  cout << "Area of circle: " << computed.area << "\t\t\tCorrect: " << is_correct.area << endl;
  cout << "Circumference of circle: " << computed.circumference << "\tCorrect: " << is_correct.circumference << endl;
}
