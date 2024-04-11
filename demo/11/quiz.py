import pandas as pd
import numpy as np

# Provided data frame 'df'
data = {
    'AUD/USD': [0.7280, 0.7209, np.nan, 0.7263, 0.7281, 0.7285],
    'EUR/AUD': [1.6232, 1.6321, 1.6221, 1.6282, np.nan, 1.6288],
}
index = ['2020-09-08', '2020-09-09', '2020-09-10', '2020-09-11', '2020-09-14', '2020-09-15']
df = pd.DataFrame(data, index)

# Question 1
# This will output an empty DataFrame because the index does not contain any strings between 'a' and 'z'.
q1_output = df.loc['a':'z']

# Question 2
# This will also output an empty DataFrame because the index does not contain any strings between '0' and 'z'.
q2_output = df.loc['0':'z']

# Question 3
# This will raise a KeyError because there is no column labeled 'z'.
new_df = df.copy()
new_df.loc['1', :] = 1
try:
    q3_output = new_df.loc['1', 'z']
except KeyError as e:
    q3_output = str(e)

# Question 4
# This will output an empty DataFrame because indices 100 to 1000 are out of range.
q4_output = df.iloc[100:1000]

# Question 5
# This will output a Series with the 'AUD/USD' column values.
q5_output = df.loc[:, 'AUD/USD']

# Question 6
# This will raise a KeyError because 'AUD/USD' is not a row label.
try:
    q6_output = df.loc['AUD/USD']
except KeyError as e:
    q6_output = str(e)
