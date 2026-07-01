import os

# Arquivos a remover do index
files_to_remove = {27, 49, 51, 52, 54, 61, 68, 72, 73, 84, 86, 87, 89, 92, 94, 96, 97, 102, 103}

# Ler o index.html
index_path = r"I:\My Drive\Backup Ativo\Trabalho\2026\IA Agents\BibleCover\index.html"

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extrair o array D atual
import re

# Encontrar o array D
d_match = re.search(r'var D = \[(.*?)\];', content, re.DOTALL)
if d_match:
    d_content = d_match.group(1)
    
    # Extrair cada entrada
    entries = re.findall(r'\{ n: (\d+), s: "([^"]*)", z: (\d+), h: (\d+), r: (\d+) \}', d_content)
    
    # Filtrar entradas (remover as deletadas)
    filtered_entries = []
    for n, s, z, h, r in entries:
        n_int = int(n)
        if n_int not in files_to_remove:
            filtered_entries.append(f'{{ n: {n}, s: "{s}", z: {z}, h: {h}, r: {r} }}')
    
    # Reconstruir o array D
    new_d = "var D = [\n"
    for i, entry in enumerate(filtered_entries):
        if i > 0 and i % 4 == 0:
            new_d += "\n                "
        new_d += entry
        if i < len(filtered_entries) - 1:
            new_d += ", "
    new_d += "\n            ];"
    
    # Substituir no content
    content = content[:d_match.start()] + new_d + content[d_match.end():]

# Encontrar o objeto TAGS
tags_match = re.search(r'var TAGS = \{(.*?)\};', content, re.DOTALL)
if tags_match:
    tags_content = tags_match.group(1)
    
    # Extrair cada entrada
    tag_entries = re.findall(r'(\d+): \[(.*?)\]', tags_content)
    
    # Filtrar entradas (remover as deletadas) e adicionar VIN. LISO para 116-124
    filtered_tags = []
    for n, tags in tag_entries:
        n_int = int(n)
        if n_int not in files_to_remove:
            # Adicionar VIN. LISO para 116-124
            if 116 <= n_int <= 124:
                filtered_tags.append(f'{n}: ["VIN. LISO"]')
            else:
                filtered_tags.append(f'{n}: [{tags}]')
    
    # Reconstruir o objeto TAGS
    new_tags = "var TAGS = {\n"
    for i, tag in enumerate(filtered_tags):
        if i > 0 and i % 5 == 0:
            new_tags += "\n                "
        new_tags += tag
        if i < len(filtered_tags) - 1:
            new_tags += ", "
    new_tags += "\n            };"
    
    # Substituir no content
    content = content[:tags_match.start()] + new_tags + content[tags_match.end():]

# Salvar o index.html atualizado
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Index.html atualizado com sucesso!")
print(f"Entradas removidas: {len(files_to_remove)}")
print(f"Tags 'VIN. LISO' adicionadas para: 116-124")
