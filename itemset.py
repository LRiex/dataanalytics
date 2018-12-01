import numpy as np
import pandas as pd
import random
dfMain = pd.read_csv("Sample_Crimes3.csv")
# print dfMain.head(3) #prints 3 heading rows

# df = pd.read_csv("DayofWeek.csv")

# for index in range(0, len(df.values)):
# dfMain.loc[dfMain["LocationDescription"] == Nan, "LocationDescription"] = 1

# dfMain.to_csv("Sample_Crimes.csv", index=False)
trainiSize = 18000

# print dfMain.values[206]

indexing = random.sample(range(0, 20000), trainiSize)

X_train = dfMain.values[indexing, 0:568]
Y_train = dfMain.values[indexing, 568]
# print [sum(Y==i) for i in range(1,35)]
# print Y_train

remaining = list(set(range(0, 20000)) - set(indexing))
X_test = dfMain.values[remaining, 0:568]
Y_test = dfMain.values[remaining, 568]

# X = [list(element) for element in list(X)]
# X = [list(map(float, element)) for element in X]
# Y = list(map(float, Y))
# print remaining
# print X_test
# print Y_test

from sklearn.naive_bayes import BernoulliNB
from sklearn import svm
lin_clf = svm.LinearSVC()

# lin_clf = BernoulliNB()
lin_clf.fit(X_train, Y_train)
# BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)
# print X[6:800]
# print Y
# print lin_clf.predict(X_test)

# print lin_clf.decision_function

print 'test accuracy: ' + str(len([i for i, j in zip(lin_clf.predict(X_test), Y_test) if i == j])/float(20000 - trainiSize))

print 'trainig accuracy: ' + str(len([i for i, j in zip(lin_clf.predict(X_train), Y_train) if i == j])/float(trainiSize))

import csv
RESULT = zip(remaining, list(lin_clf.predict(X_test)))
# print RESULT
RESULT = [list(elem) for elem in RESULT]
# print RESULT


with open("Sample_Crimes4.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(RESULT)



# with open("output.csv",'wb', newline = '') as resultFile:
#     wr = csv.writer(resultFile, dialect='excel')
#     wr.writerow(remaining)