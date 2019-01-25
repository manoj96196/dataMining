1. Basic Loops:
a. Write a for loop that prints the ASCII code of each character in a string named S.
(Hint: You may use the build-in function ord (character)). (2 marks)
b. Change the loop to compute the sum of the ASCII codes of all characters in a string.
(2 marks)
c. Modify your code to return a new list that contained the ASCII code of each character
in the string. (2 marks)
Submit your Python source codes in a single Python script file Question 1.
2.
a. What is the output of the following code and explain why? (2 marks)
X= 'HELLO'
def fun():
X='NI'
def nested():
print(X)
nested()
fun()
print(X)
b. Write an expression that changes the first item in a tuple. (4, 5, 6) should become
(1, 5, 6) in the process. (2 marks)
Part II (10 marks)
3. In this part, we are going to build a decision tree classifier with Orange3
programming to predict the acceptability of the room. The dataset can be found in
the CSV file assg1_room.csv. The first six columns and the last column are the
attributes of the rooms and the second last column is class label denoting the
evaluated room acceptability. The attribute information is shown in the following
table:
Attribute Description Possible values
Price Renting price vhigh, high, med, low
Bills Bills of gas, water, etc. vhigh, high, med, low
Tenants Number of tenants 2, 3, 4

Rooms Number of rooms 2, 4, more
Size Size of the room small, med, large
Furnished Furnished room Yes, No, N/A
Accept (class label) Acceptability of the room unacc, soso, good, vgood
Bathrooms Number of bathrooms 1, 2, 3
a. The values for attribute “Tenants” are missing for some tuples. Write a Python script to
read the input CSV file (assg1_room.csv), replace the missing values with the mean
value for that attribute, and then export the entire dataset to another CSV file. Remember
to keep all other attribute values unchanged. (Hint: You may need to check how your
data import and/or export functions handle missing values). (4 marks)
b. Using the data exported in part (a), create an Orange3 decision tree learner and perform
a 10-fold cross-validation to evaluate the performance of its decision tree classifier with
this data. The answer should include the followings:
i. Python source codes reading the source data, building the learner, and
performing 10-fold cross-validation. (2 marks)
ii. Accuracy and area under (receiver operating characteristic, ROC) curve
(AUC). Note: no marks will be given without answer for (i) (2 marks)
c. Since there are four class labels for this dataset, one claims that the number of leaf nodes
of the decision tree can be limited to four such that each leaf node represents a particular
class label. Is this correct? Justify your answer with both explanation and computational
demonstration. (2 marks)
