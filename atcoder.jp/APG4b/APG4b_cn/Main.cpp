#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int x,a,b,tmp;
    cin>>x>>a>>b;
    tmp=x+1;
    cout<<tmp<<endl;
    tmp*=(a+b);
    cout<<tmp<<endl;
    tmp*=tmp;
    cout<<tmp<<endl;
    tmp-=1;
    cout<<tmp<<endl;
}

