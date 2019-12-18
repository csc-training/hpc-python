subroutine add(a, b, c, n)

  implicit none

  ! f2py understands only limited number of kind parameters
  real(kind=8), intent(in) :: a(n)
  real(kind=8), intent(in) :: b(n)
  real(kind=8), intent(out) :: c(n)
  integer :: n

  c = a + b

end subroutine
