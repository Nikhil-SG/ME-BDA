#include "header.h"

int armstrongnumber(int number){
    int sum=0;
    while(number>0){
        int rem=number%10;
        sum=sum+(rem*rem*rem);
        number=number/10;
    }
    return sum;
}
