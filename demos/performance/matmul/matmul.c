#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <math.h>

double mytime(void);

int dgemm_(char *transa, char *transb, int *m, int * n,
           int *k, double *alpha, double *a, int *lda,
           double *b, int *ldb, double *beta,
           double *c, int *ldc);


int main(int argc, char **argv)
{

  int ind_ij, ind_ik, ind_kj; // linearized indeces
  double *a, *b, *c;
  double t_on, t_off;

  int n = 1000;
  if (argc >= 2) {
    n = atoi(argv[1]);
  }

  a = (double* ) malloc(n * n * sizeof(double));
  b = (double* ) malloc(n * n * sizeof(double));

  /*Create random matrix */
  int jj = 0;
  srand(5);
  for (int i=0; i < n; i++) {
    for (int j=0; j < n; j++) {
      a[jj] = (double)(rand()/(double)RAND_MAX);
      b[jj] = (double)(rand()/(double)RAND_MAX);
      jj++;
    }
  }

  c = (double* ) malloc(n * n * sizeof(double));


// Triple loop
  t_on = mytime();
  for (int i=0; i < n; i++)
    for (int j=0; j < n; j++)
       {
          ind_ij = i + j*n;
          c[ind_ij] = 0.0;
          for (int k=0; k < n; k++)
            {
              ind_ik = i + k*n;
              ind_kj = k + j*n;
              c[ind_ij] += a[ind_ik] * b[ind_kj];
            }
       }
  t_off = mytime();
  printf("Time with triple loop %-6.3f s \n", t_off - t_on);


// BLAS call
  int lda = n;
  double alpha = 1.0;
  double beta = 0.0;

  t_on = mytime();
  for (int i=0; i < 10; i++)
     dgemm_("t", "t", &n, &n, &n, &alpha, a, &lda, b, &lda, &beta, c, &lda);
  t_off = mytime();

  printf("Time with dgemm       %-6.3f s \n", (t_off - t_on)/10);

}

double mytime(void)
{
  struct timeval t;
  gettimeofday(&t, (struct timezone *)NULL);
  return (double)t.tv_sec + t.tv_usec*0.000001;
}

