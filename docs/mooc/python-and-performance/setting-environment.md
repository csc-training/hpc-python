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
- Cffi
- Mpi4py
- Optionally, iPython and Scipy

In Ubuntu based Linux environments installation can be done (admin rights needed) as

~~~bash
sudo apt install python3-numpy python3-numexpr python3-matplotlib cython3
python3-cffi python3-mpi4py python3-scipy ipython3 
~~~

We provide also a Virtual Machine image containing proper software environment.

## Setting up the Virtual Machine for the course
 
1. Download the Virtual Machine [image](https://kannu.csc.fi/s/fKaGEfrfHWLANJ2)  
   Size of download is about 1.8 GB
2. Install the VirtualBox software 
     - Download the installation file for your operating system (Windows,
       Mac, and Linux are all supported) https://www.virtualbox.org/
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
![Import appliance](https://ugc.futurelearn.com/uploads/assets/04/95/0495c4ee-4e02-48c8-a2ef-0f254f9a036c.png "Import appliance")
     - Select the HPCPython.ova image you downloaded in step 1.
![Select image](https://ugc.futurelearn.com/uploads/assets/49/8f/498f5176-7962-49ef-b21b-7f6d62c7633a.png "Select image")
     - Default values for memory and number of CPUs should be ok
       but you can increase them a bit depending on your system
![Appliance settings](https://ugc.futurelearn.com/uploads/assets/31/f5/31f573bd-9824-4a3d-8255-f87b655a4775.png "Appliance settings")
5. You should now see **HPC Python** image listed in VirtualBox. You can start
   it either double clicking or via the `Start` button.
![Start virtual machine](img src=https://ugc.futurelearn.com/uploads/assets/ff/da/ffda9341-9c0b-4e05-b149-a2da397cf688.png "Start virtual machine")
6. The system should now boot up and greet you with the login screen
     - Log in with user `Monty Python` and password `hpc1python`
![Log in](https://ugc.futurelearn.com/uploads/assets/68/93/68930db0-c0e0-4ed5-bb9e-105557b7e96e.png "Log in")






