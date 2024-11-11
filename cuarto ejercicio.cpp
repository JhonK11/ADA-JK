#include <iostream>
using namespace std;

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return (i + 1);
}

void quicksort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quicksort(arr, low, pi - 1);
        quicksort(arr, pi + 1, high);
    }
}

int main() {
    int archivos[] = {850, 230, 690, 540, 310};
    int n = sizeof(archivos) / sizeof(archivos[0]);

    quicksort(archivos, 0, n - 1);

    cout << "Tamaño de archivos en orden ascendente: ";
    for (int i = 0; i < n; i++) {
        cout << archivos[i] << " ";
    }
    cout << endl;

    return 0;
}