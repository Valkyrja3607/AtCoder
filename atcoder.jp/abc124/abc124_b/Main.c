#include<stdio.h>
int main(){
  int n;
  int h;
  int p;
  int ans;
  ans=0;
  p=0;
  scanf("%d",&n);
  int i=0;
  for(i=0;i<n;i++){
    scanf("%d",&h);
    if (p<=h){
      ans+=1;
      p=h;
    }
  }
  printf("%d\n",ans);
}
  
