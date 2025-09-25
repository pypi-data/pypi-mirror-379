def disp() -> str:
    return """
    disp_1 - Simplified ML Model using Scikit-Learn
    disp_2 - S-Find
    disp_3 - PCA Annova
    disp_4 - Candidate Elimination
    disp_5 - Naive Baise Classifer
    disp_6 - Decision Tree
    disp_7 - Least Square Regression
    disp_8 - Logistic Regression
    disp_9 - ID3 Decision Tree
    disp_10 - KNN
    disp_11 - KNN with diffrent Distance Methods
    disp_12 - KMeans
    disp_13 - Hierarchal Model
    disp_14 - Rule Based
    disp_15 - Basiyen Method
    disp_16 - Non Paramentric Locally Weighted Regression
    """


def disp_1() -> None:
    print(
        """import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

print("Testing scikit-learn Logistic Regression...")

np.random.seed(42)
X = np.random.randn(100, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

sk_model = LogisticRegression()
sk_model.fit(X_train, y_train)

predictions_sk = sk_model.predict(X_test)
accuracy_sk = accuracy_score(y_test, predictions_sk)

print(f"Scikit-learn Logistic Regression Accuracy: {accuracy_sk:.2f}")
print("Weights:", sk_model.coef_)
print("Bias:", sk_model.intercept_)"""
    )


def disp_2() -> None:
    print(
        """import pandas as pd

data = [
    ['A',5,8,8.5],
    ['B',5,10,8.8],
    ['C',2,12,3],
    ['D',3,8,5]
]

cols = ['Name','Stduy_hour','Sleep_hour','CGPA']

df = pd.DataFrame(data,columns=cols)

print(df)

def find_s(df,target_column):
    specific_hypothesis = None
    for index,row in df.iterrows():
        if row[target_column] >= 6.0:
            attributes = row.drop(target_column).tolist()
            if specific_hypothesis is None:
                specific_hypothesis = attributes
            else:
                for i in range(len(specific_hypothesis)):
                    if specific_hypothesis[i] != attributes[i]:
                        specific_hypothesis[i] = '?'
    return specific_hypothesis

h = find_s(df, 'CGPA')
print("Final hypothesis (Find-S):", h)"""
    )


def disp_3() -> None:
    print(
        """from sklearn.datasets import load_breast_cancer
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

breast_cancer = load_breast_cancer()
X_bc = breast_cancer.data
y_bc = breast_cancer.target
feature_names = breast_cancer.feature_names

df_bc = pd.DataFrame(X_bc, columns=feature_names)
df_bc['target'] = y_bc

correlation_with_target = df_bc.corr()['target'].sort_values(ascending=False)
print("Correlation with Target:")
print(correlation_with_target)

print("\\nANOVA Test Results (Breast Cancer Dataset):")
anova_results = {}
for feature in feature_names:
    group1 = df_bc[feature][df_bc['target'] == 0]
    group2 = df_bc[feature][df_bc['target'] == 1]
    f_value, p_value = stats.f_oneway(group1, group2)
    anova_results[feature] = {'F-value': f_value, 'P-value': p_value}

anova_df = pd.DataFrame(anova_results).T
print(anova_df)

anova_df_sorted = anova_df.sort_values(by='P-value', ascending=True)
plt.figure(figsize=(12, 8))
sns.barplot(x=anova_df_sorted.index, y=anova_df_sorted['P-value'])
plt.xticks(rotation=90)
plt.ylabel('P-value')
plt.title('ANOVA P-values for Breast Cancer Features')
plt.tight_layout()
plt.show()

top_features = correlation_with_target.head(11).index.tolist()

plt.figure(figsize=(10, 8))
sns.heatmap(df_bc[top_features].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Top Features with Target')
plt.show()"""
    )


