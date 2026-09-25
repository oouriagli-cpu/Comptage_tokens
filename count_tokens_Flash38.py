import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
cle = os.environ.get("GEMINI_API_KEY", "").strip()
client = genai.Client(api_key=cle)

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

# Sélection du modèle Gemini récent 
selected_model = "gemini-3.8-flash"

print(f"=== Étape 1 : Comptage des tokens par fichier avec le modèle Gemini '{selected_model}' ===\n")

total_tokens_count = 0

for file_path, content in file_contents.items():
    if content:
        try:
            response = client.models.count_tokens(
                model=selected_model,
                contents=content
            )
            tokens = response.total_tokens
            total_tokens_count += tokens
            print(f"-> {file_path} : {tokens} tokens.")
        except Exception as e:
            print(f"Erreur lors du comptage des tokens pour '{file_path}' : {e}\n")

print("\n" + "=" * 50)
print(f"TOTAL GEMINI ({selected_model}) : {total_tokens_count} tokens d'entrée cumulés.")
print("=" * 50)
