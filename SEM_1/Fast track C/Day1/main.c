#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "header.h"

/*int main(){
    char uppercasechar='A';
    char convertedchar=caseconvert(uppercasechar);

    //using assert to verify that the conversion is correct
    assert(convertedchar=='a');
    assert(convertedchar=='b');

    printf("uppercase: %c\n lowercase:%c\n", uppercasechar, convertedchar);
    return 0;


}*/

/*
int main(){
    double r=5.0;
    double area=areaofcircle(r);
    assert(area==78);

    printf("Radius:%.2f\nArea:%.2f\n",r,area);
    return 0;
}
*/

/*
int main(){
    double temperature=35;
    double f=ctof(temperature);
    assert(f==95.00);

    printf("farhenhiet:%.2f\n Celcius:%.2f",f,temperature);
}
*/

/*
int main(){
    int num;
    printf("enter a number\n");
    scanf("%d",&num);
    int result=evenodd(num);

    assert(result==1 || result==0);
    if (result==1){
        printf("%d is even number\n",num);
    }
    else{
        printf("%d is odd number\n",num);
    }
    return 0;
}
*/

/*
int main(){
    int num1=rand();
    int num2=rand();
    int sum=calculatesum(num1,num2);
    printf("number1:%d\n number2:%d\n Sum:%d\n",num1,num2,sum);
    return 0;
}
*/

/*
int main(){
    char input;
    printf("enter a character or an integer (0-9): ");
    scanf("%c",&input);
    int result=isCharacterOrInteger(input);
    assert(result==1||result==0);
    if(result==1){
        printf("%c is an integer within range 0-9.\n",input);
    }
    else{
        printf("%c is a character.\n",input);
    }
    return 0;
}
*/

/*
int main(){
    int n=10;
    //printf("enter n: \n");
    //scanf("%d",&n);
    sumofthree(n);
    return 0;
}
*/

int main(){
    int num;
    printf("enter a number: \n");
    scanf("%d",&num);
    int result = sumofdigits(n);
    return 0;
}




