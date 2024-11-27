#include <stdio.h>
/*
int main(){
    int day,month,year;

    printf("enter the day(1-31): \n");
    scanf("%d",&day);

    printf("enter the month(1-12): \n");
    scanf("%d",&month);

    printf("enter the year: \n");
    scanf("%d",&year);

    if(day<1||day>31||month<1||month>12||year<0){
        printf("Invalid date, month, or year entered. \n");
        return 1;
    }

    printf("Worded format: ");
    switch(day){
    case 1:
    case 21:
    case 31:
        printf("%dst ",day);
        break;

    case 2:
    case 22:
        printf("%dnd ",day);
        break;

    case 3:
    case 33:
        printf("%drd ",day);
        break;

    default:
        printf("%dth ",day);
        break;
    }

    switch(month){
        case 1:
            printf("January");
            break;
        case 2:
            printf("February");
            break;
        case 3:
            printf("March");
            break;
        case 4:
            printf("April");
            break;
        case 5:
            printf("May");
            break;
        case 6:
            printf("June");
            break;
        case 7:
            printf("July");
            break;
        case 8:
            printf("August");
            break;
        case 9:
            printf("September");
            break;
        case 10:
            printf("October");
            break;
        case 11:
            printf("November");
            break;
        case 12:
            printf("December");
            break;
        default:
            printf("Invalid month");
            break;
    }

    printf(",%d\n",year);

    return 0;
}
*/