def disp_4() -> None:
    print(
        """import pandas as pd

def candidate_elimination(df):
    n_attrs = df.shape[1] - 1
    S = [['0'] * n_attrs]
    G = [['?'] * n_attrs]

    print("Initial: S =", S[0], "G =", G[0])

    for idx, row in df.iterrows():
        attrs = list(row.iloc[:-1])
        label = row.iloc[-1]

        if label == 'Yes':
            G = [g for g in G if all(g_attr == '?' or g_attr == a_attr
                                     for g_attr, a_attr in zip(g, attrs))]
            for s_idx, s in enumerate(S):
                new_s = s.copy()
                for i in range(n_attrs):
                    if new_s[i] == '0':
                        new_s[i] = attrs[i]
                    elif new_s[i] != attrs[i]:
                        new_s[i] = '?'
                S[s_idx] = new_s
        else:
            S = [s for s in S if any(s_attr != '?' and s_attr != a_attr
                                     for s_attr, a_attr in zip(s, attrs))]
            new_G = []
            for g in G:
                if all(g_attr == '?' or g_attr == a_attr for g_attr, a_attr in zip(g, attrs)):
                    for i in range(n_attrs):
                        if g[i] == '?':
                            if S and S[0][i] != '?':
                                new_g = g.copy()
                                new_g[i] = S[0][i]
                                if new_g not in new_G:
                                    new_G.append(new_g)
                            elif g[i] == '?':
                                new_g = g.copy()
                                new_g[i] = attrs[i]
                                if new_g not in new_G:
                                    new_G.append(new_g)
                else:
                    if g not in new_G:
                        new_G.append(g)
            G = new_G

        print(f"After ex {idx+1}: S = {S[0]}, G = {G}")

    return S, G

data = {
    'Sky': ['Sunny', 'Sunny', 'Rainy'],
    'Temp': ['Warm', 'Warm', 'Cold'],
    'Humidity': ['Normal', 'High', 'High'],
    'EnjoySport': ['Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)
print("Dataset:\\n", df, "\\n")

S, G = candidate_elimination(df)
print("\\nFinal: S =", S[0], "G =", G)"""
    )


def disp_5() -> None:
    print(
        """import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

wine = load_wine(as_frame=True)
df = wine.frame
df['target'] = wine.target
df.to_csv("wine.csv", index=False)

data = pd.read_csv("wine.csv")

X = data[wine.feature_names]
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

nb = GaussianNB()
nb.fit(X_train, y_train)

y_pred = nb.predict(X_test)

print("Naïve Bayes Results:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\\nConfusion Matrix:\\n", confusion_matrix(y_test, y_pred))
print("\\nClassification Report:\\n", classification_report(y_test, y_pred, target_names=wine.target_names))

plt.figure(figsize=(6,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d",
            xticklabels=wine.target_names, yticklabels=wine.target_names, cmap="Blues")
plt.title("Naïve Bayes Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

new_samples = [
    [13.0, 2.0, 2.5, 20.0, 100.0, 2.8, 3.0, 0.3, 2.0, 5.0, 1.0, 3.0, 1000.0],
    [14.0, 4.0, 2.8, 22.0, 90.0, 2.0, 2.5, 0.4, 1.8, 4.0, 0.8, 2.8, 1200.0],
    [12.0, 1.5, 2.0, 18.0, 80.0, 1.8, 2.0, 0.2, 1.5, 3.0, 0.7, 2.5, 900.0]
]

predictions = nb.predict(new_samples)
for sample, pred in zip(new_samples, predictions):
    print(f"\\nNew Sample {sample} -> Predicted Class: {wine.target_names[pred]}")"""
    )


