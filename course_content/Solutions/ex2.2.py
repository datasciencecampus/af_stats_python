salary_scatter = sns.scatterplot(data=salaries, 
                                 x='experience', 
                                 y='salary')

x = np.arange(10) # explanatory variable: years of experience for the x-axis
a0 = 1400 # slope 1: the rate at which the salary increases per year of experience
a1 = 1500 # slope 2: the rate at which the salary increases per year of experience
a2 = 1600 # slope 3: ""

b0 = 60000 # intercept 1: the starting salary
b1 = 58000 # intercept 2: the starting salary
b2 = 59000 # intercept 3: ""

y0 = a0*x + b # predicted salary 1
y1 = a1*x + b1 # predicted salary 2
y2 = a2*x + b2 # predicted salary 3

# First regression line
salary_scatter = sns.regplot(x=x, 
                             y=y0, 
                             marker="+")

# Second regression line
salary_scatter = sns.regplot(x=x, 
                             y=y1, 
                             marker="+", 
                             line_kws={"color": "red"})

# Third regression line
salary_scatter = sns.regplot(x=x, 
                             y=y2, 
                             marker="+", 
                             line_kws={"color": "orange"})

salary_scatter.set(xlim=(-0.5,9.5));