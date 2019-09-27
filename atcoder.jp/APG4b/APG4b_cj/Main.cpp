#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int n;
    int ans=0;
    vector<int> l;
    cin>>n;
    for (int i=0;i<n;i++){
        int tmp;
        cin>>tmp;
        ans+=tmp;
        l.push_back(tmp);
    }
    for (int i=0;i<n;i++){
        cout<<abs(ans/n-l.at(i))<<endl;
    }
    
}

