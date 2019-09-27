import subprocess as sp
import sys
 
code = r"""
#include<bits/stdc++.h>
using namespace std;
const int mod=1e9+7;
int add(int x,int y){return(x+=y)<mod?x:x-mod;}
int sub(int x,int y){return(x-=y)>= 0?x:x+mod;}
int dp[1<<21];
int n,a[21][21];
int main(){
  scanf("%d",&n);
  for(int i=0;i<n;++i){
    for(int j=0;j<n;++j){
      scanf("%d",&a[i][j]);
    }
  }
  dp[0]=1;
  for(int b=1;b<(1<<n);++b){
    int bc=__builtin_popcount(b)-1;
    for(int i=0;i<n;++i){
      if((b>>i&1)&&a[bc][i]){
        dp[b]=add(dp[b],dp[b^(1<<i)]);
      }
    }
  }
  printf("%d\n",dp[(1<<n)-1]);
}
"""
 
with open("A.cpp","w") as f:
	f.write(code)
    
sp.Popen(['g++','-std=c++11','-O2',"A.cpp"]).communicate()
sp.Popen(['./a.out'],stdin=sys.stdin,stdout=sys.stdout).communicate()
