#include "Circle.hpp"
#include <iostream>

using namespace std;

// Function declaration for exercise2 which takes an integer radius.
void exercise2(int radius);

int main() {
  double radius = 5.0; // Initialize radius with a double value.
  exercise2(static_cast<int>(radius));

  return 0;
}

// Function definition for exercise2.
// Takes an integer radius and uses it to create a Circle object.
// It then prints out the area and circumference of the circle.
void exercise2(int radius) {

  cout << "\n\tExercise 2)" << endl;

  // Create a Circle object using the given integer radius.
  Circle circle(radius);

  // Compute and print the area of the circle.
  int area = circle.get_area();
  cout << "Area equal to " << area << endl;

  // Compute and print the circumference of the circle.
  // The circumference is stored in a double to maintain precision.
  double circumference = circle.get_circumference();
  cout << "Circumference equal to " << circumference << endl;
}
