#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i=0;i<n;i++)
int main() {
    int n,ans=1000000000;
    cin>>n;
    rep(i,n){
        int a,tmp=0;
        cin>>a;
        while(a%2==0){
            a=a/2;
            tmp+=1;
        }
        ans=min(ans,tmp);
    }
    cout<<ans<<endl;
}