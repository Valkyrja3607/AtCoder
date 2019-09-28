#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
int main() {
    int n,ans=1;
    cin>>n;
    rep(i,3){
        int a=0;
        rep(i,n){
            int tmp;
            cin>>tmp;
            a+=tmp;
        } 
        ans*=a;
    }
    
    cout<<ans<<endl;
}