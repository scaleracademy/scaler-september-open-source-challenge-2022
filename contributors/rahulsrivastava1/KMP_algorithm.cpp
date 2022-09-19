// KMP algorithm
// Time Complexity:- O(n+m)
// Space Complexity :- O(m)

// This algorithm is used to find pattern in given string

#include<bits/stdc++.h>
using namespace std;

vector<int> prefix_func(string t){
  int n=t.size();
  vector<int> pi(n,0);
  for(int i=1;i<n;i++){
    int j=pi[i-1];
    while(j>0 && t[i]!=t[j])
      j=pi[j-1];
    if(t[i]==t[j])
      j++;
    pi[i]=j;
  }
  return pi;
}

int main(){
  string s="srivastava";
  string t="vas";
  vector<int> prefix=prefix_func(t);
  int pos=-1;
  int i=0,j=0;
  while(i<s.size()){
    if(s[i]==t[j]{
      i++;
      j++;
    }else{
      if(j!=0)
        j=prefix[j-1];
      else
        i++;
    }
    if(j==t.size()){
      pos=i-t.size();
      break;
    }
  }
  cout<<pos;
}
