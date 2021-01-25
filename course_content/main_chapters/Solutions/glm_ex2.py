from IPython.display import display

# Create rain categorical
bikes['rain'] = pd.cut(bikes['precip'], bins = [-1,0.001,0.3,4], labels = ['No Rain', 'Light Rain', 'Heavy Rain'])

# Fit Poisson model
formula = 'bb_count ~ rain*high_temp_C + weekend'
poisson_glm_ex1 = sm.formula.glm(formula = formula, data=bikes, family = sm.families.Poisson()).fit()

# Compute alpha
outcome = ((bikes['bb_count'] - poisson_glm_ex1.mu)**2 - bikes['bb_count'])/ poisson_glm_ex1.mu
aux_ols = sm.OLS(outcome, poisson_glm_ex1.mu).fit()
alpha = aux_ols.params['x1']

# Fit negative binomial model
nbin_glm_ex1 = sm.formula.glm(formula=formula, data=bikes, family = sm.families.NegativeBinomial(alpha = alpha)).fit()
display(nbin_glm_ex1.summary())

# Plot predictions

f, ax = plt.subplots(figsize=(12,6))
bikes['predict'] = nbin_glm_ex1.fittedvalues
ax.plot(bikes['date'], bikes['bb_count'], label = 'Observed')
ax.plot(bikes['date'], bikes['predict'], label = 'Predicted')
ax.legend()
ax.set_ylabel("Daily Number of Bicycles")
ax.set_xlabel("Time")
ax.set_title("Bicycle Counts: Observed vs. Negative Binomial Regression Model Predictions");