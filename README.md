# my-colab-project
Part 1: Suitable Python Frameworks for This Dataset

pandas
📦 The most popular library for loading, processing, and analyzing tabular data such as CSV and Excel.
Example (used in this project):

import pandas as pd
df = pd.read_excel("filename.xlsx")


openpyxl / xlrd
📦 Libraries for directly reading Excel files. Often used as backends with pandas.
Example:

df = pd.read_excel("file.xlsx", engine="openpyxl")


matplotlib / seaborn
📊 Used for visualization and statistical plots (e.g., label distribution, sentence length, histograms, etc.).

scikit-learn
🤖 Provides machine learning and statistical analysis tools. Also supports text vectorization (TF-IDF, CountVectorizer, etc.).

NLTK / Hazm
📖 For Natural Language Processing (NLP).

NLTK: mainly for English (tokenization, POS tagging, stopword removal, etc.).

Hazm: specialized for Persian (normalization, stemming, tokenization).

🔹 Part 2: Exploratory Data Analysis (EDA)

Here is a complete EDA plan used in this project:

Check the number of samples per label

How many comments exist in each category.

Analyze text length

Number of words and characters in each comment.

Check for duplicates and missing values

Drop empty or repeated rows.

Visualizations

Distribution of labels (bar chart).

Distribution of text lengths (histogram/boxplot).

Preview a few samples

Inspect some comments with their labels for better understanding.

📊 Example EDA code (simplified):

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("filename.xlsx")

# 1. Label distribution
print(df['label'].value_counts())

plt.figure(figsize=(6,4))
sns.countplot(x="label", data=df, palette="Set2")
plt.title("Label Distribution")
plt.show()

# 2. Comment length analysis
df["word_count"] = df["comment"].apply(lambda x: len(str(x).split()))
df["char_count"] = df["comment"].apply(lambda x: len(str(x)))

plt.figure(figsize=(6,4))
sns.histplot(df["word_count"], bins=30, kde=True)
plt.title("Distribution of Comment Word Counts")
plt.show()

# 3. Check missing & duplicate values
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

# 4. Preview some samples
print(df.head(5))


Text Classification and Analysis on Persian Comments
📌 Project Overview

This project focuses on data preprocessing, exploratory analysis, and machine learning classification for Persian text data. The workflow includes cleaning raw comments, generating word clouds, training machine learning models, and evaluating results.

The main objective is to demonstrate how preprocessing and feature engineering affect the quality of text classification models.

⚙️ Features Implemented

Data Cleaning & Preprocessing

Removing punctuation, digits, and stopwords

Normalizing Persian text

Tokenization and stemming/lemmatization

Exploratory Data Analysis (EDA)

Word cloud for all comments

Word cloud for misclassified samples

Distribution of labels

Machine Learning Models

TF-IDF vectorization

Training a baseline classification model (Logistic Regression / SVM)

Evaluation with classification report & confusion matrix

Visualization

Heatmaps of confusion matrix

Bar plots of label distributions

Word clouds for frequent tokens

📊 Sample Results
1. Word Cloud of Frequent Words

(Generated using WordCloud library)

2. Confusion Matrix Example
           precision    recall  f1-score   support
label_0       0.82      0.85      0.83       200
label_1       0.78      0.74      0.76       180

3. Label Distribution

Visualized using bar charts to show class balance.

📂 Project Structure
├── data/                     # Raw and processed datasets
├── notebooks/                # Jupyter/Colab notebooks
├── outputs/                  # Word clouds, plots, and reports
├── main.ipynb                # Main analysis notebook
└── README.md                 # Project documentation

🚀 How to Run

Clone this repository:

git clone https://github.com/username/repo-name.git
cd repo-name


Install dependencies:

pip install -r requirements.txt


Open Jupyter/Colab and run:

jupyter notebook main.ipynb

🔮 Future Work

Try deep learning models (LSTMs, Transformers, BERT-based models)

Improve preprocessing with advanced Persian NLP tools

Hyperparameter tuning for better accuracy

👨‍💻 Author

Developed as part of a Persian text data analysis and classification project.
