# Statistics for Data Science

### Version 1.0

**Course Duration**

12 Hours

**Course Summary**

This course introduces the basics of carrying out a statistical analysis in Python. It covers exploratory data analysis and constructing and interpreting linear and generalized linear models. 

**Course Objective**

By the end of the course students will be comfortable implementing and interpreting linear models and generalized linear model in Python.

**Lead Developer**

Laurie Baker, Dan Lewis

**Course Reviewer(s)**

Pending

**Intended Audience**

This course is intended for those interested in learning and applying linear and generalized linear modelling to their work. 

**Learning Objective Detail**
### Chapter 1: Exploratory Data Analysis

By the end of Chapter 1, learners should know:

*   What is tidy data?
    *   What is a variable, value, and observation?
    *   Several python commands to explore the structure of the data
    *   What is the difference between a continuous and categorical variable?
    *   What is variation and covariation?
*  Where Exploratory Data Analysis fits within data analysis?
    *   How to use plots to explore variation in continuous variable and categorical variables
    *   How to use plots to explore covariation between two categorical variables, two continuous variables or a categorical and continuous variable. 

### Chapter 2: Model Basics

By the end of Chapter 2, learners should know:

*   Model Basics
    *	 What is a model family and fitted model?
    *	 What is the difference between a response and an explanatory variable?
    
*   Model Construction
    *  How to construct a linear model in python?
    *  What are the slope and intercept in a linear model?
    *  Picking out key information from the model table
    *  How to extract specific parameters from the model object.

*  Assessing Model Fit
    *	 How to inspect model residuals to assess model fit?
    *	 How to pick out key information from the table from a fitted model. 
    *  How to use Adjusted R-squared and AIC to compare models. 

### Chapter 3: Generalized Linear Models

By the end of Chapter 3, learners should know

* What is probability? 

* What is a random variable?

* What a probability distribution is and how it differs for continuous vs. discrete random variables?
* Be familiar with several common probability distributions used to model variation in the response variable
  * Binomial
  * Normal
  * Poisson
  * Negative Binomial

* How to implement a generalized linear model in python.

### Chapter 4: Bayesian Analysis

By the end of Chapter 4, learners should know

* What is Baye's rule and how it is used in Bayesian statistics?
* How Bayesian and Frequentist schools of thought differ?
* How to implement a simple Bayesian linear model in python.


**Course Type**

* E learning - Not Available
* Self learning - Available
* Face to face - Available

**Skill Level**

Participants should be familiar with Python but do not need any prior statistical training. 

**Pre requisite summary** 

Introduction to Python.

**Pre-requisites**

Package requirements: 
import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt # data plotting
import seaborn as sns # data visualisation and plotting
import statsmodels.api as sm # statistical modelling package
import statsmodels.formula.api as smf # statistical modelling package with R-like formulas
import scipy.stats as stats
import math

from statsmodels.genmod.generalized_linear_model import GLM # importing packages to run GLM
from statsmodels.genmod import families # importing families for exponential families
from scipy.stats import binom # to illustrate the binomial distribution.
from sklearn import datasets, linear_model # fetching iris dataset and linear model functions
from sklearn.metrics import mean_squared_error, r2_score

