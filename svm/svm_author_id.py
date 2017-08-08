#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print (type(features_train[0][0]))
print (type(labels_test[10]))

#########################################################
### your code goes here ###
from sklearn.svm import SVC
t0 = time()
model = SVC()

model.fit(features_train, labels_train)
print ("training time:", round(time()-t0, 3), "s")
t1 = time()
pre = model.predict(features_test)
print ("pre time:", round(time()-t1, 3), "s")

from sklearn.metrics import accuracy_score
print(accuracy_score(pre, labels_test))
#########################################################
