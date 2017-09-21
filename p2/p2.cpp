
#include <iostream>
using namespace std;

int main() {
	
	int e=0,o=1,r = e + 2*o,sum=0;
	
	while(r<=4000000)
	{
		sum+=r;
		e=r;
		o=2*e-o;
		r=e+2*o;
		
	}

cout<<sum;
	return 0;
}