#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int n,a;
    cin>>n>>a;
    for(int i=0;i<n;i++){
        string c;
        int b;
        cin>>c>>b;
        if (c=="+"){
            a+=b;
        }else if(c=="-"){
            a-=b;
        }else if(c=="*"){
            a*=b;
        }else{
            if (b==0){
                cout<<"error"<<endl;
                break;
            }else{
                a/=b;
            }
        
        }
        cout<<i+1<<":"<<a<<endl;
    }
}

