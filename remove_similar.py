import os

# Pares similares encontrados (extrair do similar_images.txt)
similar_pairs = [
    (39, 84), (41, 86), (61, 42), (72, 73), (97, 96), (97, 94), (97, 91),
    (96, 94), (96, 91), (94, 91), (99, 102), (1, 87), (25, 27), (26, 27),
    (62, 92), (48, 49), (48, 51), (49, 51), (51, 68), (52, 46), (52, 72),
    (52, 73), (52, 103), (54, 46), (54, 103), (45, 89), (46, 72), (46, 73),
    (46, 103), (92, 90)
]

# Regra: remover o de numeracao maior em cada par
files_to_remove = set()

for n1, n2 in similar_pairs:
    if n1 > n2:
        files_to_remove.add(n1)
    else:
        files_to_remove.add(n2)

# Ordenar para melhor visualização
files_to_remove = sorted(files_to_remove)

print("=" * 70)
print("ANÁLISE DE SIMILARES - ARQUIVOS A REMOVER")
print("=" * 70)

print("\nRegla: Remover el de numeración mayor en cada par similar\n")

print("Pares analizados y decisión:")
print("-" * 70)

for n1, n2 in sorted(similar_pairs):
    if n1 > n2:
        remove = n1
        keep = n2
    else:
        remove = n2
        keep = n1
    print(f"  Par ({n1}, {n2}) => Remover: {remove} | Manter: {keep}")

print("-" * 70)
print(f"\nTotal de arquivos a remover: {len(files_to_remove)}")
print(f"\nLista de arquivos para remover: {files_to_remove}")

# Gerar lista final
print("\n" + "=" * 70)
print("COMANDOS PARA REMOVER")
print("=" * 70)

produzidas_path = r"I:\My Drive\Backup Ativo\Trabalho\2026\IA Agents\BibleCover\Produzidas"

for num in files_to_remove:
    filename = f"tapa-biblia_-{num}.jpg"
    filepath = os.path.join(produzidas_path, filename)
    print(f"Remove-Item -Path '{filepath}'")

print(f"\nTotal: {len(files_to_remove)} arquivos serão removidos")
