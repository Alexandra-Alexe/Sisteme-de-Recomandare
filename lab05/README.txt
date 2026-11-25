# Laborator 05 – Cosine Similarity

## 1. Dataset utilizat

Pentru acest laborator am utilizat fișierul `tesco_sample.json`, care conține 266 de produse din supermarketurile Tesco. Calculul similarității se bazează pe câmpul `description`, iar câmpul `name` este utilizat pentru identificarea produselor.

## 2. Implementare

Implementarea a fost realizată în Python, prin adaptarea tutorialului „Document Similarity Using Cosine Similarity”, oferit în cadrul laboratorului.

Etapele implementării sunt:

- Citirea produselor din fișierul JSON.
- Eliminarea tag-urilor HTML din descrieri.
- Transformarea textelor în litere mici.
- Eliminarea numerelor și a caracterelor speciale.
- Eliminarea cuvintelor comune din limba engleză (stopwords).
- Transformarea descrierilor în vectori numerici utilizând `TfidfVectorizer`.
- Calcularea matricei de similaritate utilizând `cosine_similarity`.
- Afișarea primelor 10 perechi distincte de produse, în ordinea descrescătoare a similarității.

## 3. Rezultate obținute

- Număr de produse: 266
- Număr de termeni unici după preprocesare: 3689
- Dimensiunea matricei de similaritate: 266 × 266

Matricea de similaritate este salvată în fișierul `similarity_matrix.csv`.

## 4. Exemplu de produse similare

Produs 1: Tesco Age 40 Balloons 6 Pack
Produs 2: Tesco Age 30 Balloons 6 Pack
Cosine Similarity: 1.0000

Cele două produse sunt seturi de câte șase baloane aniversare, având aceleași dimensiuni, caracteristici și instrucțiuni de siguranță. Principala diferență este vârsta imprimată pe baloane.

Deoarece numerele sunt eliminate în etapa de preprocesare, descrierile celor două produse devin identice, ceea ce justifică scorul maxim de similaritate.

## 5. Observații

În urma analizei rezultatelor, am observat că unele produse diferite, precum Tesco Microfibre Towel 220Gsm 70X70 și Tesco Funnel, obțin de asemenea un scor de similaritate de 1.0000.

Acest lucru se datorează faptului că descrierile lor conțin aceleași informații generice despre reciclare și adresa producătorului.
Prin urmare, metoda Cosine Similarity măsoară similaritatea dintre reprezentările vectoriale ale descrierilor, fără a garanta că produsele sunt similare din punct de vedere funcțional.
