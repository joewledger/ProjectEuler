#include <stdio.h>
#include <stdlib.h>

int* sum_int_arrays(int* arr1, int len1, int* arr2, int len2);

int main(int argc, char** argv) 
{
    printf("Aargh\n");
}

int single_array_sum(int* n, int length)
{
    int i;
    int total = 0;
    for(i = 0; i < length; i++) {
        total += n[i];
    }
    return total;
}

int multiply_int_arrays(int* arr1, int len1, int* arr2, int len2);

//assumption: len(arr1) >= len(arr2)
int* sum_int_arrays(int* arr1, int len1, int* arr2, int len2) {
    int i, local_sum;
    int* sum_array = malloc((len1 + 1) * sizeof(int));
    int* carry_array = malloc((len1 + 1) * sizeof(int));

    for(i = len1 - 1; i >= 0; i--) {
        local_sum = 0;
        if(i < len1 - len2) {
            local_sum += arr1[i] + carry_array[i];
        } else {
            local_sum += arr1[i] + arr2[len2 - len1 + i] + carry_array[i];
        }
        sum_array[i + 1] = local_sum % 10;
        carry_array[i-1] = local_sum / 10;
    }

    sum_array[0] = carry_array[0];
    free(carry_array);
    return sum_array;
}
