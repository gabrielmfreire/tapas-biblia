# Mapeamento dos arquivos renomeados com seus nomes originais
# Primera tanda (64-97): archivos de la carpeta nuevas (1-15 y Layer 1037-1056)
# Segunda tanda (98-124): archivos nuevos con nombres descriptivos

mapeamento = {
    # Primera tanda - originales numéricos y Layer (sin tags en el nombre)
    64: {"original": "Layer 1050.jpg", "tags_sugeridas": []},
    65: {"original": "Layer 1051.jpg", "tags_sugeridas": []},
    66: {"original": "Layer 1049.jpg", "tags_sugeridas": []},
    67: {"original": "Layer 1047.jpg", "tags_sugeridas": []},
    68: {"original": "Layer 1048.jpg", "tags_sugeridas": []},
    69: {"original": "Layer 1055.jpg", "tags_sugeridas": []},
    70: {"original": "Layer 1056.jpg", "tags_sugeridas": []},
    71: {"original": "Layer 1054.jpg", "tags_sugeridas": []},
    72: {"original": "Layer 1052.jpg", "tags_sugeridas": []},
    73: {"original": "Layer 1053.jpg", "tags_sugeridas": []},
    74: {"original": "Layer 1040.jpg", "tags_sugeridas": []},
    75: {"original": "Layer 1041.jpg", "tags_sugeridas": []},
    76: {"original": "Layer 1039.jpg", "tags_sugeridas": []},
    77: {"original": "Layer 1037.jpg", "tags_sugeridas": []},
    78: {"original": "Layer 1038.jpg", "tags_sugeridas": []},
    79: {"original": "Layer 1045.jpg", "tags_sugeridas": []},
    80: {"original": "Layer 1046.jpg", "tags_sugeridas": []},
    81: {"original": "Layer 1044.jpg", "tags_sugeridas": []},
    82: {"original": "Layer 1042.jpg", "tags_sugeridas": []},
    83: {"original": "Layer 1043.jpg", "tags_sugeridas": []},
    84: {"original": "1.jpg", "tags_sugeridas": []},
    85: {"original": "2.jpg", "tags_sugeridas": []},
    86: {"original": "3.jpg", "tags_sugeridas": []},
    87: {"original": "4.jpg", "tags_sugeridas": []},
    88: {"original": "5.jpg", "tags_sugeridas": []},
    89: {"original": "6.jpg", "tags_sugeridas": []},
    90: {"original": "7.jpg", "tags_sugeridas": []},
    91: {"original": "8.jpg", "tags_sugeridas": []},
    92: {"original": "10.jpg", "tags_sugeridas": []},
    93: {"original": "11.jpg", "tags_sugeridas": []},
    94: {"original": "12.jpg", "tags_sugeridas": []},
    95: {"original": "13.jpg", "tags_sugeridas": []},
    96: {"original": "14.jpg", "tags_sugeridas": []},
    97: {"original": "15.jpg", "tags_sugeridas": []},

    # Segunda tanda - nombres descriptivos con tags
    # TRITONO = Segmento A
    98: {"original": "Tritono_M_1.jpg", "segmento": "A", "tags": ["RELIEVE", "HOT STAMPING"]},
    99: {"original": "Tritono_F_4.jpg", "segmento": "A", "tags": ["RELIEVE", "HOT STAMPING"]},
    100: {"original": "Tritono_F_3.jpg", "segmento": "A", "tags": ["RELIEVE", "HOT STAMPING"]},
    101: {"original": "Tritono_F_2.jpg", "segmento": "A", "tags": ["RELIEVE", "HOT STAMPING"]},
    102: {"original": "Tritono.jpg", "segmento": "A", "tags": ["RELIEVE", "HOT STAMPING"]},

    # B_ARTE = Segmento B2
    103: {"original": "B_ARTE_U_1.jpg", "segmento": "B2", "tags": ["BITONO", "ARTE"]},
    104: {"original": "B_ARTE_M_1.jpg", "segmento": "B2", "tags": ["BITONO", "ARTE"]},
    105: {"original": "B_ARTE_3.jpg", "segmento": "B2", "tags": ["BITONO", "ARTE"]},
    106: {"original": "B_ARTE_F_2.jpg", "segmento": "B2", "tags": ["BITONO", "ARTE"]},
    107: {"original": "B_ARTE_SI.jpg", "segmento": "B2", "tags": ["BITONO", "ARTE"]},

    # HOT_RELIEVE = Posible segmento C1 o variable
    108: {"original": "HOT_RELIEVE_F_6.jpg", "segmento": "C1", "tags": ["HOT STAMPING", "RELIEVE"]},
    109: {"original": "HOT_RELIEVE_F_5.jpg", "segmento": "C1", "tags": ["HOT STAMPING", "RELIEVE"]},
    110: {"original": "HOT_RELIEVE_F_4.jpg", "segmento": "C1", "tags": ["HOT STAMPING", "RELIEVE"]},
    111: {"original": "HOT_RELIEVE_F_3.jpg", "segmento": "C1", "tags": ["HOT STAMPING", "RELIEVE"]},
    112: {"original": "HOT_RELIEVE_U_1.jpg", "segmento": "C1", "tags": ["HOT STAMPING", "RELIEVE"]},
    113: {"original": "HOT_RELIEVE_F_2.jpg", "segmento": "C1", "tags": ["HOT STAMPING", "RELIEVE"]},
    114: {"original": "HOT_RELIEVE_F_1.jpg", "segmento": "C1", "tags": ["HOT STAMPING", "RELIEVE"]},
    115: {"original": "HOT_RELIEVE_M_1.jpg", "segmento": "C1", "tags": ["HOT STAMPING", "RELIEVE"]},

    # VINILO_LISO = Segmento E
    116: {"original": "VINILO_LISO_F_7.jpg", "segmento": "E", "tags": []},
    117: {"original": "VINILO_LISO_F_6.jpg", "segmento": "E", "tags": []},
    118: {"original": "VINILO_LISO_M_1.jpg", "segmento": "E", "tags": []},
    119: {"original": "VINILO_LISO_F_5.jpg", "segmento": "E", "tags": []},
    120: {"original": "VINILO_LISO_F_4.jpg", "segmento": "E", "tags": []},
    121: {"original": "VINILO_LISO_U_1.jpg", "segmento": "E", "tags": []},
    122: {"original": "VINILO_LISO_F_3.jpg", "segmento": "E", "tags": []},
    123: {"original": "VINILO_LISO_F_2.jpg", "segmento": "E", "tags": []},
    124: {"original": "VINILO_LISO_F_1.jpg", "segmento": "E", "tags": []},
}

