import json
import re
import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("tesco_sample.json", "r", encoding="utf-8") as file:
    products = json.load(file)

names = [product["name"] for product in products]
descriptions = [product["description"] for product in products]
print("Numar de produse:", len(products))

# procesare texte 
def preprocess_text(text):
    text = BeautifulSoup(text, "html.parser").get_text(
        separator=" ", strip=True
    )

    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    return text

clean_descriptions = [
    preprocess_text(text) for text in descriptions
]

# vectorizare TD-IDF
tfidf = TfidfVectorizer(stop_words="english")
response = tfidf.fit_transform(clean_descriptions)
print("Numar de termeni unici:", len(tfidf.vocabulary_))

# calculare matrice cosine similarity
similarity_matrix = cosine_similarity(response)
print("Dimensiunea matricei:", similarity_matrix.shape)
print(similarity_matrix)

# salvarea matrice intr-un fisier CSV
df = pd.DataFrame(
    similarity_matrix,
    index=names,
    columns=names
)
df.to_csv("similarity_matrix.csv")

# identificarea perechi de produse distincte 
pairs = []

for i in range(len(products)):
    for j in range(i + 1, len(products)):
        if names[i] != names[j]:
            pairs.append((similarity_matrix[i, j], i, j))

# sortarea descrescatoare dupa similaritate
pairs.sort(reverse=True)
seen_pairs = set() # pentru evitarea afisarii perechilor duplicate
count = 0

print("\nTop 10 perechi de produse similare:")
for score, i, j in pairs:
    pair = tuple(sorted([names[i], names[j]]))

    if pair in seen_pairs:
        continue

    seen_pairs.add(pair)
    count += 1

    print(f"\nPerechea {count}")
    print("Produs 1:", names[i])
    print("Produs 2:", names[j])
    print(f"Cosine Similarity: {score:.4f}")

    if count == 10:
        break
