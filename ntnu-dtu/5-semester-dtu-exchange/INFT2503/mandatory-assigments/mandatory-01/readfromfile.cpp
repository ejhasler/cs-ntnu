#include <fstream>
#include <iostream>

void read_temperatures(double temperatures[], int length);

int main() {
  const int length = 5;
  double temperatures[length];

  read_temperatures(temperatures, length);

  int count_below_10 = 0;
  int count_between_10_and_20 = 0;
  int count_above_20 = 0;

  for (int i = 0; i < length; i++) {
    if (temperatures[i] < 10) {
      count_below_10++;
    } else if (temperatures[i] <= 20) {
      count_between_10_and_20++;
    } else {
      count_above_20++;
    }
  }

  std::cout << "Antall under 10 er " << count_below_10 << std::endl;
  std::cout << "Antall mellom 10 og 20 er " << count_between_10_and_20 << std::endl;
  std::cout << "Antall over 20 er " << count_above_20 << std::endl;

  return 0;
}

void read_temperatures(double temperatures[], int length) {
  std::ifstream file("temperatures.txt");

  if (!file) {
    std::cerr << "Kunne ikke åpne filen." << std::endl;
    exit(1);
  }

  for (int i = 0; i < length; i++) {
    file >> temperatures[i];
  }

  file.close();
}
