subroutine evolve(u, u_previous, nx, ny, a, dt, dx2, dy2)

   implicit none

   real*8, intent(inout) :: u(nx,ny), u_previous(nx, ny)
   !f2py intent(in, out) :: u, u_previous
   integer :: nx, ny
   real*8 :: a, dt, dx2, dy2

   integer :: i,j

   do j = 2, ny-1
     do i = 2, nx-1
        u(i,j) = u_previous(i,j) + a * dt * (  &
                 (u_previous(i-1, j) - 2*u_previous(i,j) +  &
                     u_previous(i+1, j)) / dx2 + &
                 (u_previous(i, j-1) - 2*u_previous(i,j) +  &
                     u_previous(i, j+1)) / dy2 )
     end do
   end do
   u_previous(:,:) = u(:,:)


end subroutine
