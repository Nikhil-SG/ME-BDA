#include <stdio.h>
#include <ctype.h>

void convertTolowercase(char *str){
    for(int i = 0; str[i]!='\0';i++){
        if(islower(str[i])){
            str[i] = toupper(str[i]);
        }
    }
}

/*
int main(){
    char inputString[100];
    printf("enter a string: \n");
    fgets(inputString, sizeof(inputString), stdin);
    convertTolowercase(inputString);
    printf("uppercase is: %s\n",inputString);
}
*/
