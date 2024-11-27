#include "header.h"

int palindrome(int number){
    int rev;
    while(number>0){
        int digit=number%10;
        rev=rev*10+digit;
        number=number/10;
    }
    return rev;
}
