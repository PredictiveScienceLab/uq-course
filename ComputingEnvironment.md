# Setting up your computing environment

## Step 1 : Creating your nanohub account.

If you don't already have one, create an account on [Nanohub](https://nanohub.org/). 

## Step 2 : Launch the Jupyter notebook tool  

2.1 Selects the 'Tools' option from the 'Resources' drop-down menu on top of the homepage and select the Jupyter notebook tool.

2.2 This should open up an 'Index' page for the jupyter notebook tool on a seperate tab on your browser. Note that you can find links to
learning resources for python/Jupyter notebooks at the bottom of this page. 

2.3 Click on 'My Files' on the top right corner of the Index page. This should open up the homepage of the Jupyter notebook server. You can 
launch your notebooks from here. 

## Step 3 : Installing pyMC.

3.1 From the 'New' drop-down menu at the top right corner of the Jupyter homepage, select 'Terminal'. This should open up a new unix terminal 
on a seperate tab and you should see a prompt which looks like this: ``` <your_username>@nanoHUB:~/notebooks$ ```.

3.2 Clone the source repository:
```
$git clone https://github.com/pymc-devs/pymc.git
```

3.3 Navigate to the pymc folder: ```$cd pymc```

3.4 Install the library:
```
$python setup.py install --prefix=..
```

## Step 4 : Clone course repository:
```
$cd ..
$git clone https://github.com/PredictiveScienceLab/uq-course.git
```
Now you should be able to run the handout notebooks / work on course assignments through the nanohub jupyter notebook tool.






