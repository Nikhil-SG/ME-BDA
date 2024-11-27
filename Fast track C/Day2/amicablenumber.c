#include "header.h"

int amicablenumber(num1,num2){
    int sum1=0,sum2=0,i,j;
    for(i=1;i<=num1/2;i++){
        int rem1=num1%i;
        if(rem1==0){
            sum1=sum1+i;
        }
    }
    for(j=1;j<=num2/2;j++){
        int rem2=num2%j;
        if(rem2==0){
            sum2=sum2+j;
        }
    }
    //printf("%d %d\n",sum1,sum2);
    if(sum1==num2 && sum2==num1){
        printf("%d and %d are amicable numbers \n",num1,num2);
        return 1;
    }
    else{
        printf("%d and %d are not amicable numbers \n",num1,num2);
        return 0;
    }
}
