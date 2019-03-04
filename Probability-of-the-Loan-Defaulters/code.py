# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)

total_length = len(df)
print(total_length)

fico = 0
for i in df['fico'] > 700:
    fico += i

print(fico)

p_a = fico/total_length
print(round(p_a, 2))

debt = 0
for i in df['purpose'] == 'debt_consolidation':
    debt += i

print(debt)

p_b = debt/total_length
print(round(p_b,2))

df1 = pd.Series(df.purpose == 'debt_consolidation')
print(df1)

p_a_b = (p_a * p_b)/p_a
print(p_a_b)

p_b_a = (p_a * p_b)/p_b
print(p_b_a)

result = ((p_a_b * p_b_a)/p_b_a == p_a)
print(result)
# code ends here


# --------------
# code starts here

prob_lp = df[df['paid.back.loan']== 'Yes'].shape[0]/df.shape[0]
print(prob_lp)

prob_cs = df[df['credit.policy']== 'Yes'].shape[0]/df.shape[0]
print(prob_cs)

new_df = df[df['paid.back.loan']== 'Yes']
print(new_df)

prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0]/new_df.shape[0]
print(p_a_b)

bayes = (prob_pd_cs * prob_lp)/prob_cs
print(bayes)

# code ends here


# --------------
# code starts here

plt.bar(df['purpose'].index, df['purpose'])

df1 = df[df['paid.back.loan']== 'No']
print(df1)

plt.bar(df1['purpose'].index, df1['purpose'])

# code ends here


# --------------
# code starts here

inst_median = df.installment.median()

inst_mean = df.installment.mean()

df.installment.hist(bins = 10)

df['log.annual.inc'].hist(bins = 10)
# code ends here


