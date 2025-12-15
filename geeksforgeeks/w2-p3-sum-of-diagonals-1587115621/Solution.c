#include<stdio.h>

int sumDiagonal(int N, int M[][N]) {
    // your code here
    int sum = 0;
    for(int i=0; i<N; i++) {
        sum += M[i][i];
    }
    
    return sum;
}