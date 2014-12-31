__author__ = 'srv'
#Name: Sarvesh Sadhoo
#UTA ID: 1000980763
import Orange

#Input training data to the classifier
titanic_training = Orange.data.Table("outputTraining.csv")
#Input test data to the classifier
titanic_test = Orange.data.Table("outputTest.csv")

# Instantiate a learner
learner = Orange.classification.bayes.NaiveLearner()
# Input the training data table into learner to create a classsifer
classifier = learner(titanic_training)

print classifier
print "Classification Values:"

# Count the classifying class value
classify_count = {}

for inst in titanic_test[0:]:
    print inst, classifier(inst)
    cls = str(classifier(inst))

    if cls not in classify_count:
        classify_count[cls] = 1
    elif cls in classify_count:
        classify_count[cls] += 1

print classify_count