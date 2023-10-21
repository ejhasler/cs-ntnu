#include <iostream>
#include "exercise-1.h" 
#include "exercise-2.h" 

using namespace std;

void exercise2() {
    Circle circle(5);

    double area = circle.get_area();
    cout << "Arealet er lik " << area << endl;

    double circumference = circle.get_circumference();
    cout << "Omkretsen er lik " << circumference << endl;
}
