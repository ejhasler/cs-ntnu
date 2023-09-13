// Prøver getline() og ignore()

#include <iostream>

using namespace std;

const int max_line_length = 81;

int main() {
  char name[max_line_length];
  char address[max_line_length];
  int age;
  char position[max_line_length];

  cout << "Navn: ";
  cin.getline(name, max_line_length);
  cout << "Adresse: ";
  cin.getline(address, max_line_length);
  cout << "Alder: ";
  cin >> age;
  cin.get(); // Tar bort newline ('\n')
  cout << "Stilling: ";
  cin.getline(position, max_line_length);

  cout << name << endl << address << endl << age << endl << position << endl;
}
