from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_recall_fscore_support

# Wczytanie danych treningowych
training_data = []
training_labels = []
languages = ["english", "finnish", "german", "italian", "polish", "spanish"]

for language in languages:
    with open("data/{}.txt".format(language), "r", encoding="ISO-8859-1") as f:
        lines = f.readlines()
        training_data += lines
        training_labels += [language] * len(lines)



# Zamiana tekstu na reprezentację n-gramową (n=3)
vectorizer = CountVectorizer(ngram_range=(1, 3))
X = vectorizer.fit_transform(training_data)

# Tworzenie klasyfikatorów
naive_bayes = MultinomialNB()
svm = SVC()
decision_tree = DecisionTreeClassifier()

# Trenowanie klasyfikatorów na danych treningowych
naive_bayes.fit(X, training_labels)
svm.fit(X, training_labels)
decision_tree.fit(X, training_labels)

# Wczytanie danych testowych
test_data = []
test_labels = []
for language in languages:
    with open("data/{}.txt".format(language), "r", encoding="ISO-8859-1") as f:
        lines = f.readlines()
        test_data += lines
        test_labels += [language] * len(lines)

# Zamiana tekstu na reprezentację n-gramową (n=3)
X_test = vectorizer.transform(test_data)

# Testowanie klasyfikatorów na danych testowych
naive_bayes_predictions = naive_bayes.predict(X_test)
svm_predictions = svm.predict(X_test)
decision_tree_predictions = decision_tree.predict(X_test)

# Obliczanie wyników (precision, recall, f1, accuracy) dla każdego klasyfikatora
naive_bayes_results = precision_recall_fscore_support(test_labels, naive_bayes_predictions, average="weighted")
svm_results = precision_recall_fscore_support(test_labels, svm_predictions, average="weighted")
decision_tree_results = precision_recall_fscore_support(test_labels, decision_tree_predictions, average="weighted")

print("Naive Bayes Results:")
print("Precision: ", naive_bayes_results[0])
print("Recall: ", naive_bayes_results[1])
print("F1 Score: ", naive_bayes_results[2])
print("Accuracy: ", naive_bayes_results[3])

print("SVM Results:")
print("Precision: ", svm_results[0])
print("Recall: ", svm_results[1])
print("F1 Score: ", svm_results[2])
print("Accuracy: ", svm_results[3])

print("Decision Tree Results:")
print("Precision: ", decision_tree_results[0])
print("Recall: ", decision_tree_results[1])
print("F1 Score: ", decision_tree_results[2])
print("Accuracy: ", decision_tree_results[3])