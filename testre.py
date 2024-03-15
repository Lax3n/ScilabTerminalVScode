import re

# Exemple de chaîne de caractères contenant le slotHash
text = '{"slotHash": "454762233", "autreAttribut": "valeur"}'

# Expression régulière pour trouver le slotHash
pattern = r'"slotHash":\s*"(\d+)"'

# Recherche dans la chaîne de caractères
match = re.search(pattern, text)

if match:
    slotHash_code = match.group(1)
    print(f"Code slotHash trouvé : {slotHash_code}")
else:
    print("slotHash non trouvé.")