#include<stdio.h>
#include<math.h>
{
 int i,j,num,temp,sum=0;
 printf("Enter number\n");
 scanf("%d",&num);
 while(sum!=1&&sum!=4)
 {
  j=num%10;
  sum+=(j*j);
  num=num/10;
 }
 num=sum;
}
if(sum==1)
{
 printf("Happy Number\n");
}
else
{
 printf("Unhappy Number\n");
}
 