def disp_6() -> None:
    print(
        """import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

wine = load_wine()
X = wine.data
y = wine.target
feature_names = wine.feature_names
target_names = wine.target_names

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

dt_clf = DecisionTreeClassifier(criterion="entropy", random_state=42)
dt_clf.fit(X_train, y_train)

y_pred_dt = dt_clf.predict(X_test)

print("Decision Tree Results:")
print("Accuracy:", accuracy_score(y_test, y_pred_dt))
print("Confusion Matrix:\\n", confusion_matrix(y_test, y_pred_dt))
print("Classification Report:\\n", classification_report(y_test, y_pred_dt, target_names=target_names))

plt.figure(figsize=(6,4))
sns.heatmap(confusion_matrix(y_test, y_pred_dt), annot=True, fmt="d",
            xticklabels=target_names, yticklabels=target_names, cmap="Blues")
plt.title("Decision Tree Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

rf_clf = RandomForestClassifier(n_estimators=100, criterion="entropy", random_state=42)
rf_clf.fit(X_train, y_train)

y_pred_rf = rf_clf.predict(X_test)

print("\\nRandom Forest Results:")
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print("Confusion Matrix:\\n", confusion_matrix(y_test, y_pred_rf))
print("Classification Report:\\n", classification_report(y_test, y_pred_rf, target_names=target_names))

plt.figure(figsize=(6,4))
sns.heatmap(confusion_matrix(y_test, y_pred_rf), annot=True, fmt="d",
            xticklabels=target_names, yticklabels=target_names, cmap="Greens")
plt.title("Random Forest Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

new_sample = [[13.0, 2.0, 2.5, 20.0, 100.0, 2.8, 3.0, 0.3, 2.0, 5.0, 1.0, 3.0, 1000.0]]
dt_pred = dt_clf.predict(new_sample)[0]
rf_pred = rf_clf.predict(new_sample)[0]

print("\\nNew Sample:", new_sample)
print("Decision Tree Prediction:", target_names[dt_pred])
print("Random Forest Prediction:", target_names[rf_pred])"""
    )


def disp_7() -> None:
    print(
        """import pandas as pd
import numpy as np

x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([3, 5, 7, 9, 11], dtype=float)

m = 0.25
b = 0
learning_rate = 0.01

def prediction(m, b, x):
    return m * x + b

def loss(m, b, x, y):
    return np.mean((y - (m * x + b)) ** 2)

def gradient_descent_step(x, y, m, b, learning_rate):
    m_gradient = -2 * np.mean(x * (y - (m * x + b)))
    b_gradient = -2 * np.mean(y - (m * x + b))
    m = m - learning_rate * m_gradient
    b = b - learning_rate * b_gradient
    return m, b

epochs = 1000
for i in range(epochs):
    m, b = gradient_descent_step(x, y, m, b, learning_rate)
    if i % 200 == 0:
        print(f"Epoch {i}: Loss = {loss(m, b, x, y)}")

print("Final Model: ")
print(f"m = {m}, b = {b}")
print(f"Prediction for x = 8: y = {prediction(m, b, 8)}")"""
    )


def disp_8() -> None:
    print(
        """import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

wine = load_wine(as_frame=True)
df = wine.frame
df['target'] = wine.target
df.to_csv("wine.csv", index=False)

data = pd.read_csv("wine.csv")

X = data[wine.feature_names]
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

log_reg = LogisticRegression(max_iter=200, multi_class="multinomial", solver="lbfgs")
log_reg.fit(X_train, y_train)

y_pred = log_reg.predict(X_test)

print("Logistic Regression Results:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\\n", classification_report(y_test, y_pred, target_names=wine.target_names))

plt.figure(figsize=(6,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d",
            xticklabels=wine.target_names, yticklabels=wine.target_names, cmap="Oranges")
plt.title("Logistic Regression Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

new_sample = [[13.0, 2.0, 2.5, 20.0, 100.0, 2.8, 3.0, 0.3, 2.0, 5.0, 1.0, 3.0, 1000.0]]
pred_class = log_reg.predict(new_sample)[0]

print("\\nNew Sample:", new_sample)
print("Logistic Regression Prediction:", wine.target_names[pred_class])"""
    )


