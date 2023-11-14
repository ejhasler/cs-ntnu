#include <iostream>

using namespace std;

int i = 3;
int j = 5;
int *p = &i;
int *q = &j;

void exercise1a() {
  cout << "\n\tExercise 1a)" << endl;
  cout << "----------------------------------\n\n";

  cout << "Variabel i:" << endl;
  cout << "\tAddresse: " << &i << endl;
  cout << "\tContent: " << *p << endl;

  cout << "Variabel j:" << endl;
  cout << "\tAddresse: " << &j << endl;
  cout << "\tContent: " << *q << endl;
}

void exercise1b() {
  cout << "\n\tExercise 1b)" << endl;
  cout << "----------------------------------\n";

  cout << "Output:" << endl;
  *p = 7;
  *q += 4;
  *q = *p + 1;
  p = q;

  cout << *p << " " << *q << endl;
}
