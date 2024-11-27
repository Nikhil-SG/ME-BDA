#include <stdio.h>

int swap(num1,num2){
    int temp = num1;
    num1 = num2;
    num2 = temp;
    return num1, num2;
}
