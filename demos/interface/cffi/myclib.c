void add(double *a, double *b, int n)
{
  int i;
  for (i=0; i<n; i++)
     a[i] += b[i];
}

void subtract(double *a, double *b, int n)
{
  int i;
  for (i=0; i<n; i++)
     a[i] -= b[i];
}

