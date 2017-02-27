#include <string.h>

void evolve(double *u, double *u_previous, int nx, int ny, 
            double a, double dt, double dx2, double dy2)
{
  int i, j;
  int ij, ip, im, jp, jm;

  for (i=1; i < nx-1; i++)
    for (j=1; j < ny-1; j++) {
      // Linearisation for 2D array
      ij = j + i*nx;
      ip = j + (i+1)*nx;
      im = j + (i-1)*nx;
      jp = (j + 1) + i*nx;
      jm = (j - 1) + i*nx;
      u[ij] = u_previous[ij] + a * dt * ( 
              (u_previous[ip] - 2*u_previous[ij] + u_previous[im]) / dx2 + 
              (u_previous[jp] - 2*u_previous[ij] + u_previous[jm]) / dy2 );
      }

  memcpy(u_previous, u, nx*ny*sizeof(double));
}
                

