#include <stdio.h>
#include "header.h"
#include "assert.h"

int main(){
    int num1 = 5;
    int num2 = 10;
    int result = swap(num1,num2);
    assert(result == 10,5);
    return 0;
}
