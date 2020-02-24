#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int val;
    bool end;
    Node* cls[0x42];
    Node(int _v): val(_v), end(false) { memset(cls, 0, 0x42*sizeof(Node*)); }
};

signed main() {
    fstream fin("dumpdata");

    string str, addr;
    getline(fin, str);
    string KEY("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789{}_");

    Node* root(nullptr);
    map<string, Node*> mp{};
    const auto find = [&](string s, int idx = -1) {
        if (mp.find(s) == mp.end()) {
            mp[s] = new Node(idx);
            if (root == nullptr) root = mp[s];
        }
        return mp[s];
    };
    bool end;
    while (getline(fin, str) && str != "Dump end") {
        //cout << "STR" << str << endl;
        fin >> str >> addr >> end;
        auto it = find(addr);
        it->end = end;
        for(auto i = 0u; i != KEY.size(); i++) {
            fin >> str;
            it->cls[i] = find(str, i);
        }
        fin.ignore();
        fin.ignore();
        fin.ignore();
    }
    cout << mp.size() << endl;
    vector<int> st{};
    function<void(Node*)> dfs;
    dfs = [&](Node* cur) {
        //cerr << st.size() << endl;
        st.emplace_back(cur->val);
        if (cur->end) { for(auto i = 1u; i != st.size(); i++) cout << KEY[st[i]]; cout << endl; }
        for(auto i = 0u; i != KEY.size(); i++) if (cur->cls[i] != nullptr) dfs(cur->cls[i]);
        st.pop_back();
    };
    dfs(root);

}
