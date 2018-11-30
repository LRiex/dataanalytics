import numpy as np
import pandas as pd
import random
dfMain = pd.read_csv("Sample_Crimes3.csv")
# print dfMain.head(3) #prints 3 heading rows

# df = pd.read_csv("DayofWeek.csv")

# for index in range(0, len(df.values)):
# dfMain.loc[dfMain["LocationDescription"] == Nan, "LocationDescription"] = 1

# dfMain.to_csv("Sample_Crimes.csv", index=False)

# print dfMain.values[206]

indexing = random.sample(range(0, 20000), 1000)

X = dfMain.values[indexing, 0:568]
Y = dfMain.values[indexing, 568]
# print [sum(Y==i) for i in range(1,35)]


# X = [list(element) for element in list(X)]
# X = [list(map(float, element)) for element in X]
# Y = list(map(float, Y))

# print X
# print Y

from sklearn.naive_bayes import BernoulliNB
from sklearn import svm
lin_clf = svm.LinearSVC()

# clf = BernoulliNB()
lin_clf.fit(X, Y)
# BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)
# print X[6:800]
print Y
print lin_clf.predict(X)

print lin_clf.decision_function

print len([i for i, j in zip(lin_clf.predict(X), Y) if i == j])