def disp_9() -> None:
    print(
        """import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, plot_tree

wine = load_wine()
X = wine.data
y = wine.target
feature_names = wine.feature_names
target_names = wine.target_names

clf = DecisionTreeClassifier(criterion="entropy", random_state=0)
clf.fit(X, y)

plt.figure(figsize=(12,8))
plot_tree(clf, feature_names=feature_names, class_names=target_names,
          filled=True, rounded=True)
plt.title("Decision Tree for Wine (ID3 style)")
plt.show()

X_plot = X[:, [0, 1]]

plt.figure(figsize=(8,6))
for i, label in enumerate(target_names):
    plt.scatter(X_plot[y==i, 0], X_plot[y==i, 1], label=label)

new_sample = [[13.0, 2.0, 2.5, 20.0, 100.0, 2.8, 3.0, 0.3, 2.0, 5.0, 1.0, 3.0, 1000.0]]
new_sample_plot = [new_sample[0][0], new_sample[0][1]]
predicted_class = clf.predict(new_sample)[0]

plt.scatter(new_sample_plot[0], new_sample_plot[1],
            color="black", marker="X", s=200,
            label=f"New Sample → {target_names[predicted_class]}")

plt.xlabel("Alcohol")
plt.ylabel("Malic Acid")
plt.title("Wine Dataset with New Sample")
plt.legend()
plt.show()"""
    )


def disp_10() -> None:
    print(
        """import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

wine = datasets.load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['TARGET CLASS'] = wine.target

scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis=1))
scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))
df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])

X_train, X_test, y_train, y_test = train_test_split(scaled_features, df['TARGET CLASS'], test_size=0.3, random_state=42)

knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
print("Predictions:", pred)

print("\\nConfusion Matrix:")
print(confusion_matrix(y_test, pred))
print("\\nClassification Report:")
print(classification_report(y_test, pred))

error_rate = []

for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,40), error_rate, color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)
plt.title('Error Rate vs K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()"""
    )


def disp_11() -> None:
    print(
        """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

wine = load_wine()
X = wine.data[:, :2]
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

k = 3
distance_metrics = ['euclidean', 'manhattan', 'chebyshev']

fig, axes = plt.subplots(1, len(distance_metrics), figsize=(15, 5))
for i, metric in enumerate(distance_metrics):
    knn_classifier = KNeighborsClassifier(n_neighbors=k, metric=metric)
    knn_classifier.fit(X_train, y_train)
    y_pred = knn_classifier.predict(X_test)

    print(f"Distance Metric: {metric}")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("\\n")

    ax = axes[i]
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='viridis', label='Training Data')
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='viridis', marker='x', s=100, label='Testing Data')

    knn_classifier = KNeighborsClassifier(n_neighbors=k, metric=metric)
    knn_classifier.fit(X, y)
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
    Z = knn_classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap='viridis', alpha=0.5, levels=range(4))
    ax.set_title(f'K-NN ({metric.capitalize()} Metric)')
    ax.set_xlabel('Alcohol')
    ax.set_ylabel('Malic Acid')
    ax.legend()
plt.show()"""
    )


def disp_12() -> None:
    print(
        """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.datasets import load_wine

x, y = load_wine(return_X_y=True)

kmeans = KMeans(n_clusters=3, random_state=40, n_init=10)
kmeans.fit(x)

kmeans_labels = kmeans.labels_
centroids = kmeans.cluster_centers_
print("Kmeans labels ", kmeans_labels)
print("Centroids ", centroids)

plt.scatter(x[:, 0], x[:, 1], c=kmeans_labels, cmap='viridis', marker="o", label='Clustered Data')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200, label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('Alcohol')
plt.ylabel('Malic Acid')
plt.legend()
plt.show()

plt.scatter(x[:, 0], x[:, 1], c=y, cmap='viridis', marker="o", label='Ground Truth')
plt.title('Ground Truth Labels')
plt.xlabel('Alcohol')
plt.ylabel('Malic Acid')
plt.legend()
plt.show()"""
    )


def disp_13() -> None:
    print(
        """from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

X, y = make_blobs(n_samples=500, centers=4, random_state=42)

linkage_methods = linkage(X, method='ward')

plt.figure(figsize=(12,6))
dendrogram(linkage_methods)
plt.title('Hierarchical Clustering Dendogram')
plt.xlabel('Sample index')
plt.ylabel('Distance')
plt.show()"""
    )


