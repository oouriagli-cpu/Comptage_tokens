import logging
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

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

print("=== Étape 1 : Récupération dynamique des modèles disponibles sur votre clé ===")
try:
    models_response = client.models.list()
    available_model_ids = [m.id for m in models_response.data]
    print(f"Modèles trouvés ({len(available_model_ids)}) :")
    for model_id in available_model_ids:
        print(f" - {model_id}")
    print()
except Exception as e:
    print(f"Erreur lors de la récupération des modèles : {e}\n")
    available_model_ids = []

# Forçage direct du modèle Opus 5
selected_model = "claude-opus-5"

print(f"=== Étape 2 : Comptage des tokens par fichier avec le modèle '{selected_model}' ===\n")

total_tokens_count = 0

for file_path, content in file_contents.items():
    if content:
        try:
            response = client.messages.count_tokens(
                model=selected_model,
                messages=[{"role": "user", "content": content}]
            )
            tokens = response.input_tokens
            total_tokens_count += tokens
            print(f"-> {file_path} : {tokens} tokens.")
        except Exception as e:
            print(f"Erreur lors du comptage des tokens pour '{file_path}' : {e}\n")

print("\n" + "=" * 50)
print(f"TOTAL ANTHROPIC ({selected_model}) : {total_tokens_count} tokens d'entrée cumulés.")
print("=" * 50)
