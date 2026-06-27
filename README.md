# BibleCover - Proyecto de Clasificación y Producción de Tapas de Biblia

## Resumen

Este proyecto es un sistema de apoyo a la clasificación y producción de tapas de Biblia, desarrollado para la organización SBA (Sociedad Bíblica del Brasil). El proyecto utiliza inteligencia artificial y visión computacional para automatizar el proceso de identificación, clasificación y generación de tapas para diferentes segmentos de Biblias.

## Objetivo

El objetivo principal es crear un sistema que ayude en:
1. **Clasificación** de diferentes tipos de tapas de Biblia
2. **Producción** de tapas estandarizadas para cada segmento
3. **Visualización** y organización del material de referencia

## Estructura del Proyecto

```
BibleCover/
├── MATERIAL/                    # Material de referencia original
│   └── PROYECTO BIBLIAS SBA.pdf # Documento de especificación del proyecto
├── extracted_temp/              # Imágenes extraídas del PDF de referencia
│   ├── page_*_img_*_xref_*.png # Imágenes de referencia por página
│   └── ...                     # Total de 45 imágenes extraídas
├── Produzidas/                  # Tapas producidas por el sistema
│   ├── tapa-biblia_ (N).jpg/png # 62 tapas producidas
│   └── ...
├── index.html                   # Interfaz web principal (home)
├── diseno.html                  # Página de recursos de diseño
├── segments.json                # Definiciones detalladas de los segmentos
├── classification_report.md     # Informe de clasificación de las tapas
└── README.md                    # Este archivo
```

## Definiciones de los Segmentos

### Segmento A - Tritono
| Característica | Descripción |
|----------------|-------------|
| **Materiales** | 3 cueros o PUs diferentes |
| **Cierre** | Sí |
| **Diseño** | Elaborado (múltiples elementos, texturas complejas) |
| **Hot Stamping** | Sí (dorado o plateado) |
| **Relieve** | Baixo relevo |
| **Visual** | Premium/Sofisticado, tipografía decorativa |
| **PVP** | AR$ 52.000 |

### Segmento B1 - Bitono
| Característica | Descripción |
|----------------|-------------|
| **Materiales** | 2 cueros o PUs diferentes |
| **Cierre** | Sí |
| **Diseño** | Semi-Elaborado (equilibrio entre elementos) |
| **Hot Stamping** | Sí (dorado o plateado) |
| **Relieve** | Variable |
| **Visual** | Clásico/Elegante, tipografía elegante |
| **PVP** | AR$ 47.000 |

### Segmento B2 - Arte
| Característica | Descripción |
|----------------|-------------|
| **Materiales** | 2 cueros o PUs diferentes |
| **Cierre** | Sí |
| **Diseño** | ARTE (4:4 cores) |
| **Hot Stamping** | Sí (dorado o plateado) |
| **Relieve** | Variable |
| **Visual** | Artístico/Colorido, diseño especial |
| **PVP** | AR$ 47.000 |

### Segmento C - GE (Letra Grande)
| Característica | Descripción |
|----------------|-------------|
| **Materiales** | 1 cuero o PU principal |
| **Cierre** | Sí |
| **Diseño** | Tipográfico (enfoque en letra grande) |
| **Hot Stamping** | Sí (letras grandes) |
| **Relieve** | Baixo relevo |
| **Visual** | Moderno/Tipográfico, tipografía grande |
| **PVP** | AR$ 44.000 |

### Segmento D - GC (Canto Dorado)
| Característica | Descripción |
|----------------|-------------|
| **Materiales** | 1 cuero o PU principal |
| **Cierre** | No |
| **Diseño** | Decorativo (canto dorado) |
| **Hot Stamping** | Sí (canto dorado) |
| **Relieve** | Baixo relevo |
| **Visual** | Elegante/Decorativo, detalles en metálico |
| **PVP** | AR$ 35.000 |

