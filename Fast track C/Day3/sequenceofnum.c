#include "header.h"

int sequence(num){
    int num1=0,num2=0,num3=1,i,sum;
    printf("%d\t%d\t%d\t",num1,num2,num3);
    for(i=1;i<=num;i++){
        sum=num1+num2+num3;
        num1=num2;
        num2=num3;
        num3=sum;
        printf("%d\t",sum);
    }
    return 0;
}
