import os
import imagehash
from PIL import Image
from itertools import combinations

# Path to the Produzidas folder
produzidas_path = r"I:\My Drive\Backup Ativo\Trabalho\2026\IA Agents\BibleCover\Produzidas"

# Get all jpg files
jpg_files = [f for f in os.listdir(produzidas_path) if f.endswith('.jpg') and f.startswith('tapa-biblia_-')]

print(f"Total de arquivos para comparar: {len(jpg_files)}")

# Dictionary to store hashes
hashes = {}

# Calculate perceptual hash for each image
for filename in jpg_files:
    filepath = os.path.join(produzidas_path, filename)
    try:
        with Image.open(filepath) as img:
            # Use perceptual hash (phash)
            hash_value = imagehash.phash(img)
            hashes[filename] = hash_value
    except Exception as e:
        print(f"Erro ao processar {filename}: {e}")

print(f"Hashes calculados: {len(hashes)}")

# Compare all pairs and find similarities > 95%
similar_pairs = []
threshold = 0.05  # 95% similarity means 5% or less difference

for (file1, hash1), (file2, hash2) in combinations(hashes.items(), 2):
    # Calculate hamming distance
    distance = hash1 - hash2
    # Maximum distance for phash is 64 bits
    similarity = 1 - (distance / 64)
    
    if similarity > 0.95:
        similar_pairs.append((file1, file2, similarity * 100))

# Sort by similarity (highest first)
similar_pairs.sort(key=lambda x: x[2], reverse=True)

# Print results
if similar_pairs:
    print(f"\nEncontrados {len(similar_pairs)} pares com similaridade > 95%:")
    print("-" * 80)
    for file1, file2, similarity in similar_pairs:
        print(f"{similarity:.1f}% similar:")
        print(f"  - {file1}")
        print(f"  - {file2}")
        print()
else:
    print("\nNenhum par com similaridade > 95% encontrado.")

# Save results to file
with open(os.path.join(produzidas_path, "similar_images.txt"), "w", encoding="utf-8") as f:
    f.write("Análise de Similaridade de Imagens\n")
    f.write(f"Total de imagens analisadas: {len(hashes)}\n")
    f.write(f"Limiar: 95% de similaridade\n\n")
    
    if similar_pairs:
        f.write(f"Encontrados {len(similar_pairs)} pares com similaridade > 95%:\n")
        f.write("-" * 80 + "\n")
        for file1, file2, similarity in similar_pairs:
            f.write(f"{similarity:.1f}% similar:\n")
            f.write(f"  - {file1}\n")
            f.write(f"  - {file2}\n\n")
    else:
        f.write("Nenhum par com similaridade > 95% encontrado.\n")

print(f"\nResultados salvos em: {os.path.join(produzidas_path, 'similar_images.txt')}")