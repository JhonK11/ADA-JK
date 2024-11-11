#include <iostream>
using namespace std;

void selectionSort(int arr[], int n) {
    int comparaciones = 0;

    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            comparaciones++;
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        if (minIndex != 1) {
            swap(arr[i], arr[minIndex]);
        }
    }

    cout << "Total de Comparaciones: " << comparaciones << endl;
}

int main() {
    int usuarios[] = {580, 320, 760, 435, 520};
    int n = sizeof(usuarios) / sizeof(usuarios[0]);

    selectionSort(usuarios, n);

    cout << "Usuarios ordenados de forma ascendente: ";
    for (int i = 0; i < n; i++) {
        cout << usuarios[i] << " ";
    }
    cout << endl;

    return 0;
}