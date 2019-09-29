#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long
#define All(v) (v).begin(),(v).end()
int main(){
    int n,ans=0;
    cin>>n;
    rep(i,n){
        int l,r;
        cin>>l>>r;
        ans+=r-l+1;
    }
    cout<<ans<<endl;
}
