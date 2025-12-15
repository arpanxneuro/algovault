#include<stdio.h>

int getSecondLargest(int *arr, int n) {
    if(n<2) return -1;
    int lg = arr[0], seclg = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] > lg) {
            seclg = lg;
            lg = arr[i];
        } else if (arr[i] > seclg && arr[i] < lg) {
            seclg = arr[i];
        }
    }
    
    return seclg;
}
