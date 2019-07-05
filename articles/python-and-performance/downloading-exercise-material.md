<!-- Title: Downloading exercise material -->

<!-- Short description:

In this article we instruct how to download the exercise material and test
the software installation
-->

In addition to installing required software, you need to download also some
material for the hands-on exercises.

Material is hosted in GitHub at: <https://github.com/csc-training/hpc-python>
You have three options for downloading the material to your own Linux system
or to the Virtual Machine:

1. Recommended approach: Fork the GitHub repository and clone then your fork
     - You need to have a GitHub user account for forking
     - After Forking clone the repository e.g. with 
       `git clone https://github.com/my-github-username/hpc-python.git`
       The URL for cloning can be copied via the `Clone or download` button.
     - You can now push back to GitHub any work you do during the course
2. Clone the repository directly
     - You can clone the repository directly with  
       `git clone https://github.com/csc-training/hpc-python.git`
     - However, you cannot push back any changes
3. (Not recommended): You can download all the material via `Clone or download`
   as Zip-file. However, you loose all the benefits of version control

Skeleton code snippets and model solutions to hands-on exercises are in
individual subdirectories under hpc-python.

## Testing the software installation 

Go into the `test` subdirectory and execute the test set:
~~~bash
pythonuser@ubuntu:~/hpc-python$ cd test
pythonuser@ubuntu:~/hpc-python/test$ python3 test.py
~~~
If everything is fine, you should see **Test set passed** printed on the
screen.





