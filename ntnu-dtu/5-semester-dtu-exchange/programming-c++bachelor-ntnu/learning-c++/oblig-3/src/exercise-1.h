#ifndef EXERCISE_1_H
#define EXERCISE_1_H

class Circle {
public:
    Circle(double radius_);
    int get_area() const;
    double get_circumference() const;

private:
    double radius; // Declaration of the member variable
};

#endif

