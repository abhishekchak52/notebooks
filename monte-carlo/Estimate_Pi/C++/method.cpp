#include "method.h"

//------------rand_sample()---------------------//
double rand_sample()
{
    return double(rand())/RAND_MAX;
}
//------------check_inside()--------------------//
bool check_inside(double x,double y)
{
    return (sqrt((x*x)+(y*y))<1);
}
//------------estimate_pi()---------------------//
void estimate_pi(double SAMPLE_SIZE)
{
    int count = 0;
    for(int i = 0;i<SAMPLE_SIZE;i++)
    {
    //pick a random point
       double pos_x = rand_sample();
      // cout<<pos_x<<endl;
       double pos_y = rand_sample();
    //   cout<<pos_y<<endl;
    //check if its inside the quadrant
        if(check_inside(pos_x,pos_y))
           count++;
    }
    //calculate pi
        out_to_file(4*double(count)/SAMPLE_SIZE);
}
//--------------out_to_file()-------------------//
void out_to_file(double PI)
{   //preparing the filename
    char* filename = new char[strlen("pi_value")+int(NUM_DIGITS)+10];
    sprintf(filename,"../outputs/%s1e%d","pi_",int(NUM_DIGITS));
    filename = strcat(filename,".txt");
    //opening the file
    ofstream fout;
    fout.open(filename,ios::app);
    fout<<PI<<endl;
    fout.close();
    delete filename;
}

