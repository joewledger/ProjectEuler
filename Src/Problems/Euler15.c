#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>

int main(int argc, char** argv)
{

    int size = atoi(argv[1]) + 1;
    int i,j;

    int64_t **matrix;
    matrix = malloc(size * sizeof(int64_t *));
    for(i = 0; i < size; i++) {
        matrix[i] = malloc(size * sizeof(int64_t));
    }

    for(i = 0; i < size; i++){
        matrix[i][size - 1] = 1LL;
        matrix[size - 1][i] = 1LL;
    }

    for(i = size - 1; i--; i >= 0) {
        for(j = size - 1; j--; j >= 0) {
            matrix[i][j] = matrix[i+1][j] + matrix[i][j+1];
            if(matrix[i][j] < 0) {
                printf("Oops");
            }
        }
    }
    
    printf("%" PRId64 "\n", matrix[0][0]);

    for(i = 0; i < size; i++) {
        free(matrix[i]);
    }
    free(matrix);
}
