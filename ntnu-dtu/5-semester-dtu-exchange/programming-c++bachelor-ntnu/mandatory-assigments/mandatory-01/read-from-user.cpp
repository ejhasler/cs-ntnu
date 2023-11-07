#include <iostream>

int main() {
    const int length = 5;
    double temperatures[length];
    int count_below_10 = 0;
    int count_between_10_and_20 = 0;
    int count_above_20 = 0;

    std::cout << "Du skal skrive inn 5 temperaturer." << std::endl;

    for (int i = 0; i < length; i++) {
        std::cout << "Temperatur nr " << i + 1 << ": ";
        std::cin >> temperatures[i];

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
