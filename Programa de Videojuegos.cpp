#include <iostream>
#include <fstream>
#include <string>
#include <ctime>
#include <cstdlib>

using namespace std;

struct Player {
    int id;
    string name;
    int score;
    Player* next;
};

Player* createNode(int id, string name, int score) {
    Player* newNode = new Player{id, name, score, nullptr};
    return newNode;
}

void appendNode(Player*& head, int id, string name, int score) {
    Player* newNode = createNode(id, name, score);
    if (head == nullptr) {
        head = newNode;
        return;
    }
    Player* temp = head;
    while (temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = newNode;
}

double calculateAverage(Player* head) {
    if (head == nullptr) return 0;
    double sum = 0;
    int count = 0;
    Player* temp = head;
    while (temp != nullptr) {
        sum += temp->score;
        count++;
        temp = temp->next;
    }
    return sum / count;
}

Player* findHighestScore(Player* head) {
    if (head == nullptr) return nullptr;
    Player* highest = head;
    Player* temp = head->next;
    while (temp != nullptr) {
        if (temp->score > highest->score) {
            highest = temp;
        }
        temp = temp->next;
    }
    return highest;
}

Player* findLowestScore(Player* head) {
    if (head == nullptr) return nullptr;
    Player* lowest = head;
    Player* temp = head->next;
    while (temp != nullptr) {
        if (temp->score < lowest->score) {
            lowest = temp;
        }
        temp = temp->next;
    }
    return lowest;
}

void removeBelowAverage(Player*& head, double average) {
    Player* temp = head;
    Player* prev = nullptr;
    while (temp != nullptr) {
        if (temp->score < average) {
            if (prev != nullptr) {
                prev->next = temp->next;
            } else {
                head = temp->next;
            }
            delete temp;
            temp = prev ? prev->next : head;
        } else {
            prev = temp;
            temp = temp->next;
        }
    }
}

void freeList(Player*& head) {
    while (head != nullptr) {
        Player* temp = head;
        head = head->next;
        delete temp;
    }
}

int main() {
    Player* head = nullptr;
    ifstream inputFile("C:\\Users\\ASUS TUF GAMING\\Documents\\TRABAJOS\\Apuntes\\jugadores.txt");
    if (!inputFile) {
        cerr << "Error al abrir el archivo." << endl;
        return 1;
    }

    string line;
    while (getline(inputFile, line)) {
        size_t firstSpace = line.find('\t');
        size_t lastSpace = line.rfind('\t');

        if (firstSpace == string::npos || lastSpace == string::npos || firstSpace == lastSpace) {
            cerr << "Línea inválida: " << line << endl;
            continue;
        }

        int id = stoi(line.substr(0, firstSpace));
        string name = line.substr(firstSpace + 1, lastSpace - firstSpace - 1);
        int score = stoi(line.substr(lastSpace + 1));

        appendNode(head, id, name, score);
    }
    inputFile.close();

    double average = calculateAverage(head);
    cout << "Puntuacion Promedio: " << average << endl;

    Player* highest = findHighestScore(head);
    Player* lowest = findLowestScore(head);

    if (highest) {
        cout << "Mayor Puntuacion: PlayerID=" << highest->id << ", PlayerName=" << highest->name
             << ", Score=" << highest->score << endl;
    }
    if (lowest) {
        cout << "Menor Puntuacion: PlayerID=" << lowest->id << ", PlayerName=" << lowest->name
             << ", Score=" << lowest->score << endl;
    }

    clock_t start = clock();
    removeBelowAverage(head, average);
    clock_t end = clock();

    double elapsed = double(end - start) / CLOCKS_PER_SEC;
    cout << "Tiempo para eliminar jugadores por debajo del promedio: " << elapsed << " segundos" << endl;

    freeList(head);

    return 0;
}