def disp_14() -> None:
    print(
        """import pandas as pd
from sklearn.datasets import load_wine

wine = load_wine(as_frame=True)

df = wine.frame
df['species'] = df['target'].map({0: 'class_0', 1: 'class_1', 2: 'class_2'})

def discover_subgroup(data, condition, label_col="species"):
    subgroup = data.query(condition)
    return {
        "Condition": condition,
        "Subgroup Size": len(subgroup),
        "Distribution": subgroup[label_col].value_counts().to_dict()
    }

rules = [
    "`alcohol` > 13",
    "`malic_acid` < 2",
    "`alcohol` > 13 and `proanthocyanins` > 2"
]

results = [discover_subgroup(df, rule) for rule in rules]
print(pd.DataFrame(results))"""
    )


def disp_15() -> None:
    print(
        """import pandas as pd
import numpy as np
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=8,
    n_redundant=2,
    random_state=42,
    n_clusters_per_class=1
)

feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak']
data = pd.DataFrame(X, columns=feature_names)

data['age'] = np.round(30 + data['age'] * 20)
data['sex'] = (data['sex'] > 0).astype(int)
data['trestbps'] = np.round(90 + data['trestbps'] * 60)
data['chol'] = np.round(150 + data['chol'] * 150)
data['fbs'] = (data['fbs'] > 0.5).astype(int)
data['heart_disease'] = y

print("Sample of Synthetic Heart Disease Dataset:")
print(data.head())
print(f"\\nDataset shape: {data.shape}")
print(f"\\nHeart disease distribution:\\n{data['heart_disease'].value_counts()}")

p_hd = data['heart_disease'].value_counts(normalize=True)
print("\\nPrior Probability P(Heart Disease):")
print(p_hd)

p_hd_given_sex = (
    data.groupby(['sex', 'heart_disease']).size().unstack().fillna(0)
)
p_hd_given_sex = p_hd_given_sex.div(p_hd_given_sex.sum(axis=1), axis=0)
print("\\nConditional Probability P(Heart Disease | Sex):")
print(p_hd_given_sex)

data['bp_level'] = pd.cut(data['trestbps'], bins=[0, 120, 140, 200], labels=['low', 'normal', 'high'])
p_hd_given_bp = (
    data.groupby(['bp_level', 'heart_disease']).size().unstack().fillna(0)
)
p_hd_given_bp = p_hd_given_bp.div(p_hd_given_bp.sum(axis=1), axis=0)
print("\\nConditional Probability P(Heart Disease | BP level):")
print(p_hd_given_bp)

data['chol_level'] = pd.cut(data['chol'], bins=[0, 200, 240, 300], labels=['normal', 'borderline', 'high'])
p_hd_given_chol = (
    data.groupby(['chol_level', 'heart_disease']).size().unstack().fillna(0)
)
p_hd_given_chol = p_hd_given_chol.div(p_hd_given_chol.sum(axis=1), axis=0)
print("\\nConditional Probability P(Heart Disease | Cholesterol level):")
print(p_hd_given_chol)

def predict_heart_disease(sex, bp, chol):
    bp_level = pd.cut([bp], bins=[0, 120, 140, 200], labels=['low', 'normal', 'high'])[0]
    chol_level = pd.cut([chol], bins=[0, 200, 240, 300], labels=['normal', 'borderline', 'high'])[0]

    probs = {}
    for hd in [0, 1]:
        prior = p_hd.loc[hd]
        p_sex = p_hd_given_sex.loc[sex, hd] if sex in p_hd_given_sex.index else 1
        p_bp = p_hd_given_bp.loc[bp_level, hd] if bp_level in p_hd_given_bp.index else 1
        p_chol = p_hd_given_chol.loc[chol_level, hd] if chol_level in p_hd_given_chol.index else 1
        probs[hd] = prior * p_sex * p_bp * p_chol

    total = sum(probs.values())
    for hd in probs:
        probs[hd] /= total

    prediction = max(probs, key=probs.get)
    return prediction, probs

test_patients = [
    {"sex": 1, "bp": 138, "chol": 250},
    {"sex": 0, "bp": 110, "chol": 180},
    {"sex": 1, "bp": 160, "chol": 280},
    {"sex": 0, "bp": 130, "chol": 220}
]

print("\\n" + "="*60)
print("NAIVE BAYES HEART DISEASE PREDICTIONS")
print("="*60)

for i, patient in enumerate(test_patients, 1):
    pred, probs = predict_heart_disease(**patient)
    print(f"\\nPatient {i}:")
    print(f"  Sex: {'Male' if patient['sex'] == 1 else 'Female'}")
    print(f"  BP: {patient['bp']} mmHg ({pd.cut([patient['bp']], bins=[0, 120, 140, 200], labels=['low', 'normal', 'high'])[0]})")
    print(f"  Cholesterol: {patient['chol']} mg/dL ({pd.cut([patient['chol']], bins=[0, 200, 240, 300], labels=['normal', 'borderline', 'high'])[0]})")
    print(f"  Prediction: {'HEART DISEASE' if pred == 1 else 'NO HEART DISEASE'}")
    print(f"  Probability (No Disease): {probs[0]:.3f}")
    print(f"  Probability (Disease): {probs[1]:.3f}")

print("\\n" + "="*60)
print("EVALUATION ON TRAINING DATA")
print("="*60)

correct_predictions = 0
total_predictions = len(data)

for idx, row in data.iterrows():
    pred, _ = predict_heart_disease(row['sex'], row['trestbps'], row['chol'])
    if pred == row['heart_disease']:
        correct_predictions += 1

accuracy = correct_predictions / total_predictions
print(f"Accuracy on training data: {accuracy:.3f}")
print(f"Correct predictions: {correct_predictions}/{total_predictions}")

print("\\n" + "="*60)
print("ADDITIONAL ANALYSIS")
print("="*60)

print("\\nBlood Pressure Distribution:")
print(data['bp_level'].value_counts())

print("\\nCholesterol Distribution:")
print(data['chol_level'].value_counts())

print("\\nSex Distribution:")
print(data['sex'].value_counts()"""
    )


