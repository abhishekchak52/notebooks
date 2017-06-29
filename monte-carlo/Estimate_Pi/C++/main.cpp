#include "method.h"
int main(void)
{
    srand(time(NULL)); //seed the random generator
    for(double i=0;i<DATA_SIZE;i++)
        estimate_pi(SAMPLE_SIZE);
}
