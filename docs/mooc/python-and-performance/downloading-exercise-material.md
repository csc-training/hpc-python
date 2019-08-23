<!-- Title: Downloading exercise material -->

<!-- Short description:

In this article we instruct how to download the exercise material and test
the software installation
-->

In addition to installing the required software (as we did in the previous
step), you need to download also some material for the hands-on exercises.

Exercise material is hosted on GitHub at:
<https://github.com/csc-training/hpc-python>


## Download

You have three options for downloading the material to your own Linux system
or to the Virtual Machine:

1. **Recommended approach**: Fork the GitHub repository and clone your fork
     - You need to have a GitHub user account for this option
     - After forking the repository (Fork button in the top right corner),
       clone your fork e.g. with the command:
       `git clone https://github.com/my-github-username/hpc-python.git`
       An easy way to get the URL for cloning, is to copy it from the green
       **Clone or download** button on the Github page of your fork.
     - You can now push back to GitHub any work you do during the course
2. Clone the repository directly
     - You can clone the repository directly with the command:
       `git clone https://github.com/csc-training/hpc-python.git`
     - However, with this option, any changes you make will only be available
       locally and can not be pushed back to Github
3. (Not recommended): If needed, you can also download all the material via
   from the **Clone or download** button as a Zip-file. However, this option
   means you will loose all the benefits of version control.


## Overall structure

Skeleton code snippets and model solutions to hands-on exercises are in
separate directories for each exercise. The exercises are organised
in subdirectories (`mpi/`, `numpy/` etc.) for each topic under the main
directory (`hpc-python/`).

The file `README.md` contains a list of all exercises (with links), which is
also shown as the default page on Github, and can be an easy way to navigate
to an exercise.

Each exercise has also a README.md file that contains the instructions for the
exercise and a solution/ directory that contains a model solution. Additional
files (skeleton code, input data etc.) may also be present.


## Test the software installation

Go into the `test` subdirectory and execute the test set:

~~~bash
pythonuser@ubuntu:~/hpc-python$ cd test
pythonuser@ubuntu:~/hpc-python/test$ python3 test.py
~~~

If everything is fine, you should see **Test set passed** printed on the
screen.
