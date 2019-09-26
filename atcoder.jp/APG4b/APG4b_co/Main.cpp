#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int a,n,p;
    string t;
    cin>>a;
    if (a==1){
        cin>>p>>n;
        cout<<p*n<<endl;
    }else{
        cin>>t>>p>>n;
        cout<<t+"!"<<endl<<p*n<<endl;
    }
}

