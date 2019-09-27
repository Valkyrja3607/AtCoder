#include <bits/stdc++.h>
using namespace std;
 
int main() {
    string s;
    cin>>s;
    int ans=1;
    int n=s.size();
    int i=1;
    while (i<n){
        if (s.at(i)=='+'){
            i++;
            ans+=1;
        }else if (s.at(i)=='-'){
            i++;
            ans-=1;
        }
        i++;
    }
    cout<<ans<<endl;
}

