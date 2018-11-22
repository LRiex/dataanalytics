import numpy as np
import pandas as pd
import random
dfMain = pd.read_csv("Sample_Crimes.csv")
# print dfMain.head(3) #prints 3 heading rows

# df = pd.read_csv("DayofWeek.csv")

# for index in range(0, len(df.values)):
# dfMain.loc[dfMain["LocationDescription"] == Nan, "LocationDescription"] = 1

# dfMain.to_csv("Sample_Crimes.csv", index=False)

# print dfMain.values[206]

indexing = random.sample(range(0, 20000), 100)

X = dfMain.values[indexing, 0:7]
Y = dfMain.values[indexing, 7]
print [sum(Y==i) for i in range(1,35)]

from sklearn.naive_bayes import BernoulliNB

clf = BernoulliNB()
clf.fit(X, Y)
# BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)
# print X[6:800]
print clf.predict(X[6:10])