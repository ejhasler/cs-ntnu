#include <iostream>

using namespace std;

int exercise5() {

  double number;

  double *ptr = &number;
  double &ref = number;

  number = 42.0;

  *ptr = 23.5;

  ref = 10.8;

  std::cout << "Number" << number << std::endl;

  return 0;
}
