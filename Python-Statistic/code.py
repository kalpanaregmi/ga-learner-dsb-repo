# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)
data["Gender"].replace("-","Agender",inplace=True)
gender_count=data["Gender"].value_counts()
gender_count.plot(kind='bar')

#Code starts here 




# --------------
#Code starts here
alignment=data["Alignment"].value_counts()
alignment.plot.pie()
plt.xlabel('Character Alignment')




# --------------
#Code starts here
sc_df=data[["Strength","Combat"]]
sc_covariance=sc_df.cov().iloc[0,1]
sc_strength=data["Strength"].std()
sc_combat=data["Combat"].std()
sc_pearson=sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)

ic_df=data[["Intelligence","Combat"]]
ic_covariance=ic_df.cov().iloc[0,1]
ic_intelligence=data["Intelligence"].std()
ic_combat=data["Combat"].std()
ic_pearson=ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)


# --------------
#Code starts here
total_high=data.Total.quantile(q=0.99)
super_best=data[data.Total>total_high]
super_best_names=[]
for name in super_best.Name:
    super_best_names.append(name)

print(super_best_names)





# --------------
#Code starts here
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))
ax_1.boxplot(super_best["Intelligence"])
ax_1.set(title="Intelligence")
ax_2.boxplot(super_best["Speed"])
ax_2.set(title="Speed")
ax_3.boxplot(super_best["Power"])
ax_3.set(title="Power")




