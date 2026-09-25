import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"].strip()
)

# Liste des deux fichiers texte à traiter
file_paths = ["10000_prompts_fr.txt", "10000_prompts_en.txt"]
file_contents = {}

print("=== Étape 0 : Lecture complète des fichiers externes ===")
for file_path in file_paths:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            file_contents[file_path] = f.read()
        print(f"Fichier '{file_path}' chargé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la lecture de '{file_path}' : {e}")
        file_contents[file_path] = ""
print()

# Sélection du modèle OpenAI récent 
selected_model = "gpt-5.6-sol"

print(f"=== Étape 1 : Comptage des tokens par fichier avec le modèle OpenAI '{selected_model}' ===\n")

try:
    import tiktoken
    encoding = tiktoken.encoding_for_model(selected_model)
except Exception:
    encoding = tiktoken.get_encoding("cl100k_base")

total_tokens_count = 0

for file_path, content in file_contents.items():
    if content:
        try:
            tokens = len(encoding.encode(content))
            total_tokens_count += tokens
            print(f"-> {file_path} : {tokens} tokens.")
        except Exception as e:
            print(f"Erreur lors du comptage des tokens pour '{file_path}' : {e}\n")

print("\n" + "=" * 50)
print(f"TOTAL OPENAI ({selected_model}) : {total_tokens_count} tokens d'entrée cumulés.")
print("=" * 50)
