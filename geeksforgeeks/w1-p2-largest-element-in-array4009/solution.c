#include<stdio.h>

int largest(int arr[], int n) {
    if(n==0) return -1;
    int max = arr[0];
    for(int i=1; i<n; i++) {
        if(arr[i]>max) {
            max = arr[i];
        }
    }
    return max;
}