### Segmento E - GI (Vinilo Económico)
| Característica | Descripción |
|----------------|-------------|
| **Materiales** | Vinilo económico |
| **Cierre** | No |
| **Diseño** | Simple (funcional) |
| **Hot Stamping** | No |
| **Visual** | Simple/Funcional, canto blanco |
| **PVP** | AR$ 33.000 |

## Funcionalidades

### 1. Extracción de Imágenes de Referencia
- El sistema extrae imágenes del PDF de especificación (PROYECTO BIBLIAS SBA.pdf)
- Imágenes organizadas por página y tipo de referencia
- Total de 45 imágenes de referencia extraídas

### 2. Clasificación por Segmentos
- Cada imagen de referencia es clasificada conforme su segmento
- Etiquetas visuales (REF/PRODUCED) identifican el estado de cada imagen
- Organización jerárquica por página y tipo
- **Etiquetas detalladas** mostrando características:
  - Tipo de material (Tritono/Bitono/Monotono/Vinilo)
  - Presencia de cierre (Sí/No)
  - Tipo de diseño (Elaborado/Semi-Elaborado/Tipográfico/Decorativo/Simple)
  - Hot Stamping (Sí/No, color)

### 3. Producción de Tapas
- Generación de tapas estandarizadas para cada segmento
- 62 tapas producidas
- **Clasificación automática** de cada tapa producida

### 4. Interfaz de Visualización (Home)
- **index.html**: Interfaz web principal con tema oscuro
- Layout en grid responsivo con cards para cada tapa
- **Tabs**: Navegación entre Producidas y Segmentos
- **Búsqueda**: Filtrar imágenes por nombre o segmento
- **Modal/Lightbox**: Visualización en pantalla completa con navegación (flechas izquierda/derecha)
- **Modal de Referencias**: Visualización de imágenes de referencia por segmento
- **Modal de Consideraciones**: Notas positivas/negativas sobre cada tapa
- **Estadísticas**: Contadores automáticos por segmento
- **Filtros por Segmento**: Botones de leyenda para filtrar por segmento
- **PVP**: Precio visible al pasar el mouse sobre cada tapa
- **Navegación por teclado**: Escape para cerrar, flechas para navegar

### 5. Sistema de Clasificación
- Definiciones detalladas en `segments.json`
- Reglas de clasificación basadas en:
  - Cantidad de materiales
  - Presencia de cierre
  - Tipo de diseño
  - Presencia de hot stamping
- Informe completo en `classification_report.md`

## Cómo Usar

### Visualización de las Imágenes
1. Abra el archivo `index.html` en cualquier navegador web
2. Navegue por las pestañas:
   - **Producidas**: Tapas clasificadas automáticamente
   - **Segmentos**: Definiciones detalladas de cada segmento
3. Use la búsqueda para filtrar por nombre o segmento
4. Filtre por segmento usando los botones de leyenda (Todos, Preseleccionadas, A, B1, B2, C1, D, E)
5. Haga clic en cualquier imagen para ver en pantalla completa
6. Use las flechas izquierda/derecha o teclado para navegar entre tapas
7. Presione Escape o haga clic fuera del modal para cerrar
8. Pase el mouse sobre una tapa para ver su precio (PVP)

### Proceso de Producción
1. Las imágenes de referencia son extraídas del PDF
2. Cada segmento es clasificado conforme sus características
3. Tapas son producidas siguiendo los patrones definidos
4. El sistema clasifica automáticamente cada tapa producida
5. El resultado final se almacena en la carpeta "Produzidas"

### Recursos de Diseño
- Acceda a la página de recursos de diseño desde el enlace "Recursos Diseño" en el pie de la home
- Contiene definiciones visuales de cada segmento con imágenes de referencia

## Clasificación Automática

El sistema clasifica las tapas con base en los siguientes criterios:

### Identificación de Tritono (3 materiales)
- Múltiples texturas visibles
- 3+ colores o tonos diferentes
- Composición compleja con elementos variados

### Identificación de Bitono (2 materiales)
- Dos texturas principales
- Combinación de 2 colores
- Diseño equilibrado

