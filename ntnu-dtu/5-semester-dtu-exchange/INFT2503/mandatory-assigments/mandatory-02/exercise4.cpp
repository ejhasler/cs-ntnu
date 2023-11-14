#include <iostream>

using namespace std;

void exercise4() {

  // Code with syntax errors:
  //
  // int &b; lacks an initialization for the reference b. References
  //         must always be initialized with an existing variable at their creation
  //         You cannot have an uninitialized reference.
  // int *c; has been declared, but there is no initialization. You need to
  //         assign a valid address to c before using it to point to something.
  //
  // *a = *b + *c; contains stars as if they where pointers, but a, b and c are not declared
  //               as pointers. This will result in a syntax error.
  // &b = 2; attempts to assign the value 2 to the reference b. This is not valid.
  //
  /**
   */

  // Correct syntax below

  int a = 5;
  int b = 0;
  int *c;
  c = &b;
  a = b + *c;
  b = 2;
}
