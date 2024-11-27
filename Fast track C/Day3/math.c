#include <stdio.h>
#include <math.h>

//int main(){

int n,x,choice;

printf("enter x: ");
scanf("%d",&x);
printf("enter choice");
scanf("%d",&choice);

switch(choice){
case 1:
    if(x>=0){
            printf("%f",sqrt(x));
    }
    else{
        return 0;
    }


case 2:
    {
        if(x>0){
            return log(x);
        }
        else{
            return 0;
            }
    }

case 3:
    {
        if(x>0){
            return log10(x);
        }
        else{
            return 0;
        }
    }

case 4:
    {
        printf("enter the value of n: ");
        scanf("%d",&n);
        return pow(x,n);
    }

case 5:
    {
        return cos(x);
    }
}
return 0;
}
