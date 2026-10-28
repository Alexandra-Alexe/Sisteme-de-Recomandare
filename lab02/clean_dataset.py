import pandas as pd

# Căile către fișiere
PATH_ORIGINAL = '../movies_updated.csv'
PATH_CLEAN = '../movies_clean.csv'

def clean_dataset():
    # 1. Citim dataset-ul original
    df = pd.read_csv(PATH_ORIGINAL)
    
    # 2. Păstrăm doar cele 5 coloane dorite
    columns_to_keep = ['name', 'genre', 'score', 'director', 'year']
    df = df[columns_to_keep].copy()
    
    # 3. Ne asigurăm că eliminăm rândurile care nu au nume
    df = df.dropna(subset=['name'])
    
    # 4. Generăm un ID numeric unic ca string (ex: '1', '2', '3'...) pentru item_id
    # Recombee cere ca itemId să fie de tip string, chiar dacă conține cifre
    df['item_id'] = [str(i) for i in range(1, len(df) + 1)]
    
    # Reordonăm coloanele astfel încât item_id să fie prima coloană (opțional, dar arată mai bine)
    cols = ['item_id'] + [col for col in df.columns if col != 'item_id']
    df = df[cols]
    
    # 5. Salvăm noul fișier CSV curat
    df.to_csv(PATH_CLEAN, index=False)
    print(f"Dataset-ul curat cu ID-uri numerice a fost salvat în '{PATH_CLEAN}' și conține {len(df)} rânduri.")

if __name__ == "__main__":
    clean_dataset()