#include <stdbool.h>

// User function template for C
bool isPalindrome(char s[]) {
    int left = 0;
    int right;
    while(s[left] != '\0') left++;
    right = left-1;
    for(int i=0; i<left/2; i++) {
        if(s[i] != s[right-i]) {
            return false;
        }
    }
    return true;
}