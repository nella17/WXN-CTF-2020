#include <iostream>
#include <string>
using namespace std;

class tnode {
public:
    tnode* cls[0x42];
    tnode() {
        for(int i = 0; i < 0x42; ++i) cls[i] = nullptr;
    }
} *root;

void insert(string str) {
}
bool search(string str) {
    return str.size() > 1;
}
void dump() {
}

signed main() {
    root = new tnode();
    int x;
    string str;
    while (true) {
        cin >> x;
        switch (x) {
        case 1:
            cin >> str;
            insert(str);
            break;
        case 2:
            cin >> str;
            cout << (search(str) ? "Success!!" : "Fail") << endl;
            break;
        case 3:
            cout << "Dump data" << endl;
            dump();
            cout << "Dump end" << endl;
            break;
        default:
            cout << "Error" << endl;
            break;
        }
    }
}
