#include "charintcheck.h"

int isCharacterOrInteger(char input){
    if(input>='0' && input <='9'){
        return 1;
    }
    else{
        return 0;
    }
}
