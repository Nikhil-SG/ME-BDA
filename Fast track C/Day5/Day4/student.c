#include <stdio.h>

// Define a structure for a student
struct Student {
    int rollNo;
    char name[50];
    int age;
    float marks;
};

int main() {
    // Declare an array of structures to store information for 10 students
    struct Student students[1];

    // Input information for 10 students
    for (int i = 0; i < 1; i++) {
        printf("Enter details for Student %d:\n", i + 1);
        printf("Roll No.: ");
        scanf("%d", &students[i].rollNo);
        printf("Name: ");
        scanf("%s", students[i].name); // Note: Using %s for name input
        printf("Age: ");
        scanf("%d", &students[i].age);
        printf("Marks: ");
        scanf("%f", &students[i].marks);
    }

    // Display information for all 10 students
    printf("\nStudent Information:\n");
    for (int i = 0; i < 1; i++) {
        printf("Student %d\n", i + 1);
        printf("Roll No.: %d\n", students[i].rollNo);
        printf("Name: %s\n", students[i].name);
        printf("Age: %d\n", students[i].age);
        printf("Marks: %.2f\n", students[i].marks);
        printf("\n");
    }

    return 0;
}
