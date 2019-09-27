#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
int main() {
    int a,b,c;
    cin>>a>>b>>c;
    vector<int> l={a,b,c};
    sort(l.begin(),l.end());
    cout<<l.at(2)-l.at(0)<<endl;
}

