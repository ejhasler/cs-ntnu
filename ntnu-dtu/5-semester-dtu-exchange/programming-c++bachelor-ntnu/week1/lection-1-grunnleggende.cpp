// include referer til bibloteker
#include <iostream> // innlesing/utskrift

using namespace std; // bruker standard navnerom, se cout nedenfor

int main() {
    int a;
    int b[3]; // en heltallstabell med 3 elementer
    double c;
    cout << "a = " << a << ", c = " << c << endl; // kan skrive std::cout
    for (int i = 0; i < 5; i++) {
        cout << "i = " << i << " tabellelement: " << b[i] << endl;
    }
    return 0; // pga at main() er av typen int, kan sløyfes
}