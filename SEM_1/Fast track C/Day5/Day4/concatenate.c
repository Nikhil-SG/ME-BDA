#include <stdio.h>

void concatenateStrings(const char *str1, const char *str2, char *result){
    int i=0,j=0;

    while(str1[i] != '\0'){
        result[j++] = str1[i++];
    }

    i=0;
    while(str2[i] != '\0'){
        result[j++] = str2[i++];
    }

    result[j] = '\0';
}
/*
int main(){
    char str1[100],str2[100], result[200];
    printf("enter first string: ");
    scanf("%s", str1);

    printf("enter second string: ");
    scanf("%s", str2);

    concatenateStrings(str1, str2, result);
    printf("concatenated string: %s\n", result);

    return 0;
}
*/

