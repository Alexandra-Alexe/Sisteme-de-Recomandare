import pandas as pd
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import SetItemValues, Batch, AddItem
from recombee_api_client.exceptions import APIException

# TODO 1: Configurare credentiale Recombee (la fel ca la Lab 02)
DB_NAME = 'alexe-alexandra-dev'
PRIVATE_TOKEN = 'G0LzytIxoaB0g3covHmafBDYoAdXwHgF7u8KTUphdEWmfu6FrqMkv9uEEJRia54S'
REGION = 'eu-west'  

client = RecombeeClient(DB_NAME, PRIVATE_TOKEN)

# TODO 2: Incarcarea aceluiasi dataset folosit la Lab 02
PATH_DATASET = '../movies_clean.csv' 

def send_items():
    """Functie care citeste dataset-ul si trimite item-urile in Recombee"""
    df = pd.read_csv(PATH_DATASET)

    print(f"Se trimit {len(df)} item-uri in Recombee...")
    
    requests = []
    
    for index, row in df.iterrows():
        # TODO 3: Extrageti ID-ul unic al produsului din coloana corespunzatoare din CSV
        item_id = str(row['item_id'])
        
        # TODO 4: Mapati proprietatile definite anterior cu valorile din randul curent
        # Exemplu:
        properties = {
            "name": str(row['name']),
            "genre": str(row['genre']),
            "score": float(row['score']) if pd.notna(row['score']) else 0.0,
            "director": str(row['director']) if pd.notna(row['director']) else "Unknown",
            "year": int(row['year']) if pd.notna(row['year']) else 0
        }
        
        # Adaugam request-ul de setare a valorilor pentru item
        # (SetItemValues creează automat item-ul dacă acesta nu există) Ba nu.
        requests.append(AddItem(item_id))
        requests.append(SetItemValues(item_id, properties))
        
       # Trimitem in loturi (batch) de cate 100 pentru eficienta
        if len(requests) == 100:
            try:
                response = client.send(Batch(requests))
                print(f"Lot de 100 trimis cu succes!")
            except APIException as e:
                print("Eroare la trimiterea lotului: {e}")
            
            requests = []
            
    # Trimitem si restul ramanase (daca numarul total nu e multiplu de 100)
    if requests:
        client.send(Batch(requests))
        print("S-a trimis ultimul lot de item-uri.")
        
    print("Toate item-urile au fost trimise cu succes!")

if __name__ == "__main__":
    send_items()
