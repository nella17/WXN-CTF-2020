#include <iostream>
#include <string>
using namespace std;

string first() {
    string flag("VYOz2`4x^s2");
    for(char &c: flag) c ^= 1;
    return flag;
}
string second() {
    string flag("\x0dH\x09\x08H4x\x7fK\x03\x12");
    for(char &c: flag) {
        c ^= 0x41;
        c += 0xa;
        c ^= 0x20;
    }
    return flag;
}

signed main() {
    printf("%s%s\n", first().c_str(), second().c_str());
}
