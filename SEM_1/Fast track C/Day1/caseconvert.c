#include "caseconvert.h"

char caseconvert(char c) {
    if (c >= 'A' && c <= 'Z') {
        // Convert uppercase to lowercase by adding 32 (difference between uppercase and lowercase characters in ASCII)
        return c + 32;
    }
    return c; // Return the character unchanged if it's not an uppercase character
}
