<!-- Title: Setting up the programming environment -->

<!-- Short description:

In this article we guide you through installing the software used during the 
course.

-->

In order to carry out the hands-on programming exercises, you need a working
Python environment as well as selected Python packages for scientific and
high-performance computing.

The following software will be used during the course:

- Python 3 interpreter
- NumPy 
- Numexpr 
- Matplotlib 
- Cython
- Mpi4py
- Optionally, iPython and Scipy

In Ubuntu based Linux environments installation can be done (admin rights needed) as

~~~bash
sudo apt install python3-numpy python3-numexpr python3-matplotlib cython3 python3-mpi4py python3-scipy ipython3 
~~~

We provide also a Virtual Machine image containing proper software environment.

== Setting up the Virtual Machine for the course ==
 
1. Download the Virtual Machine image:
   link here
   Size of download is about 1.8 GB
2. Install the VirtualBox software 
     - Download the installation file for your operating system (Windows,
       Mac, and Linux are all supported
     - When installing the software you might be asked to install some 
       device drivers: Oracle Corporation Universal Serial Bus, Network 
       Adapters, Network Service. Install them as well. If you are asked, 
       choose to install all the components of the VirtualBox software.
     - After installation you will be notified that the installation is 
       complete and you can already start Oracle VM VirtualBox in that step by 
       clicking finish.
3. Start VirtualBox
4. Import the Virtual Machine Image
     - In the File menu choose Import appliance
     - Select the HPCPython.ova image you downloaded in step 1.
     - Default values for memory and number of CPUs should be ok
       but you can increase them a bit depending on your system
5. You should now see **HPC Python** iamge listed in VirtualBox. You can start
   it either double clicking or via the `Start` button.
6. The system should now boot up and greet you with the login screen
     - Log in with user `Monty Python` and password `hpc1python`