### Identificación de Cierre
- Presencia de trilho de cierre en los costados
- Tiras visibles
- Bordes reforzados

### Identificación de Hot Stamping
- Letras con brillo metálico
- Reflejo dorado o plateado
- Texto elevado con acabado especial

## Tecnologías Utilizadas

- **HTML5/CSS3**: Interfaz de visualización con tema oscuro
- **JavaScript vanilla**: Interactividad, filtros y modales
- **JSON**: Definiciones de los segmentos
- **Procesamiento de Imágenes**: Extracción y manipulación de imágenes del PDF

## Datos del Proyecto

- **Total de Imágenes de Referencia**: 45
- **Total de Tapas Producidas**: 62
- **Segmentos Definidos**: 6 (A, B1, B2, C1, D, E)
- **Páginas de Referencia**: 5 (páginas 9-13 del PDF)
- **Bíblias Preseleccionadas**: 12 (números 1, 4, 14, 23, 33, 39, 40, 42, 47, 53, 57, 63)
- **Bíblias No Comerciales**: 3 (números 13, 17, 18)

### Distribución por Segmento (Tapas Producidas)

| Segmento | Bíblias | Precio PVP |
|----------|---------|------------|
| A - Tritono | 0 | AR$ 52.000 |
| B1 - Bitono 1 | 21 | AR$ 47.000 |
| B2 - Arte | 15 | AR$ 47.000 |
| C1 - GE Letra Grande | 17 | AR$ 44.000 |
| D - GC Canto Dorado | 7 | AR$ 35.000 |
| E - GI Vinilo Económico | 2 | AR$ 33.000 |
| **Total** | **62** | - |

#### Detalle de Bíblias por Segmento

| Segmento | Números de Bíblias |
|----------|-------------------|
| B1 | 15, 42-56, 58, 60-63 |
| B2 | 1, 28-41 |
| C1 | 3-12, 14, 16, 23, 25-27, 57 |
| D | 2, 13, 17-18, 21-22, 24 |
| E | 19-20 |

## Próximos Pasos

1. **Automatización de la Clasificación**: Implementar IA/ML para clasificación visual automática
2. **Expansión de Segmentos**: Agregar nuevos tipos de tapas conforme demanda
3. **Integración con Sistema de Producción**: Conectar con sistemas de impresión
4. **Dashboard**: Panel para seguimiento de la producción en tiempo real
5. **API**: Crear API para integración con otros sistemas

## Licencia

Este proyecto es de uso interno de la organización SBA.

## Contacto

Para más información sobre el proyecto, consulte:
- Documento de especificación: `MATERIAL/PROYECTO BIBLIAS SBA.pdf`
- Definiciones de los segmentos: `segments.json`
- Informe de clasificación: `classification_report.md`

## Registro de Cambios

### 2026-06-26

#### Corrección de Modales
- **Problema**: Los botones de cerrar (×) no funcionaban en los modales de la home
- **Problema**: Hacer clic fuera del contenido no cerraba los modales
- **Causa**: Las funciones `cm()` y `crm()` estaban definidas dentro del IIFE (escopo local) pero las llamadas onclick en HTML esperaban que fueran globales
- **Solución**: Exponer funciones via `window.cm` y `window.crm` para que sean accesibles desde los atributos onclick del HTML

#### Asignación de Segmentos
- Se actualizaron las asignaciones de segmentos para todas las bíblias (números 1-63)
- **B1 (Bitono 1)**: 15, 42-56, 58, 60-63 (21 bíblias)
- **B2 (Arte)**: 1, 28-41 (15 bíblias)
- **C1 (GE Letra Grande)**: 3-12, 14, 16, 23, 25-27, 57 (17 bíblias)
- **D (GC Canto Dorado)**: 2, 13, 17-18, 21-22, 24 (7 bíblias)
- **E (GI Vinilo Económico)**: 19-20 (2 bíblias)
- **Total**: 62 bíblias (número 59 no existe en el dataset)