def disp_16() -> None:
    print(
        """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def locally_weighted_regression_demo():
    np.random.seed(42)
    X = np.sort(5 * np.random.rand(100, 1), axis=0)
    y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])

    def locally_weighted_regression(X_train, y_train, x_query, tau=0.5):
        X_train_b = np.c_[np.ones(len(X_train)), X_train]
        x_query_b = np.array([1, x_query])
        weights = np.exp(-(X_train - x_query)**2 / (2 * tau**2))
        W = np.diag(weights.ravel())
        theta = np.linalg.pinv(X_train_b.T @ W @ X_train_b) @ X_train_b.T @ W @ y_train
        return theta @ x_query_b

    X_test = np.linspace(0, 5, 100)
    y_pred = [locally_weighted_regression(X, y, x_i, tau=0.5) for x_i in X_test]

    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='blue', alpha=0.5, label='Data')
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='LWR Prediction')
    plt.plot(X_test, np.sin(X_test), color='green', linewidth=2, label='True Function')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Locally Weighted Regression')
    plt.legend()
    plt.show()

    lr_model = LinearRegression()
    lr_model.fit(X, y)
    y_pred_lr = lr_model.predict(X_test.reshape(-1, 1))

    mse_lwr = mean_squared_error(np.sin(X_test), y_pred)
    mse_lr = mean_squared_error(np.sin(X_test), y_pred_lr)

    print(f"LWR MSE: {mse_lwr:.4f}")
    print(f"Linear Regression MSE: {mse_lr:.4f}")

    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='blue', alpha=0.5, label='Data')
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='LWR Prediction')
    plt.plot(X_test, y_pred_lr, color='orange', linewidth=2, label='Linear Regression')
    plt.plot(X_test, np.sin(X_test), color='green', linewidth=2, label='True Function')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Comparison: LWR vs Linear Regression')
    plt.legend()
    plt.show()

    return y_pred, mse_lwr, mse_lr

locally_weighted_regression_demo()"""
    )
