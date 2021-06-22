## 1. Which department gets the highest raises (biggest slope)?


# Looking at the plot both the informatics department and the sociology department have steep positive slopes but it is difficult to tell by eye which has a higher slope (estimated yearly raise).

a3 = results_mod3.params['experience:C(department)[T.informatics]'] + results_mod3.params['experience']
a4 = results_mod3.params['experience:C(department)[T.sociology]'] + results_mod3.params['experience']

print('Informatics slope:', a3)
print('Sociology slope:', a4)

## Yearly raise: The sociology department has the highest estimated yearly raise with 1941.11 USD increase in pay per year. The informatics department has the second highest estimates yearly raise with 1526.05 USD increase in pay per year.

## 2. Which department has the highest starting salary (biggest intercept)?

# Looking at the plot the statistics department has the largest intercept (highest point crossing the y-axis). 

b5 = results_mod3.params['C(department)[T.statistics]'] + results_mod3.params['Intercept']

print('Statistics Intercept', b5)


## The starting salary is estimated at 80,453.3 USD.