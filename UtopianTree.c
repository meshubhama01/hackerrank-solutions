#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){

    int t,a; 
    scanf("%d",&t);
    for(a= 1; a <= t; a++){
        int n; 
        scanf("%d",&n);
   int h,c;
          h=1;
    for(c=1;c<=n;c++){
      
        if(c%2==0) { h=h+1;}
        else   {h=h*2;}
    }
     printf("%d\n",h); }
    
    return 0;
}
          
