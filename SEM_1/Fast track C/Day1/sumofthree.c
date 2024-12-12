#include "header.h"

int sumofthree(n){
    int a=0;
    int b=0;
    int c=1;
    printf("%d %d %d\t",a,b,c);
    int i=0;
    while(i>=10)
    {
        int sum=0;
        sum=a+b+c;
        printf("%d\t",sum);
        a=b;
        b=c;
        c=sum;
    }
}
