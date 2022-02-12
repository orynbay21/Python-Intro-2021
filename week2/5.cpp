#include <iostream>
using namespace std;
int main()
{
    int x,y;
    cin>>x>>y;
    int sum=x+y;
    int first_function=y^sum;
    int second_function=x^first_function;
    cout<<second_function;

}