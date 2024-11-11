#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n, int &intercambios) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                intercambios++;
            }
        }
    }
}

int main() {
    int tiempos[] = {125, 90, 150, 105, 80};
    int n = sizeof(tiempos) / sizeof(tiempos[0]);
    int intercambios = 0;

    bubbleSort(tiempos, n, intercambios);

    cout << "Tiempos de ordenados en orden ascendente: ";
    for (int i = 0; i < n; i++) {
        cout << tiempos[i] << " ";
    }
    cout << endl;

    cout << "Total de intercambios: " << intercambios << endl;

    return 0;
}

