#include<fstream>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<cstdio>
#include<cstring>
using namespace std;


const int SIZE = 1;
const double SAMPLE_SIZE = 1e3;
const int NUM_DIGITS = log10(SAMPLE_SIZE);
const double DATA_SIZE = 1e5;

double rand_sample();
bool check_inside(double x,double y);
void estimate_pi(double SAMPLE_SIZE);
void out_to_file(double PI);
