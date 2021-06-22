## Extracting the intercept

print("Intercept =", (results_mod2.params['C(department)[T.sociology]'] + results_mod2.params['Intercept']))


## Extracting the slope

print("(experience) coef. =", results_mod2.params['experience'])


## Extracting the R-squared

print("R^2 =", results_mod2.rsquared_adj)



# Model interpretation

## Intercept: The base salary for the sociology department from the line of best fit was 47800.2 USD.
## Slope: The rate at which salary increases with experience was estimated to be 755.5 USD per year based on the line of best fit.
## Overall fit: The model fit explained 91.8% of the variation in individual's salaries.