#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long
#define All(v) (v).begin(),(v).end()
int main() {
    string s,t;
    int ans=0;
    cin>>s>>t;
    rep(i,3){
        if(s[i]==t[i])ans++;
    }
    cout<<ans<<endl;
}
