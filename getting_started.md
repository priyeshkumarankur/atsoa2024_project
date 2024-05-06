
## Installing Prerequisite Software
 **1) Python, C & C++** (installation via apt package manager)

     >  sudo apt update                    # Update the Package Repository
      
     >  sudo apt install python3           # Install Python
     >  python3 --version                  # Verify Installation

     >  sudo apt install gcc               # Install GCC on Ubuntu
     >  sudo apt install build-essential
     >  gcc --version                      # Verify Installation
 
 **2) openmpi library**

     >  sudo apt-get install openmpi-bin libopenmpi-dev
     >  which mpifort && which mpirun                       # Verify Installation
  
**3) Paraview** 

     >  sudo apt-get update
     >  sudo apt-get install paraview


## Read about: (just google it)
- Numerical Simulation
- Astrophysical fluid dynamics
- PLUTO Astrophysics code
- Kelvin-Helmholtz Instability
- Rayleigh-Taylor Instability
- Astrophysical Jets
- Blast Simulations


## Tasks:
1) Install Linux on your system. Try to install the prerequisite software as mentioned in the above message.
2) Download the PLUTO code https://plutocode.ph.unito.it/download.html
3) Go through Chapter 0 Quick Start of the documentation (https://plutocode.ph.unito.it/userguide.pdf) and try to follow the steps mentioned there.


## Steps to run a simulation:
1) Go to the directory of any test problem. We need 3 files for the simulation - definition.h ,pluto.ini , and init.c
  
       > cp definitions_01.h definitions.h
       > cp pluto_01.ini pluto.ini
    
3) First, run the Python script, which will create the makefile (choose linux.gcc for serial run and linux.mpicc for parallel runs).
  
       > python3 $PLUTO_DIR/setup.py
   
5) Make sure to change output format to **vtk files**.
6) Now run makefile, it will compile all the .c files into .o files, and a binary file ***pluto*** will be generated.
   
        > make
   
8) Then, finally, run ***pluto*** file.

        > ./pluto                   # for serial
        >  mpirun -np 4 ./pluto     # for parallel
   
## Steps to visualise the simulation data:
1) open paraview in the same directory where simulation data is kept.
2) open all vtk files group, and apply.


### Read the initial chapters of this note, which will give you all an idea about fluids and fluid equations.



