#include <stdio.h>

void transpose(int **mat, int **tMat, int n) {
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            tMat[j][i] = mat[i][j];
        }
    }

    return tMat;
}
