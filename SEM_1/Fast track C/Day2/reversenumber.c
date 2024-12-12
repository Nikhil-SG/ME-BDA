#include "header.h"

int reversenumber(int number){
    while(number>0){
        int digit=number%10;
        printf("%d",digit);
        number=number/10;
    }
}
