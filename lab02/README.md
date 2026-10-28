# Lab 02 - Recommender systems - Recombee

## 1. Descrierea Domeniului
Acest proiect utilizează un dataset din domeniul cinematografic preluat de pe Kaggle (`movies_updated.csv`), care conține informații despre filme, genuri, scoruri, anii de apariție și regizori.

## 2. Volumul Datelor
- **Număr de înregistrări:** 4000 de filme 
- **Link Kaggle:** https://www.kaggle.com/code/yousefsaeedian/movies-dataset-visualization/notebook
- Cu ajutorul fișierului 'clean_dataset.py' datele au fost curățate.

## 3. Proprietățile definite în Recombee
Conform schemei din scriptul Python, au fost configurate următoarele 5 proprietăți în Recombee:
- **`name`** (tip: `string`) - Titlul filmului.
- **`genre`** (tip: `string`) - Genul principal al filmului.
- **`score`** (tip: `double`) - Nota sau scorul obținut.
- **`director`** (tip: `string`) - Regizorul filmului.
- **`year`** (tip: `int`) - Anul apariției.
