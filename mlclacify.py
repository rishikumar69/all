from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


iris = datasets.load_iris()

features = iris.data
lables = iris.target

# print(features, lables)

clf = KNeighborsClassifier()
clf.fit(features, lables)
lst = []
for i in range(4):
    num = float(input(":"))
    lst.append(num)


pre = clf.predict([lst])
# print(iris.DESCR)

# - Iris-Setosa
# - Iris-Versicolour
# - Iris-Virginica

if pre == 0:
    print("Setosa")

elif pre == 1:
    print("Versicolour")

elif pre == 2:
    print("Virginica")

else:
    print("None")
