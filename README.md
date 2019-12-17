# Introduction to Uncertainty Quantification

This version of the course is being taught at Purdue University during Spring 2020.
The code for the course is ME 59700 and MA 59800.
The instructor is Prof. [Ilias Bilionis](https://www.predictivesciencelab.org/authors/ebilionis/).
The class meets every Tuesday and Thursday 12:00pm-1:15pm at ME 3006.

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

+ Lecture 1 - Introduction, 01/14/2020.

  - Topics: Course logistics and introduction.
  - [Lecture notebook](lectures/lecture_01.ipynb)

+ Lecture 2 - Introduction to Predictive Modeling, 01/16/2020.

  - Topics: Predictive modeling, structural causal models and their graphical
      representation, aleatory vs epistemic uncertainties,
      the uncertainty propagation problem, the model calibration problem.
  - [Lecture notebook](lectures/lecture_02.ipynb)

+ Lecture 3 - Introduction to Probability Theory (Part I), 01/21/2020.

  - Tentative
  - Topics: Dynamics of coin toss; Interpretation of probability; Basic rules of probability; Practice examples; Probability as an extension of Aristotelian logic.
  - [Notebook](handouts/handout_03.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jchtmcf4bcf5n3)

+ Lecture 4 - Introduction to Probability Theory (Part II), 01/23/2018.

  - Tentative
  - Topics: Independence; Conditional independence; Graphical representation of probability models; Causality; Discrete random variables; Continuous random variables; Expectations.
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jcc0r1i59hr3nc)

+ Lecture 5 - Common Random Variables, 01/28/2020.

  - Tentative
  - Topics: Uniform distribution; Generating uniform random numbers; Bernoulli distribution and how to sample it; Binomial distribution; Poisson distribution.
  - [Notebook](handouts/handout_05.ipynb)

+ Lecture 6 - Turning Prior Information to Probability Statements, 01/30/2020.

  - Tentative
  - Topics: Principle of insufficient reason, maximum entropy principle, statistical mechanics.
  - [Notebook](handouts/handout_06.ipynb)

+ Lecture 7 - Generalized Linear Models (Part I), 02/04/2020.

  - Tentative
  - Topics: Supervised learning; regression; generalized linear models; least squares; maximum likelihood.
  - [Notebook](handouts/handout_07.ipynb)

+ Lecture 8 - Generalized Linear Models (Part II), 02/06/2020.

  - Tentative
  - Topics: Bayesian linear regression; maximum a posteriori estimates.
  - [Notebook](handouts/handout_08.ipynb)

