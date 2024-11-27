#include <stdio.h>
#include <assert.h>
#include "file_utility.h"

void displayFileContents(const char *filename){
    FILE *file = fopen(filename, "r");
    assert(file!=NULL);

    char ch;
    while((ch = fgetc(file)) !=EOF){
        putchar(ch);
    }

    fclose(file);
}
