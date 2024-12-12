#include <stdio.h>
#include "headr.h"


int store_num(int array[], int *size){
    for(int i=0;i<*size;i++){
        for(int j=0;j<*size){
            if(array[i] == array[j]){
                for(int k = j;k<*size-1;k++){
                    array[k] = arr[k+1];
                }
                (*size)--;
            }else{
                j++;
            }
        }
    }
}
