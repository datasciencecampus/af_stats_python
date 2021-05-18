# We can calculate this by plugging in 7 years into our model equation for informatics
# Note that we have to combine the baseline slope with our slope for informatics
# We also have to combine our baseline intercept with our intercept for informatics

(results_mod3.params['experience'] + results_mod3.params['experience:C(department)[T.informatics]'])*7 + results_mod3.params['Intercept'] + results_mod3.params['C(department)[T.informatics]']