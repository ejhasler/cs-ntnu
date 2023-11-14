#include <iostream>

using namespace std;

int find_sum(const int *table, int length) {
  int sum = 0;
  for (int i = 0; i < length; i++) {
    sum += table[i];
  }
  return sum;
}

int exercise6() {
  const int table_size = 20;
  int table[table_size];

  for (int i = 0; i < table_size; i++) {
    table[i] = i + 1;
  }

  int sum_first_10 = find_sum(table, 10);
  int sum_next_5 = find_sum(table + 10, 5);
  int sum_last_5 = find_sum(table + 15, 5);

  cout << "Sum of the first 10 numbers: " << sum_first_10 << endl;
  cout << "Sum of the next 5 numbers: " << sum_next_5 << endl;
  cout << "Sum of the last 5 numbers: " << sum_last_5 << endl;

  return 0;
}
