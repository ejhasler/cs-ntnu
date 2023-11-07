#include "Commodity.hpp"
#include <string>

string Commodity::get_name() {
  return name;
}

int Commodity::get_id() {
  return id;
}

double Commodity::get_price() {
  return price;
}

double Commodity::get_price_with_sales_tax() {
  return price * (1 + tax / 100);
}

double Commodity::get_price(double quantity) {
  return price * quantity;
}

double Commodity::get_price_with_sales_tax(double quantity) {
  return price * (1 + tax / 100) * quantity;
}

void Commodity::set_price(double price) {
  this->price = price;
}

Commodity::Commodity(string name_, int id_, double price_) : name(name_), id(id_), price(price_){};
