#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "header.h"

/*Q1
int main()
{
    int number;
    printf("enter the number: \n");
    scanf(" %d",&number);
    int result = sumofdigits(number);
    printf("sum = %d\n",result);
    assert(result==3);
    return 0;
}
*/

/*Q2
int main(){
    int number=12345678901;
    int result = reversenumber(number);
    return 0;
}
*/

/*Q3
int main(){
    int number,digit;
    printf("enter the number: \n");
    scanf("%d",&number);
    printf("enter the digit to count: ");
    scanf("%d",&digit);
    int result = countdigit(number,digit);
    assert(result == 2);
    return 0;
}
*/

/*Q5
int main(){
    int number;
    printf("enter a number: \n");
    scanf("%d",&number);
    int result=palindrome(number);
    assert(number==result);
    return 0;
}
*/

/*Q6
int main(){
    int n;
    printf("enter number of prime numbers to find: \n");
    scanf("%d",&n);
    int result = prime(n);
    result 0;
}
*/

/*Q7
int main(){
    int number;
    printf("enter the number: \n");
    scanf("%d",&number);
    int result=armstrongnumber(number);
    printf("%d",result);
    assert(result==number);
    return 0;
}
*/


int main(){
    int num1,num2;
//    int num1=220,num2=284;
    printf("enter num1: \n");
    scanf("%d",&num1);
    printf("enter num2: \n");
    scanf("%d",&num2);
    int result = amicablenumber(num1,num2);
    assert(result==1);
    return 0;
}








