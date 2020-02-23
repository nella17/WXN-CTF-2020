#include <bits/stdc++.h>
using namespace std;

signed main() {
    string version; cin >> version;

    fstream fin(version+".txt");
    int H, W;
    fin >> H >> W; fin.ignore();
    vector<vector<int>> R(H, vector<int>{});
    vector<vector<int>> C(W, vector<int>{});
    string str;
    stringstream ss;
    int x;
    for(int i = 0; i != H; ++i) {
        getline(fin, str);
        ss.str(str); ss.clear();
        while (ss >> x) R[i].emplace_back(x);
    }
    for(int i = 0; i != W; ++i) {
        getline(fin, str);
        ss.str(str); ss.clear();
        while (ss >> x) C[i].emplace_back(x);
    }

    cout << "{\"ver\":[";
    for(int i = 0; i != H; ++i) {
        cout << "[";
        for(int j = 0; j != R[i].size(); j++) cout << R[i][j] << ",]"[j+1==R[i].size()];
        if (i+1 != H) cout << ",";
    }
    cout << "],\"hor\":[";
    for(int i = 0; i != W; ++i) {
        cout << "[";
        for(int j = 0; j != C[i].size(); j++) cout << C[i][j] << ",]"[j+1==C[i].size()];
        if (i+1 != W) cout << ",";
    }
    cout << "]}\n";

    /*
    reverse(R.begin(), R.end());
    reverse(C.begin(), C.end());
    int hH = 0, hW = 0;
    for(int i = 0; i != H; ++i) hH = max(hH, int(C[i].size()));
    for(int i = 0; i != W; ++i) hW = max(hW, int(R[i].size()));

    system(("rm "+version+".csv").c_str());
    system(("touch "+version+".csv").c_str());
    fstream fout(version+".csv");
    const char spe(','), line('\n');
    for(int i = 0; i != H+hH; ++i) for(int j = 0; j != W+hW; j++) {
        if (i < hH && j < hW) {
        } else if (i < hH) {
            if (C[j-hW].size() > hH-i-1) fout << C[j-hW][hH-i-1];
        } else if (j < hW) {
            if (R[i-hH].size() > hW-j-1) fout << R[i-hH][hW-j-1];
        }
        fout << (j+1==W+hW ? line : spe);
    }
    */

}
