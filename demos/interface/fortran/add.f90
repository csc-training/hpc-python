subroutine add(a, b, n)

  implicit none

  ! f2py understands only limited number of kind parameters
  real(kind=8), intent(inout) :: a(n)
  real(kind=8), intent(inout) :: b(n)
  integer :: n

  a = a + b

end subroutine
