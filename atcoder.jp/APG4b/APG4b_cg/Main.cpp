#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
int main() {
    int ans=0,tmp=12345;
    rep(i,5){
        int n;
        cin>>n;
        if (n==tmp){
            ans+=1;
        }
        tmp=n;
    }
    if (ans>0){
        cout<<"YES"<<endl;
    }else{
        cout<<"NO"<<endl;
    }
}

