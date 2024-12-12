#include "header.h"

int sumofdigits(int number) {
    int sum = 0;
    while (number > 0) {
        sum = sum+number % 10;
        number = number/10;
    }
    return sum;
}
