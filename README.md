# Introduction to Uncertainty Quantification

This version of the course is being taught at Purdue University during Spring 2020.
The code for the course is ME 59700 and MA 59800.
The instructor is Prof. [Ilias Bilionis](https://www.predictivesciencelab.org/authors/ebilionis/).
The class meets every Tuesday and Thursday 12:00pm-1:15pm at WALC 2127.

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

  - Topics: Interpretation of probability as a representation of our state of knowledge, basic rules of probability, practice examples.
  - [Lecture notebook](lectures/lecture_03.ipynb)

+ Lecture 4 - Introduction to Probability Theory (Part II), 01/23/2018.

  - Topics: Discrete random variables, probability mass function, cumulative distribution function, expectation, variance, covariance, joint probability mass function, marginals, independence, conditional probability, the Bernoulli distribution, the Binomial distribution, the categorical distribution, the Poisson distribution.
  - [Lecture notebook](lectures/lecture_04.ipynb)

+ Lecture 5 - Introduction to Probability Theory (Part III), 01/28/2020.

  - Topics: Continuous random variables, the uniform distribution, the Gaussian distribution, analytical Bayesian inference examples.
  - [Lecture notebook](lectures/lecture_05.ipynb)

+ Lecture 6 - Introduction to Probability Theory (Part IV), 01/30/2020.

  - Topics: Bayesian parameter estimation, credible intervals, Bayesian decision making, analytical Bayesian inference examples.
  - [Lecture notebook](lectures/lecture_06.ipynb)

+ Lecture 7 - Introduction to Probability Theory (Part V), 02/04/2020.

  - Topics: Pseudo-random number generators, sampling the uniform distribution, the empirical cumulative distribution function, the Kolmogorov-Smirnov test, sampling the Bernoulli distribution, sampling any discrete distribution, limiting behavior of the binomial distribution, the central limit theorem and the ubiquitousness of the Gaussian distribution, sampling continuous distributions using inverse sampling and rejection sampling.
  - [Lecture notebook](lectures/lecture_07.ipynb)

+ Lecture 8 - Uncertainty Propagation: Introduction to Monte Carlo Sampling, 02/06/2020.

  - Topics: Curse of dimensionality, estimate multi-dimensional integrals using Monte Carlo, quantification of epistemic uncertainty in Monte Carlo estimates, example of uncertainty propagation through partial differential equations.
  - [Lecture notebook](lectures/lecture_08.ipynb)

+ Lecture 9 - Uncertainty Propagation: Advanced Monte Carlo Sampling, 02/11/2020.

  - Topics: Importance sampling, latin-hyper cube designs, example of uncertainty propagation through partial differential equations.
  - [Lecture notebook](lectures/lecture_09.ipynb)

+ Lecture 10 - Uncertainty Propagation: Perturbation Methods, 02/13/2020.

  - Topics: Taylor series expansions; The Laplace Approximation; Low-order perturbation methods for dynamical systems; Method of adjoints.
  - [Lecture notebook](lectures/lecture_10.ipynb)

+ Lecture 11 - Model Checking and Evaluation, 02/18/2020.

  - Topics: External validity, posterior predictive checking, test statistics, Bayesian p-values, examples.
  - [Lecture notebook](lectures/lecture_11.ipynb)

+ Lecture 12 - Basics of Curve Fitting: The Generalized Linear Model, 02/20/2020.

  - Topics: Supervised learning, regression, generalized linear model, least squares, maximum likelihood.
  - [Lecture notebook](lectures/lecture_12.ipynb)

+ Lecture 13 - Basics of Curve Fitting: Bayesian Linear Regression, 02/25/2020.

  - Topics: Maximum a posteriori estimates, Bayesian linear regression, evidence approximation, automatic relevance determination.
  - [Lecture notebook](lectures/lecture_13.ipynb)

+ Lecture 14 - Advanced Curve Fitting: Gaussian Processes to Encode Prior Knowledge about Functions, 02/27/2020.

  - Topics: Stochastic processes, random fields, Gaussian process, mean functions, covariance functions, sampling from a Gaussian process, encoding prior knowledge about functions.
  - [Lecture notebook](lectures/lecture_14.ipynb)

+ Lecture 15 - Advanced Curve Fitting: Gaussian Process Regression I, 03/03/2020.

  - Topics: Conditioning Gaussian random fields on exact and noisy observations.
  - [Lecture notebook](lectures/lecture_15.ipynb)

+ Lecture 16 - Advanced Curve Fitting: Gaussian Process Regression II, 03/05/2020.

  - Topics: Diagnostics for curve fitting, estimating the hyperparameters of covariance functions.
  - [Lecture notebook](lectures/lecture_15.ipynb) (same as lecture 15)

+ Lecture 17 - Advanced Curve Fitting: Multivariate Gaussian Process Regression and Automatic Relevance Determination, 03/10/2020.

  - Topics: Multivariate Gaussian process regression, automatic relevance determination, the curse of dimensionality, active subspaces, high-dimensional model representation.
  - [Lecture notebook](lectures/lecture_17.ipynb)

+ Lecture 18 - Application of Gaussian Process Regression: Optimizing expensive black-box functions, 03/12/2020.

  - Topics: Bayesian global optimization without noise, maximum upper interval, probability of improvement, expected improvement, quantifying epistemic uncertainty in the location of the maximum, Bayesian global optimization with noise.
  - [Lecture notebook](lectures/lecture_18.ipynb)

+ **No lecture on Tuesday 03/17/2020** (spring break).

+ **No lecture on Thursday 03/19/2020** (spring break).

+ Lecture 19 - Inverse Problems/Model Calibration: Classical Approach, 03/24/2020.

  - Topics: Formulate inverse problems as optimization problems, reaction kinetics example, shortcomings of the classical approach.
  - [Lecture notebook](lectures/lecture_19.ipynb)

+ Lecture 20 - Inverse Problems/Model Calibration: Bayesian Approach, 03/26/2020.

  - Topics: Ill-posed problems, Bayesian formulation, reminder of the Laplace approximation, reaction kinetics example, shortcomings of the Laplace approximation.
  - [Lecture notebook](lectures/lecture_20.ipynb)

+ Subject to change from this point on.

+ Lecture 19 - Sampling from Posteriors: The Metropolis Algorithm, 03/24/2020.

  - Topics: TBD.
  - [Lecture notebook](lectures/lecture_19.ipynb)

+ Lecture 20 - Sampling from Posteriors: The Metropolis-Hastings algorithm, 03/26/2020.

  - Topics: TBD.
  - [Lecture notebook](lectures/lecture_20.ipynb)

+ Lecture 21 - Sampling from Posteriors: Gibbs Sampling, 03/31/2020.

  - Topics: TBD
  - [Lecture notebook](lectures/lecture_21.ipynb)

+ Lecture 22 - Sampling from Posteriors: Sequential Monte Carlo, 04/02/2020.

  - Topics: TBD.
  - [Lecture notebook](lectures/lecture_22.ipynb)

+ Lecture 23 - Bayesian Model Selection, 04/07/2020.

  - Topics: TBD.
  - [Lecture notebook](lectures/lecture_23.ipynb)

+ Lecture 24 - Estimating Posteriors: Variational Inference, 04/09/2020.

  - Topics: TBD.
  - [Lecture notebook](lectures/lecture_24.ipynb)

+ Lecture 25 - Estimating Posteriors: Automatic Differentiation Variational Inference, 04/14/2020.

  - Topics: TBD.
  - [Lecture notebook](lectures/lecture_25.ipynb)

+ Lecture 26 - Bayesian Model Selection with Variational Inference, 04/16/2020.

  - Topics: TBD.
  - [Lecture notebook](lectures/lecture_26.ipynb)

+ Lecture 27 - Deep Neural Networks (Part I), 04/21/2020.

  - Topics: TBD.
  - [Lecture notebook](lectures/lecture_27.ipynb)

+ Lecture 28 - Deep Neural Networks (Part II), 04/23/2020.
  - Topics: TBD.
  - [Lecture notebook](lectures/lecture_28.ipynb)

+ Lecture 29 - Deep Neural Networks (Part III), 04/28/2020
  - Topics: TBD.
  - [Lecture notebook](lectures/lecture_29.ipynb)

+ Lecture 30 - Deep Neural Networks (Part IV), 04/30/2020
  - Topics: TBD.
  - [Lecture notebook](lectures/lecture_30.ipynb)

## Homework Notebooks

+ [Homework 1 (Lectures 1-6)](homeworks/hw_01.ipynb), due 02/04/2020.

+ [Homework 2 - (Lectures 7-10)](homeworks/hw_02.ipynb), due 02/18/2020.

+ [Homework 3 - (Lectures 12-13)](homeworks/hw_03.ipynb), due 03/05/2020.

+ Tentative, [Homework 4 - (Lectures 12-13)](homeworks/hw_04.ipynb): due 03/03/2020.

+ Tentative, [Homework 5 - (Lectures 14-15)](homeworks/hw_05.ipynb): due 03/10/2020.

+ Tentative, [Homework 6 - (Lectures 16-17)](homeworks/hw_06.ipynb), due 03/24/2020.

+ Tentative, [Homework 7 - (Lectures 18-20)](homeworks/hw_07.ipynb), due 04/02/2020.

+ Tentative, [Homework 8 - (Lectures 20-24)](homeworks/hw_08.ipynb), due 04/21/2020.

+ Tentative, [Homework 9 - (Lectures 25-29)](homeworks/hw_08.ipynb), due 05/03/2020.

## Project submission timeline

+ Title and abstract, due 02/15/2020.

+ Final report, due TBD.


## Running the notebooks on Google Colab

Make sure you have a Google account before you start.
Ok, there are many ways you can do this.
This is the simplest one:

### Google Colab using directly this GitHub site

+ Go to the [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb) website and login with your Google account (if you are not already logged in).

+ Then hit File->Open Notebook.

+ In the pop up window that opens, click on GitHub.

+ Write: https://github.com/PredictiveScienceLab/uq-course.git and hit enter.

+ Now you can select the notebook you would like to open.
For example, select "lecture_01.ipynb".

+ That's it.

### Google Colab using notebooks on your computer

+ First, download this repository to your computer.
Use this [link](https://github.com/PredictiveScienceLab/uq-course/archive/master.zip).
Unzip the file and make sure you know where it is.

+ Go to the [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb) website and login with your Google account (if you are not already logged in).

+ Google Colab can see your Google drive. So you should be able to open any notebook you have on your Google drive. This is one way you can do it.
Drop the course directory in your Google drive. You can find these by "File->Open Notebook" and hitting the Google Drive tab.

+ The other way is to individually upload notebooks.
On the Google Colab page hit File->Upload Notebook and drop the notebook you would like to open.

### Installing software on Google Colab
When running on google Colab, you will have to install some software manually **every time you run the notebook**.
For example, to install the Python module ``GPy``, you need to add a code block:
```
!pip install GPy
```

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

#### Linux

If you are using Linux, I am sure that you can figure it out on your own.

### Installation of Required Python Packages

Independently of the operating system, use the command line to install the following Python packages:
+ [Seaborn](http://stanford.edu/~mwaskom/software/seaborn/), for beautiful graphics:
```
conda install seaborn
```

+ [PyMC3](https://docs.pymc.io/) for MCMC sampling:
```
conda install pymc3
```

+ [GPy](https://github.com/SheffieldML/GPy) for Gaussian process regression:
```
pip install GPy
```

+ [pydoe](https://pythonhosted.org/pyDOE/randomized.html) for generating experimental designs:
```
pip install pydoe
```

+ [fipy](https://www.ctcms.nist.gov/fipy/) for solving partial differential equations using the finite volume method:
```
pip install fipy
```
*** Windows Users ***

You may receive the error
```
ModuleNotFoundError: No module named 'future'
```
If so, please install future and then install fipy:
```
pip install future
```

+ [scikit-learn](https://scikit-learn.org/stable/) for some standard machine learning algorithms implemented in Python:
```
conda install scikit-learn
```

+ [graphviz](https://www.graphviz.org/download/) for visualizing probabilistic graphical models:
```
pip install graphviz
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
