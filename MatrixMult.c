#include<stdio.h>
#include <time.h>
#include<string.h> 
#include<stdlib.h>

long a[5000][5000],b[5000][5000],p[5000][5000];
int main(int num,char *args[])
{
	int n1=atoi(args[1]);
	long n=n1;

	clock_t start, end;
	double t;
 	 	
	for(long i=0;i<n;i++)
	{
		for(long j=0;j<n;j++)
		{
			a[i][j]=i+j;
		}
	}
			
	for(long i=0;i<n;i++)
	{
		for(long j=0;j<n;j++)
		{
			b[i][j]=i+(2*j);
		}
	}
	start = clock();		

	long c,d,k,sum=0;
	for(c=0;c<n;c++){
		for(d=0;d<n;d++)
		{
			for(k=0;k<n;k++)
			{
				sum=sum+a[c][k]*b[k][d];
			}
			p[c][d]=sum;
			sum=0;
		}
	}
	
	 end = clock();
	t =(double) (end - start) / CLOCKS_PER_SEC;
 
 	printf("%f",t);
	return 0;
	
}
	
	
	
	
	
	
	
	
	
	
	
	
	
