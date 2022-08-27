#include <stdio.h>

int sumOfSeriesInvoicing()
{
    int n;
    float a1, d;
    printf("Please type the number of the length of the series: ");
    scanf("%d", &n);
    printf("Please type the first number  in the series: ");
    scanf("%f", &a1);
    printf("Please type the jump (number) between the numbers in the series: ");
    scanf("%f", &d);

    printf("The sum of this series is: %f  :)", (n * (2 * a1 + (n - 1) * d)) / 2.0);
    return 0;
}



int main() {
    sumOfSeriesInvoicing();
    return 0;
}
