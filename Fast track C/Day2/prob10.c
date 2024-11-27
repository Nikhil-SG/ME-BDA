/*#include <stdio.h>
#include <stdlib.h>
#define PI 3.14

int main(){
    int edge,length,breadth,height,radius;
    int choice;
    printf("Select volume of\n 1.Cube\n 2.Cuboid\n 3.Sphere\n 4.Cylinder\n 5.Cone\n");
    scanf("%d",&choice);
    switch(choice){
        case 1:
            printf("enter edge of cube:\n");
            scanf("%d",&edge);
            return edge*edge*edge;
            break;

        case 2:
            printf("enter length, breadth, height of cuboid:\n");
            scanf("%d",&length);
            scanf("%d",&breadth);
            scanf("%d",&height);
            return length*breadth*height;
            break;

        case 3:
            printf("enter radius of sphere:\n");
            scanf("%d",&radius);
            return (4/3)*PI*radius*radius*radius;
            break;

        case 4:
            printf("enter radius, height of cylinder:\n");
            scanf("%d",&radius);
            scanf("%d",&height);
            return PI*radius*radius*height;
            break;

        case 5:
            printf("enter radius and height of Cone:\n");
            scanf("%d",&radius);
            scanf("%d",&height);
            return PI*radius*radius*(height/3);
            break;

        default:
            printf("Enter valid option\n");
            break;
    }
}*/
