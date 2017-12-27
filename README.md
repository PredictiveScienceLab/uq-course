# Introduction to Uncertainty Quantification

This version of the course is being taught at Purdue University during Spring 2018.
The code for the course is ME 59700.
The instructors is Prof. [Ilias Bilionis](http://www.predictivesciencelab.org/people.html).
The class meets every Tuesday and Thursday 1:30pm-2:45pm at ME ????.

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

+ [Lecture 1 - Introduction to Uncertainty Quantification](lectures/lec_01.ipynb) on 01/12/2017.

+ [Lecture 2 - Probability Theory](lectures/lec_02.ipynb) on 01/14/2017.

+ [Lecture 3 - Probability Distributions](lectures/lec_03.ipynb) on 01/19/2017.

+ [Lecture 4 - Uncertainty Propagation using Sampling Methods: Monte Carlo](lectures/lec_04.ipynb) on 01/21/2017.

+ [Lecture 5 - Uncertainty Propagation using Sampling Methods: Latin-hypercube designs](lectures/lec_05.ipynb) on 01/26/2017.

+ [Lecture 6 - Uncertainty Propagation using Polynomial Chaos I](lectures/lec_06.ipynb) on 01/28/2017.

+ [Lecture 7 - Uncertainty Propagation using Polynomial Chaos II](lectures/lec_07.ipynb) on 02/02/2017.

+ [Lecture 8 - Uncertainty Propagation using Polynomial Chaos III](lectures/lec_08.ipynb) on 02/04/2017.

+ [Lecture 9 - Maximum Likelihood, Bayesian Parameter Estimation, Bayesian Linear Regression](lectures/lec_09.ipynb) on 02/09/2017.

+ [Lecture 10 - Priors of Function Spaces: Gaussian Processes](lectures/lec_10.ipynb) on 02/11/2017.

+ [Lecture 11 - Gaussian Process Regression](lectures/lec_11.ipynb) on 02/16/2017.

+ [Lecture 12 - Dimensionality Reduction: Principal Component Analysis](lectures/lec_12.ipynb) on 02/18/2017.

+ [Lecture 13 - Dimensionality Reduction of Random Fields: The Karhunen-Loeve Expansion](lectures/lec_13.ipynb) on 02/23/2017.

+ [Lecture 14](lectures/lec_14.ipynb) on 02/25/2017.

+ [Lecture 15](lectures/lec_15.ipynb) on 03/01/2017.

+ [Lecture 16](lectures/lec_16.ipynb) on 03/03/2017.

+ [Lecture 17](lectures/lec_17.ipynb) on 03/08/2017.

+ [Lecture 18](lectures/lec_18.ipynb) on 03/10/2017.

+ [Lecture 19](lectures/lec_19.ipynb) on 03/22/2017.

+ [Lecture 20](lectures/lec_20.ipynb) on 03/24/2017.

+ [Lecture 21 - Markov Chain Monte Carlo Methods (Part I)](lectures/lec_21.ipynb) on 03/29/2017.

+ [Lecture 22 - Markov Chain Monte Carlo Methods (Part II)](lectures/lec_22.ipynb) on 03/31/2017.

+ [Lecture 23](lectures/lec_23.ipynb) on 04/05/2017.

+ [Lecture 24](lectures/lec_24.ipynb) on 04/07/2017.

+ [Lecture 25 - How to Optimize Expensive Functions](lectures/lec_25.ipynb) on 04/12/2017.

+ [Lecture 26 - Sequential Monte Carlo and Bayesian Model Comparison](lectures/lec_26.ipynb) on 04/14/2017.


## Homework Sets

+ [Homework 1](hw/hw_01.ipynb) due on 01/26/2017.

+ [Homework 2](hw/hw_02.ipynb) due on 02/18/2017.

+ [Homework 3](hw/hw_03.ipynb) due on 03/03/2017.

+ [Homework 4](hw/hw_04.ipynb) due on 04/07/2017.

+ [Homework 5](hw/hw_05.ipynb) due on 04/21/2017.



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
