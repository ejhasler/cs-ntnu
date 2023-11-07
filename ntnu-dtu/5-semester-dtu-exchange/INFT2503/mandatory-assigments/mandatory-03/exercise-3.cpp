#include "Commodity.hpp"
#include <iostream>

using namespace std;

// Main function for Exercise 3.
int main() {

  cout << "\n\tExercise 3)" << endl;

  // Declare and initialize the quantity of the commodity in kilograms.
  const double quantity = 2.5;

  // Create a Commodity object named 'commodity' with a name, ID number, and unit price.
  Commodity commodity("Salma", 300, 23.50);

  // Print the name, ID number, and price per unit of the commodity.
  cout << "Product name: " << commodity.get_name() << ", product number: " << commodity.get_id()
       << " Price per unit: " << commodity.get_price() << endl;
  // Print the kilo price of the commodity, which is the same as the price per unit.
  cout << "Price per kilo: " << commodity.get_price() << endl;
  // Print the price for a specific quantity of the commodity without sales tax.
  cout << "The price for " << quantity << " kg is " << commodity.get_price(quantity)
       << " without sales tax" << endl;
  // Print the price for the same quantity of the commodity with sales tax included.
  cout << "The price for " << quantity << " kg is " << commodity.get_price_with_sales_tax(quantity)
       << " with sales tax" << endl;

  // Update the price per unit of the commodity.
  commodity.set_price(79.60);
  // Print the new kilo price of the commodity.
  cout << "New price per kilo: " << commodity.get_price() << endl;
  // Print the new price for the specified quantity of the commodity without sales tax.
  cout << "The price for " << quantity << " kg is " << commodity.get_price(quantity)
       << " without sales tax" << endl;
  // Print the new price for the same quantity of the
}
