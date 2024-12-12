#include "header.h"

void sumNine(){
    int n;

    for(int i=10;i<=n;i++){
        int digit = n%10;
        int ans = n/10;
        if(ans+digit==9){
            printf("%d\t",i);
        }
    }
}