+ Lecture 9 - Generalized Linear Models (Part III), 02/11/2020.

  - Tentative
  - Topics: The evidence approximation; automatic relevance determination.
  - [Notebook](handouts/handout_08.ipynb) (*it is the same as lecture's 8 handout*)

+ Lecture 10 - Priors on Function Spaces, 02/13/2020.

  - Tentative
  - Topics: Random fields, Gaussian random fields (Gaussian processes).
  - [Notebook](handouts/handout_10.ipynb)

+ Lecture 11 - Conditioning a Random Field on Observations, 02/18/2020.

  - Tentative
  - Topics: Gaussian process regression
  - [Notebook](handouts/handout_11.ipynb)

+ Lecture 12 - Reducing the Dimensionality of Random Fields, 02/20/2020.

  - Tentative
  - Topics: Karhunen-Lo\`eve expansion (KLE); Nystr\"om approximation to the KLE.
  - [Notebook](handouts/handout_12.ipynb)

+ Lecture 13 - Uncertainty Propagation: Sampling Methods I, 02/25/2020.

  - Tentative
  - Topics: Monte Carlo; high-dimensional integration; error estimates; convergence.
  - [Notebook](handouts/handout_13.ipynb)

+ Lecture 14 - Uncertainty Propagation: Sampling Methods II, 02/27/2020.

  - Tentative
  - Topics: Importance sampling; latin hyper-cube designs; multi-level Monte Carlo.
  - [Notebook](handouts/handout_14.ipynb)

+ Lecture 15 - Uncertainty Propagation: Perturbation Methods, 03/03/2020.

  - Tentative
  - Topics: Taylor series expansions; The Laplace Approximation; Low-order perturbation methods for dynamical systems; Method of adjoints.
  - [Notebook](handouts/handout_15.ipynb)

+ Lecture 16 - Uncertainty Propagation: Polynomial Chaos I, 03/05/2020.

  - Tentative
  - Topics: Hilbert space of square integrable functions; orthogonal polynomials; constructing orthonormal polynomials in 1D; Hermite, Laguerre, Legendre polynomials; constructing multi-dimensional orthonormal polynomials; solving stochastic dynamical system with polynomial chaos;
  - [Notebook](handouts/handout_16.ipynb)

+ Lecture 17 - Uncertainty Propagation: Polynomial Chaos II, 03/10/2020.

  - Tentative
  - Topics: Quadrature rules in 1D; sparse grid collocation; intrusive solution of stochastic dynamical systems; stochastic harmonic oscillator.
  - [Notebook](handouts/handout_17.ipynb)

+ Lecture 18 - Uncertainty Propagation: Polynomial Chaos III, 03/12/2020.

  - Tentative
  - Topics: Intrusive polynomial chaos for stochastic dynamical systems; stochastic exponential decay; stochastic harmonic oscillator; Non-intrusive polynomial chaos.
  - [Notebook](handouts/handout_18.ipynb)

+ **No lecture on Tuesday 03/17/2020** (spring break).

+ **No lecture on Thursday 03/19/2020** (spring break).

+ Lecture 19 Inverse Problems/Model Calibration: Classic Approaches, 03/24/2020.

  - Tentative
  - Topics: Formulation of inverse problems as optimization problems; method of adjoints revisited; calibration of reaction kinetics problem.
  - [Notebook](handouts/handout_19.ipynb)

+ Lecture 20 - Inverse Problems/Model Calibration: Bayesian Approaches, 03/26/2020.

  - Tentative
  - Topics: stochastic formulation of inverse problems; the Laplace approximation; solving inverse problems with MCMC; hierarchical Bayes modeling.
  - [Notebook](handouts/handout_20.ipynb)

+ Lecture 21 - Markov Chain Monte Carlo I, 03/31/2020.

  - Tentative
  - Topics: Basics of Markov chains; random walks; Metropolis algorithm; Bayesian calibration of the catalysis problem.
  - [Notebook](handouts/handout_21.ipynb)

+ Lecture 22 - Markov Chain Monte Carlo II, 04/02/2020.

  - Tentative
  - Topics: Metropolis-Hastings; Metropolis-Adjusted Langevin Dynamics; Gibbs sampling; Hierarchical Bayes.
  - [Notebook](handouts/handout_22.ipynb)

+ Lecture 23 - Markov Chain Monte Carlo III, 04/07/2020.

  - Tentative
  - Topics: Hierarchical Bayes examples; Logistic regression; PyMC tutorial.
  - [Notebook](handouts/handout_23.ipynb)

+ Lecture 24 - Bayesian Model Selection I, 04/09/2020.

  - Tentative
  - Topics: Model evidence; Sequential Monte Carlo; Adaptive Importance Sampling.
  - [Notebook](handouts/handout_24.ipynb)

+ Lecture 25 - Bayesian Model Selection II, 04/14/2020.

  - Tentative
  - Topics: PySMC tutorial.
  - [Notebook](handouts/handout_24.ipynb)

+ Lecture 26 - Accelerating Bayesian Statistics, 04/16/2020.

  - Tentative
  - Topics: Kullback-Leibler divergence; expectation propagation; variational inference.
  - [Notebook](handouts/handout_26.ipynb)

+ Lecture 27 - Bayesian Algorithms for Solving Stochastic Optimization Problems with Expensive Information Sources, 04/21/2020.

  - Tentative
  - Topics: Bayesian global optimization; expected improvement; probability of improvement; knowledge gradient; expected improvement in dominated hypervolume.
  - [Notebook](handouts/handout_27.ipynb)

+ Lecture 28 - TBD, 04/23/2020

+ Lecture 29 - TBD, 04/28/2020

+ Lecture 30 - TBD, 04/30/2020

## Homework Notebooks

+ Tentative, [Homework 1 - Probability Theory Basics](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jcgek4cict75kr), due 01/28/2020.

+ Tentative, [Homework 2 - Choosing Prior Probabilities](homeworks/hw_02.ipynb), due 02/04/2020.

+ Tentative, [Homework 3 - Bayesian Linear Regression](homeworks/hw_03.ipynb), due 02/13/2020.

+ Tentative, [Homework 4 - Gaussian process regression and KL expansion](homeworks/hw_04.ipynb): due 02/25/2020.

+ Tentative, [Homework 5 - Propagating uncertainty using Monte Carlo Latin hypercube sampling](homeworks/hw_05.ipynb): due 03/05/2020.

+ Tentative, [Homework 6 - Polynomial Chaos and Stochastic Collocation method](homeworks/hw_06.ipynb), due 03/24/2020.

+ Tentative, [Homework 7 - Inverse Problems/Model Calibration and Bayesian model selection](homeworks/hw_07.ipynb), due 03/31/2020.

+ Tentative, HW 8 - TBD, due 04/16/2020.

+ Tentative, HW 9 - TBD, due 04/30/2020.

## Running the notebooks on Nanohub

**TODO: Rohit to update this. Step by step guide.
Please make sure that things are not duplicated. Remove when done.**

## Running the notebooks on your personal computer

Find and download the right version of
[Anaconda for Python 3.7](https://www.anaconda.com/distribution) from Continuum Analytics.
This package contains most of the software we are going to need.
**Note:** You do need Python 3 and note Python 2. The notebooks will not work
with Python 2.

### OS Specific Instructions

#### Microsoft Windows

+ We need C, C++, Fortran compilers, as well as the Python sources.
Start the command line by opening "Anaconda Prompt" from the
start menu. In the command line type:
```
conda config --append channels https://repo.continuum.io/pkgs/free
conda install mingw libpython
```
+ Finally, you need [git](https://git-scm.com/downloads). As you install it,
make sure to indicate that you want to use "Git from the command line and
also from 3rd party software".

#### Apple OS X

+ Download and install the latest version of [Xcode](https://developer.apple.com/xcode/download/).

+ Install your favorite version of the GNU compiler suite.
You can do this with [Homebrew](http://brew.sh/) (after you install it of course),
by typing in the terminal:
```
brew install gcc
```
Alternatively, you may use the [MacPorts](https://www.macports.org/).

#### Linux

If you are using Linux, I am sure that you can figure it out on your own.

### Installation of Required Python Packages

Independently of the operating system, use the command line to install the following Python packages:
+ [Seaborn](http://stanford.edu/~mwaskom/software/seaborn/), for beautiful graphics:
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

### Running the notebooks

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
+ If the course content has been updated, type the following command (while being inside `uq-course`) to get the latest version:
```
git pull origin master
```
Keep in mind, that if you have made local changes to the repository, you may have to commit them before moving on.
