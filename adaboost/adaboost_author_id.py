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

#########################################################
### your code goes here ###

from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

clf = AdaBoostClassifier(tree.DecisionTreeClassifier(min_samples_split=40),
                         n_estimators=600,learning_rate=1,algorithm='SAMME.R')

clf.fit(features_train, labels_train)

pre = clf.predict(features_test)


print (accuracy_score(pre, labels_test))


#accuracy:0.996587030717
#########################################################
