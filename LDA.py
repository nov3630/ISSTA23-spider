import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd
import numpy as np

abstract_subdir_files = os.listdir("abstract")


# Define a function to read a file and return its content
def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Read all the abstracts into a dictionary
abstract_dict = {}
for file_name in abstract_subdir_files:
    file_path = f"abstract/{file_name}"
    abstract_dict[file_name] = read_file_content(file_path)

# Preprocessing
n_features = 1000
n_top_words = 10

# Use tf-idf features for NMF.
print("Extracting tf-idf features for NMF...")
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=n_features, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(list(abstract_dict.values()))

# Use tf (raw term count) features for LDA.
print("Extracting tf features for LDA...")
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=n_features, stop_words='english')
tf = tf_vectorizer.fit_transform(list(abstract_dict.values()))

n_topics = 10

print("Fitting LDA models with tf features, n_samples=%d and n_features=%d..."
      % (len(abstract_dict), n_features))
lda = LatentDirichletAllocation(n_components=n_topics, max_iter=5, learning_method='online', learning_offset=50.,
                                random_state=0)
lda.fit(tf)


# Define function to print top words
def print_top_words(model, feature_names, n_top_words):
    top_words = {}
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
        top_words[topic_idx] = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
        print(message)
    print()
    return top_words


print("\nTopics in LDA model:")
tf_feature_names = tf_vectorizer.get_feature_names_out()
top_words = print_top_words(lda, tf_feature_names, n_top_words)

# Convert to DataFrame
df_top_words = pd.DataFrame(top_words)
print(df_top_words)
