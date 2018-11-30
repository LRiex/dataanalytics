import numpy as np
import pandas as pd
import random
dfMain = pd.read_csv("Sample_Crimes2.csv")
# print dfMain.head(3) #prints 3 heading rows

# df = pd.read_csv("DayofWeek.csv")

# for index in range(0, len(df.values)):
# dfMain.loc[dfMain["LocationDescription"] == Nan, "LocationDescription"] = 1

# dfMain.to_csv("Sample_Crimes.csv", index=False)

# print dfMain.values[206]

indexing = random.sample(range(0, 20000), 1000)

X = dfMain.values[indexing, 0:13]
Y = dfMain.values[indexing, 13]
print [sum(Y==i) for i in range(1,35)]

from sklearn.naive_bayes import BernoulliNB

clf = BernoulliNB()
clf.fit(X, Y)
# BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)
# print X[6:800]


print len([i for i, j in zip(clf.predict(X), Y) if i == j])
