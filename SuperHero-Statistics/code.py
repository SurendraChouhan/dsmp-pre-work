# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
print(data)

#Code starts here 
data['Gender'].replace('-', 'Agender', inplace = True)
print(data)

gender_count = data.Gender.value_counts()
print(gender_count)



# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
print(alignment)

plt.pie(alignment)
plt.show()
plt.title("Character Alignment")


# --------------
#Code starts here
sc_df = data[['Strength', 'Combat']].copy()
print(sc_df)

sc_covariance = sc_df.Strength.cov(sc_df.Combat)
print(sc_covariance)

sc_strength = sc_df.Strength.std()
print(sc_strength)

sc_combat = sc_df.Combat.std()
print(sc_combat)

sc_pearson = sc_covariance/(sc_strength * sc_combat)
print(sc_pearson)

#Pearson for the columns Intelligence and Combat
print('='*50)

ic_df = data[['Intelligence','Combat']].copy()
print(ic_df)

ic_covariance = ic_df.Intelligence.cov(sc_df.Combat)
print(ic_covariance)

ic_intelligence = ic_df.Intelligence.std()
print(ic_intelligence)

ic_combat = ic_df.Combat.std()
print(ic_combat)

ic_pearson = ic_covariance/(ic_intelligence * sc_combat)
print(ic_pearson)


# --------------
#Code starts here
total_high = data.Total.quantile(0.99)
print(total_high)

#super_best = data[['Total'] > total_high]
#print(super_best)

super_best = data.loc[data['Total'] > total_high]
print(super_best)

super_best_names = list(super_best[['Name']].copy())

print(super_best_names)


# --------------
#Code starts here
import matplotlib.pyplot as plt

fig, (ax_1, ax_2, ax_3) = plt.subplots(1, 3, figsize = (20, 8))

ax_1.boxplot(super_best['Intelligence'])

ax_1.set(title = 'Intelligence')

ax_2.boxplot(super_best['Speed'])

ax_2.set(title = 'Speed')

ax_3.boxplot(super_best['Power'])

ax_3.set(title = 'Power')
#print(ax1)


