#include <algorithm>
#include <iostream>
#include <vector>

int main() {

  std::vector<double> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};

  std::cout << "Front element: " << numbers.front() << std::endl;
  std::cout << "Back element: " << numbers.back() << std::endl;

  numbers.emplace(numbers.begin() + 1, 1.5);
  std::cout << "New front element after emplace: " << numbers.front() << std::endl;

  double searchValue = 3.0;
  auto it = std::find(numbers.begin(), numbers.end(), searchValue);
  if (it != numbers.end()) {
    std::cout << "Value " << searchValue << " found in the vector." << std::endl;
  } else {
    std::cout << "Value " << searchValue << " not found in the vector." << std::endl;
  }

  return 0;
}
