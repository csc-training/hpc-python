# Introducing heat equation

In this article, we introduce the heat equation which will be
used in various hands-on exercises thoughtout the course

Heat (or diffusion) equation is partial differential equation, which 
describes how the temperature varies in space  over time.

The heat equation can be written as
$$
\frac{\partial u}{\partial t} = \alpha \nabla^2 u
$$
where **u(x, y, t)** is the temperature field that varies in space and time,
and α is thermal diffusivity constant.

The equation can be solved numerically in two dimensions by discretizing 
first the Laplacian with finite differences as
$$
\nabla^2 u  = \frac{u(i-1,j)-2u(i,j)+u(i+1,j)}{(\Delta x)^2} \\
 + \frac{u(i,j-1)-2u(i,j)+u(i,j+1)}{(\Delta y)^2}
$$

Given an initial condition (u(t=0) = u0) one can follow the time dependence of
the temperature field with explicit time evolution method:

$$
u^{m+1}(i,j) = u^m(i,j) + \Delta t \alpha \nabla^2 u^m(i,j) 
$$

Note: Algorithm is stable only when
$$
\Delta t < \frac{1}{2 \alpha} \frac{(\Delta x \Delta y)^2}{(\Delta x)^2 (\Delta y)^2}
$$
