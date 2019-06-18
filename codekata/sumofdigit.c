#include <stdio.h>

    int main() {
    int a,digit;
    int sum=0;
    printf("enter the number");
    scanf("%d" ,&a);
    while(a>0)
    {
    digit=a%10;
    sum=sum+digit;
    a=a/10;
    }
    printf("sum of the digit=%d",sum);
    return 0;
    }  
