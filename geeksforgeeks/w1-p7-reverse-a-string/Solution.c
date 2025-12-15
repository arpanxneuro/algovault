#include<stdio.h>

// User function Template for C
char* reverseString(char* s) {
    int len = 0;
    static char rev[1000001];
    while(s[len] != '\0') len++;
    
    for(int i = 0; i < len; i++) {
        rev[i] = s[len-1-i];
    }
    rev[len] = '\0';
    
    return rev;
}