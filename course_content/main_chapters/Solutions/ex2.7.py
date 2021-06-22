# 1. Let's compare the models we ran using Adjusted R^2 and AIC. Using the notes above, discuss in groups or write a paragraph about which model you think is best and why?

print("Adjusted R^2 Model 1 = ", results_mod1.rsquared_adj, 
      "\nAdjusted R^2 Model 2 = ", results_mod2.rsquared_adj, 
      "\nAdjusted R^2 Model 3 = ", results_mod3.rsquared_adj)

## Model 3 explains the most variation out of the models with 93.5% of the variation in salary explained compared to 91.8% of variation in salary explained by Model 2.  Model 3 also has the lowest AIC 1917.8 compared to 1937.6 for Model 2. 

print("AIC Model 1 = ", results_mod1.aic, 
      "\nAIC Model 2 = ", results_mod2.aic, 
      "\nAIC Model 3 = ", results_mod3.aic)

#2. Take a look at the main parameters of Model 2 and Model 3 from the model summary tables. Do they seem to vary much between the models?

## Model 2

b1 = results_mod2.params['Intercept'] # biology
b2 = results_mod2.params['C(department)[T.english]'] + results_mod2.params['Intercept'] # english
b3 = results_mod2.params['C(department)[T.informatics]']  + results_mod2.params['Intercept'] # informatics
b4 = results_mod2.params['C(department)[T.sociology]'] + results_mod2.params['Intercept'] # sociology
b5 = results_mod2.params['C(department)[T.statistics]']  + results_mod2.params['Intercept'] # statistics

print(b1, b2, b3, b4, b5)


## The starting salary (intercept) ranges from 47800.20-78568.42 USD. 
## The yearly raise (slope) is the same for all departments and is 755.52 USD.


## Model 3

##Slope
a1 = results_mod3.params['experience']
a2 = results_mod3.params['experience:C(department)[T.english]'] + results_mod3.params['experience']
a3 = results_mod3.params['experience:C(department)[T.informatics]'] + results_mod3.params['experience']
a4 = results_mod3.params['experience:C(department)[T.sociology]'] + results_mod3.params['experience']
a5 = results_mod3.params['experience:C(department)[T.statistics]'] + results_mod3.params['experience']

print(a1, a2, a3, a4, a5)

## The slope (yearly raises) varies between 274.73 and 1941.12 USD per year.


## Intercept
b1 = results_mod3.params['Intercept']
b2 = results_mod3.params['C(department)[T.english]'] + results_mod3.params['Intercept']
b3 = results_mod3.params['C(department)[T.informatics]'] + results_mod3.params['Intercept']
b4 = results_mod3.params['C(department)[T.sociology]'] + results_mod3.params['Intercept']
b5 = results_mod3.params['C(department)[T.statistics]'] + results_mod3.params['Intercept']

print(b1, b2, b3, b4, b5)

## The intercept (starting salary) varies between 40923.71 and 80453.26 USD per year. 


## Comparing the two models the intercepts (starting salary) ranges do not vary greatly, however, the yearly raises vary quite a lot between Model 3 and Model 2. If we were interested in comparing department starting salaries between the model we could subtract the intercept estimated in model 3 by the intercept estimated in model 2 to see the difference. 

## The starting salary in biology was 2067.37 higher in model 3 compared to model 2

print(results_mod3.params['Intercept'] - results_mod2.params['Intercept'])

## The yearly raise in biology was estimated to be 480.78 USD per year lower in model 3 compared to model 2

results_mod3.params['experience']-results_mod2.params['experience']
