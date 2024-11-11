#include <iostream>
using namespace std;

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int clics[] = {250, 120, 300, 95, 210};
    int n = sizeof(clics) / sizeof(clics[0]);

    insertionSort(clics, n);

    cout << "Clics en orden ascendente: ";
    for (int i = 0; i < n; i++) {
        cout << clics[i] << " ";
    }
    cout << endl;

    cout << "Anuncio con mayor cantidad de clics: " << clics[n - 1] << endl;

    return 0;
}