#include "header.h"

int countdigit(int number,int digit){
    int count;
    while(number>0){
            int n=number%10;
        if(n==digit){
            count++;
        }
        number=number/10;
    }
    return count;
}
