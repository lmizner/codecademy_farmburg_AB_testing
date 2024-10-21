# Import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from scipy.stats import binom_test

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')

# Inspect data
print(abdata.head())

# Create a contingency table 
Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab)

# Run Chi-Square test
chi2, pval, dof, expected = chi2_contingency(Xtab)
print(pval)

# Determine if the p-value is significant
is_significant = True

# Calculate number of visitors
num_visits = len(abdata)
print(num_visits)

# Calculate the purchase rate needed at 0.99
num_sales_needed_099 = 1000 / 0.99
p_sales_needed_099 = num_sales_needed_099 / num_visits

print(num_sales_needed_099)
print(p_sales_needed_099)

# Calculate the purchase rate needed at 1.99
num_sales_needed_199 = 1000 / 1.99 
p_sales_needed_199 = num_sales_needed_199 / num_visits

print(num_sales_needed_199)
print(p_sales_needed_199)

# Calculate the purchase rate needed at 4.99
num_sales_needed_499 = 1000 / 4.99
p_sales_needed_499 = num_sales_needed_499 / num_visits

print(num_sales_needed_499)
print(p_sales_needed_499)

# Calculate samp size & sales for 0.99 price point
samp_size_099 = np.sum(abdata.group == 'A')
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))

print(samp_size_099)
print(sales_099)

# Calculate samp size & sales for 1.99 price point
samp_size_199 = np.sum(abdata.group == 'B')
sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))

print(samp_size_199)
print(sales_199)

# Calculate samp size & sales for 4.99 price point
samp_size_499 = np.sum(abdata.group == 'C')
sales_499 = np.sum((abdata.group == 'C') & (abdata.is_purchase == 'Yes'))

print(samp_size_499)
print(sales_499)

# Calculate the p-value for Group A
pvalueA = binom_test(sales_099, n = samp_size_099, p = p_sales_needed_099, alternative = 'greater')
print(pvalueA)

# Calculate the p-value for Group B
pvalueB = binom_test(sales_199, n = samp_size_199, p = p_sales_needed_199, alternative = 'greater')
print(pvalueB)

# Calculate the p-value for Group C
pvalueC = binom_test(sales_499, n = samp_size_499, p = p_sales_needed_499, alternative = 'greater')
print(pvalueC)


# Final answer: Based on this information, what price should be chared for the upgrade package?
final_answer = '4.99'

# Print the chosen price group
print(final_answer)
