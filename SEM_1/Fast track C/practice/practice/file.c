#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *file;
    file = fopen("output.txt","w");
    if (file==NULL){
        printf("file does not exist\n");
        return 1;
    }

    char data[]="ertgretg\n dslkfjsldfghjl";
    fprintf(file,"%s", data);
    fclose(file);

    file=fopen("output.txt","r");

    char str[100];
    while(!feof(file)){
        fgets(str,99,file);
        printf(str);
    }
    return 0;
}
