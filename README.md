# Introduction to Uncertainty Quantification

This version of the course is being taught at Purdue University during Spring 2018.
The code for the course is ME 59700 and MA 598.
The instructor is Prof. [Ilias Bilionis](http://www.predictivesciencelab.org/people.html).
The class meets every Tuesday and Thursday 12:00pm-1:15pm at Lambert Field House & Gym 104	.

The goal of this course is to introduce the fundamentals of uncertainty quantification to advanced undergraduates or graduate engineering and science students with research interests in the field of predictive modeling. Upon completion of this course the students should be able to:

+ Represent mathematically the uncertainty in the parameters of physical models.
+ Propagate parametric uncertainty through physical models to quantify the induced uncertainty on quantities of interest.
+ Calibrate the uncertain parameters of physical models using experimental data.
+ Combine multiple sources of information to enhance the predictive capabilities of models.
+ Pose and solve design optimization problems under uncertainty involving expensive computer simulations.

## Student Evaluation

+ 10% Participation
+ 60% Homework
+ 30% Final Project

## Lectures

+ [Lecture 1 - Introduction to Uncertainty Quantification on 01/09/2018](https://github.com/PredictiveScienceLab/uq-course/blob/master/handouts/handout_02.ipynb).


+ Lecture 2 - Probability Theory I on 01/11/2018.

  - Slides
  - Notebook


## Homework Sets

+ [Homework 1](hw/hw_01.ipynb) due on 01/16/2018.


## Installation of Required Software for Viewing the Notebookes

Find and download the right version of 
[Anaconda for Python 2.7](https://www.continuum.io/downloads) from Continuum Analytics.
This package contains most of the software we are going to need.

### OS Specific Instructions

#### Microsoft Windows

+ We need C, C++, Fortran compilers, as well as the Python sources.
Start a command line (look for ``cmd``) and type:
```
conda install mingw libpython
```
+ Finally, you need [git](https://git-scm.com/downloads). As you install it,
make sure you select that you want to use it from the Windows command prompt.

#### Apple OS X

+ Download and install [Xcode](https://developer.apple.com/xcode/download/)
+ Agree to the license of Xcode by opening a terminal and typing:
```
sudo xcrun cc
```
+ Install your favorite version of the GNU compiler suite.
You can do this with [Homebrew](http://brew.sh/) (after you install it of course),
by typing in the terminal:
```
brew install gcc
```
Alternatively, you may use the [MacPorts](https://www.macports.org/).

#### Linux

Nothing special is required.

### Installation of Required Python Packages

Independently of the operating system, use the command line to install the following Python packages:
+ [Seaborn](http://stanford.edu/~mwaskom/software/seaborn/), for beatiful graphics:
```
conda install seaborn
```

+ [PyMC](https://https://github.com/pymc-devs/pymc) for MCMC sampling:
```
conda install pymc
```

+ [GPy](https://github.com/SheffieldML/GPy) for Gaussian process regression:
```
pip install GPy
```

+ [py-design](https://github.com/PredictiveScienceLab/py-design) for generating designs for computer codes:
```
pip install py-design
```

+ [py-orthpol](https://github.com/PredictiveScienceLab/py-orthpol) for generating orthogonal polynomials with respect to arbitrary probability measures:
```
pip install py-orthpol
```

## Running the notebooks

+ Open the command line.
+ `cd` to your favorite folder.
+ Then, type:
```
git clone https://github.com/PredictiveScienceLab/uq-course.git
```
+ This will download the contents of this repository in a folder called `uq-course`.
+ Enter the ``uq-course`` folder:
```
cd uq-course
```
+ Start the jupyter notebook by typing the command:
```
jupyter notebook
```
+ Use the browser to navigate the course, experiment with code etc.
+ If the course contented is updated, type the following command (while being inside `uq-course`) to get the latest version:
```
git pull origin master
```
Keep in mind, that if you have made local changes to the repository, you may have to commit them before moving on.
