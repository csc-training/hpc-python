## Masked arrays

File [faulty_data.dat](faulty_data.dat) contains x, y data which should follow
approximately y=x^2 relation. Plot the data in order to find out if some of it
looks invalid. Create masked arrays representing only correct data, and fit a
second order polynomial to masked arrays using `ma.polyfit` (Note that standard
`np.polyfit` does not understand about masked arrays). Do the fit also with the
original data and compare the two results.
