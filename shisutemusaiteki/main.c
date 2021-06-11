// 問２
#include <stdio.h>
#include <stdlib.h>
#include "mpi.h"
#include <math.h>

int main(int argc, char **argv){

  int i, j;
  int P, rank, a;
  int *t, *s, *tmp;
  MPI_Status st;

  MPI_INIT(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &P);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  t= (int *) malloc(sizeof (int) * 4);
  s= (int *) malloc(sizeof (int) * 4);
  tmp= (int *) malloc(sizeof (int) * 4);
  a = log2(P);

  for (i=0; i<4; i++){
    t[i]=rank;
  }

  for (i=0; i<4; i++){
    s[i]=0;
  }

  for (i=1; i<=P; i*2){
      MPI_Sendrecv(&t, 4, MPI_INT, (rank+i)%P, 0, &tmp, 4, MPI_INT,(rank+P-i)%P, 0, MPI_COMM_WORLD, &st);
      for (j=0; j<4; j++){
          s[j] += tmp[j];
      }
  }

  free(t);
  free(s);
  free(tmp);

  return 0;
}




// 問３
#define nx 1000000
int main(void){
  int it,i;
  double u[nx],un[nx];

  for (i=0; i<nx; i++){u[i]=0.0;}
    u[0]=0.5;
    u[nx-1]=1.0;
  for (it=0; it<1000; it++){
    #pragma opm for 
    for (i=1; i<nx-1; i++){
      un[i]=u[i]*2.0-u[i+1]-u[i-1];
    }
    #pragma omp for 
    for (i=1; i<nx-1; i++){
      u[i]=un[i];
    }
  }
  return 0;
} 


