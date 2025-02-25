/*
 * SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>
 *
 * SPDX-License-Identifier: MIT
 */

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

