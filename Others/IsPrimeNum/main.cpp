#include <iostream>
#include <stdbool.h>
#include <math.h>


bool IsPrimeNum(int num)
{
    int sqrtNum = sqrt(num) + 1;
    for (int i = 2; i < sqrtNum; i++)
        if (num % i == 0)
            return false;
    return true;
}



int main() {
//    bool answer = IsPrimeNum(832175063); - False
//    bool answer = IsPrimeNum(832175081); - True
    bool answer = IsPrimeNum(832175093);
//    printf("%i \n", answer); - True
    return 0;
}
