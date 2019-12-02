# Introduction to Uncertainty Quantification

This version of the course is being taught at Purdue University during Spring 2018.
The code for the course is ME 59700 and MA 598.
The instructor is Prof. [Ilias Bilionis](http://www.predictivesciencelab.org/people.html).
The class meets every Tuesday and Thursday 12:00pm-1:15pm at GRIS 102.

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

+ Lecture 1 - Introduction, 01/09/2018.
  
  - Topics: Course logistics.
  - [Notebook](handouts/handout_01.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jc5ad23r6uy2x4)
  
+ Lecture 2 - Quantifying Uncertainties in Physical Models, 01/11/2018.

  - Topics: Scope of UQ; Aleatoric vs epistemic uncertainties; Uncertainty propagation problem; Hands-on example.
  - [Notebook](handouts/handout_02.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jc5fvaa8ic74uf)
  - [Handwritten Notes](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jcc0pqc0cxx39e)
  - [Video](https://nanohub.org/resources/27933/watch?resid=27934)

+ Lecture 3 - Introcution to Probability Theory (Part I), 01/16/2018.

  - Topics: Dynamics of coin toss; Interpretation of probability; Basic rules of probability; Practice examples; Probability as an extension of Aristotelian logic.
  - [Notebook](handouts/handout_03.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jchtmcf4bcf5n3)
  - [Handwritten Notes](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jcifed4ka9334d)
  - [Video](https://nanohub.org/resources/27945/watch?resid=27947)
  
+ Lecture 4 - Introduction to Probability Theory (Part II), 01/18/2018.

  - Topics: Independence; Conditional independence; Graphical representation of probability models; Causality; Discrete random variables; Continuous random variables; Expectations.
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jcc0r1i59hr3nc)
  - [Handwritten Notes](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jckn3jo0rp234j)
  - [Video](https://nanohub.org/resources/27993/watch?resid=28001)
  
+ Lecture 5 - Common Random Variables, 01/23/2018.

  - Topics: Uniform distribution; Generating uniform random numbers; Bernoulli distribution and how to sample it; Binomial distribution; Poisson distribution.
  - [Notebook](handouts/handout_05.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jcuq4thgjk32bo)
  - [Video](https://www.youtube.com/watch?v=HIU7bExENjU)
  
+ Lecture 6 - Turning Prior Information to Probability Statements, 01/25/2018.

  - Topics: Principle of insufficient reason, maximum entropy principle, statistical mechanics.
  - [Notebook](handouts/handout_06.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jcuq5gcljy32pt)
  - [Video](https://www.youtube.com/watch?v=Kv82r4Bu338)
  
+ Lecture 7 - Generalized Linear Models (Part I), 01/30/2018.

  - Topics: Supervised learning; regression; generalized linear models; least squares; maximum likelihood.
  - [Notebook](handouts/handout_07.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jcz3tpfjvn9305)
  - [Video](https://www.youtube.com/watch?v=KQm-MZwaqts)
  
+ Lecture 8 - Generalized Linear Models (Part II), 02/01/2018.

  - Topics: Bayesian linear regression; maximum a posteriori estimates.
  - [Notebook](handouts/handout_08.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jcz8xnf5b3r116)
  - [Video](https://www.youtube.com/watch?v=iZUZ_PxDjjc)
  
+ Lecture 9 - Generalized Linear Models (Part III), 02/01/2018.

  - Topics: The evidence approximation; automatic relevance determination.
  - [Notebook](handouts/handout_08.ipynb) (*it is the same as lecture's 8 handout*)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jd92et3im3f705)
  - [Video](https://www.youtube.com/watch?v=LxHLfkH8iec)

+ Lecture 10 - Priors on Function Spaces, 02/08/2018.

  - Topics: Random fields, Gaussian random fields (Gaussian processes).
  - [Notebook](handouts/handout_10.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jd92f0cjjuw747)
  - [Video](https://www.youtube.com/watch?v=B-jmRZ0yncs)
  
+ Lecture 11 - Conditioning a Random Field on Observations, 02/13/2018.

  - Topics: Gaussian process regression
  - [Notebook](handouts/handout_11.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jdj4dvx098o5ld)
  - [Video](https://www.youtube.com/watch?v=MiVdNQ5DN8Y)
  
+ Lecture 12 - Reducing the Dimensionality of Random Fields, 02/15/2018.

  - Topics: Karhunen-Lo\`eve expansion (KLE); Nystr\"om approximation to the KLE.
  - [Notebook](handouts/handout_12.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jdj4eqjt4gk673)
  - [Video](https://www.youtube.com/watch?v=pQRRCihuOms)
   
+ Lecture 13 - Uncertainty Propagation: Sampling Methods I, 02/20/2018.

  - Topics: Monte Carlo; high-dimensional integration; error estimates; convergence.
  - [Notebook](handouts/handout_13.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jdm9fe56l3669e)
  - [Video](https://www.youtube.com/watch?v=ahr7ZRk1AyM)
  
+ Lecture 14 - Uncertainty Propagation: Sampling Methods II, 02/22/2018.

  - Topics: Importance sampling; latin hyper-cube designs; multi-level Monte Carlo.
  - [Notebook](handouts/handout_14.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jdqh0pde6ny3jg)
  - [Video](https://www.youtube.com/watch?v=6O_l-UVUbuU)

+ Lecture 15 - Uncertainty Propagation: Perturbation Methods, 02/27/2018.

  - Topics: Taylor series expansions; The Laplace Approximation; Low-order perturbation methods for dynamical systems; Method of adjoints.
  - [Notebook](handouts/handout_15.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/je26yh0hgjm23g)
  - [Video](https://www.youtube.com/watch?v=C8Y47zzq8-E)
  
   
+ Lecture 16 - Uncertainty Propagation: Polynomial Chaos I, 03/01/2018.

  - Topics: Hilbert space of square integrable functions; orthogonal polynomials; constructing orthonormal polynomials in 1D; Hermite, Laguerre, Legendre polynomials; constructing multi-dimensional orthonormal polynomials; solving stochastic dynamical system with polynomial chaos;
  - [Notebook](handouts/handout_16.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jea4oym2rj75h4)
  - [Video](https://www.youtube.com/watch?v=k3m3Ncbm-o8)
  
+ Lecture 17 - Uncertainty Propagation: Polynomial Chaos II, 03/06/2018.

  - Topics: Quadrature rules in 1D; sparse grid collocation; intrusive solution of stochastic dynamical systems; stochastic harmonic oscillator.
  - [Notebook](handouts/handout_17.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jegdbeaultz28j)
  - [Video](https://www.youtube.com/watch?v=xvLJZb-S2zo)
 
+ Lecture 18 - Uncertainty Propagation: Polynomial Chaos III, 03/08/2018.
  
  - Topics: Intrusive polynomial chaos for stochastic dynamical systems; stochastic exponential decay; stochastic harmonic oscillator; Non-intrusive polynomial chaos.
  - [Notebook](handouts/handout_18.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jegdbhy7uth2ar)
  - [Handwritten Notes](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jeotr9mszfb13h)
  - [Video](https://www.youtube.com/watch?v=FI-U9adhyYw)

+ **No lecture on Tuesday 03/12/2018** (spring break).

+ **No lecture on Thursday 03/15/2018** (spring break).

+ Lecture 19 Inverse Problems/Model Calibration: Classic Approaches, 03/20/2018.
 
  - Topics: Formulation of inverse problems as optimization problems; method of adjoints revisited; calibration of reaction kinetics problem.
  - [Notebook](handouts/handout_19.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jeri5f7ncyj4f)
  - [Video](https://www.youtube.com/watch?v=5oFT-pTHuZ8)
  
+ **No lecture on Thursday 03/22/2018** (The instructor will be at [2018 NSF Design Circle Workshop: Designing and Developing Global Engineering Systems](http://blogs.oregonstate.edu/designcircle/)).
  
+ Lecture 20 - Inverse Problems/Model Calibration: Bayesian Approaches, 03/27/2018.

  - Topics: stochastic formulation of inverse problems; the Laplace approximation; solving inverse problems with MCMC; hierarchical Bayes modeling.
  - [Notebook](handouts/handout_20.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jeyg7ilzq8t2sf)
  - [Video](https://www.youtube.com/watch?v=611ypCZVzuA)
  
+ Lecture 21 - Markov Chain Monte Carlo I, 03/29/2018.

  - Topics: Basics of Markov chains; random walks; Metropolis algorithm; Bayesian calibration of the catalysis problem.
  - [Notebook](handouts/handout_21.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jf8smnt2y7t3w5)
  - [Video](https://www.youtube.com/watch?v=3BhLfHcafEI)

+ Lecture 22 - Markov Chain Monte Carlo II, 04/03/2018.

  - Topics: Metropolis-Hastings; Metropolis-Adjusted Langevin Dynamics; Gibbs sampling; Hierarchical Bayes.
  - [Notebook](handouts/handout_22.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jfhayrmizm96qo)
  - [Video](https://www.youtube.com/watch?v=A-M82GeUxTU)

+ Lecture 23 - Markov Chain Monte Carlo III, 04/05/2018.

  - Topics: Hierarchical Bayes examples; Logistic regression; PyMC tutorial.
  - [Notebook](handouts/handout_23.ipynb)
  - Slides: No slides. This is a hands-on section.

+ Lecture 24 - Bayesian Model Selection I, 04/10/2018.

  - Topics: Model evidence; Sequential Monte Carlo; Adaptive Importance Sampling.
  - [Notebook](handouts/handout_24.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jfidv8saabj2fi)
  - [Video](https://www.youtube.com/watch?v=-UDjaxgmMGY)

+ Lecture 25 - Bayesian Model Selection II, 04/12/2018.

  - Topics: PySMC tutorial.
  - [Notebook](handouts/handout_24.ipynb)
  - Slides: No slides. This is a hands-on section.
  
  
+ **No lecture on Tuesday 04/17/2018** (The instructor will be at the [SIAM Conference for Uncertainty Quantification 2018](https://www.siam.org/meetings/uq18/)).

+ **No lecture on Thursday 04/19/2018** (The instructor will be at the [SIAM Conference for Uncertainty Quantification 2018](https://www.siam.org/meetings/uq18/)).

+ Lecture 26 - Accelerating Bayesian Statistics, 04/24/2018.

  - Topics: Kullback-Leibler divergence; expectation propagation; variational inference.
  - [Notebook](handouts/handout_26.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jgbgxcedtkoau)
  - [Video](https://www.youtube.com/watch?v=buVaK51Y1Eo)

+ Lecture 27 - Bayesian Algorithms for Solving Stochastic Optimization Problems with Expensive Information Sources, 04/26/2018.

  - Topics: Bayesian global optimization; expected improvement; probability of improvement; knowledge gradient; expected improvement in dominated hypervolume.
  - [Notebook](handouts/handout_27.ipynb)
  - [Slides](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jgbgvdvdjwa73w)



## Homework Notebooks

+ [Homework 1 - Probability Theory Basics](https://piazza.com/class_profile/get_resource/jbozz0zxpftby/jcgek4cict75kr), due 01/23/2018.

+ [Homework 2 - Choosing Prior Probabilities](homeworks/hw_02.ipynb), due 01/30/2018.

+ [Homework 3 - Bayesian Linear Regression](homeworks/hw_03.ipynb), due 02/15/2018.

+ [Homework 4 - Gaussian process regression and KL expansion](homeworks/hw_04.ipynb): due 03/01/2018.

+ [Homework 5 - Propagating uncertainty using Monte Carlo Latin hypercube sampling](homeworks/hw_05.ipynb): due 03/09/2018.

+ [Homework 6 - Polynomial Chaos and Stochastic Collocation method](homeworks/hw_06.ipynb), due 03/27/2018.

+ [Homework 7 - Inverse Problems/Model Calibration and Bayesian model selection](homeworks/hw_07.ipynb), due 04/26/2018.


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
