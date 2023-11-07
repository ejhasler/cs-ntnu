#pragma once
#include <string>

using namespace std;

const double tax = 25;

class Commodity {
public:
  Commodity(string name_, int id_, double price_);

  string get_name();
  int get_id();
  double get_price();
  double get_price(double quantity);
  double get_price_with_sales_tax();
  double get_price_with_sales_tax(double quantity);
  void set_price(double price);

private:
  string name;
  int id;
  double price;
};