# Imprimir resumen
print("=" * 80)
print("ANÁLISIS DE NOMBRES ORIGINALES Y TAGS EXTRAÍDAS")
print("=" * 80)

print("\n### SEGUNDA TANDA (98-124) - CON TAGS EN EL NOMBRE ###\n")

for num in range(98, 125):
    info = mapeamento[num]
    segmento = info.get("segmento", "N/A")
    tags = info.get("tags", [])
    original = info["original"]
    
    print(f"tapa-biblia_-{num}.jpg")
    print(f"  Original: {original}")
    print(f"  Segmento: {segmento}")
    print(f"  Tags: {', '.join(tags) if tags else 'Ninguna'}")
    print()

print("\n### PRIMERA TANDA (64-97) - SIN TAGS EN EL NOMBRE ###")
print("Estos archivos solo tenían números o 'Layer XXXX' en sus nombres.")
print("Necesitan que les asigne segmento y tags manualmente.\n")

# Generar código para actualizar el index.html
print("\n" + "=" * 80)
print("CÓDIGO PARA ACTUALIZAR INDEX.HTML")
print("=" * 80)

print("\n// Segmentos y Tags para segunda tanda (98-124):")
print("// Copiar y pegar en el objeto D (array) y TAGS:\n")

for num in range(98, 125):
    info = mapeamento[num]
    segmento = info.get("segmento", "")
    tags = info.get("tags", [])
    
    # Para el array D
    print(f"// {num}: {info['original']}")
    print(f'{{ n: {num}, s: "{segmento}", z: 1, h: 1, r: 1 }},')
    
print()
print("// Tags para segunda tanda:")

for num in range(98, 125):
    info = mapeamento[num]
    tags = info.get("tags", [])
    print(f'{num}: {tags},')
