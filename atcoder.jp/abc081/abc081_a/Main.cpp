#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i=0;i<n;i++)
int main() {
    string s;
    cin>>s;
    int ans=0;
    rep(i,3){
        if (s[i]=='1'){
            ans+=1;
        }
    }
    cout<<ans<<endl;
}