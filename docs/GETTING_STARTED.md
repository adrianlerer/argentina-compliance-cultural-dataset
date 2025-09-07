# 🚀 Getting Started

Guía rápida para comenzar a usar el Argentina Compliance Cultural Dataset.

## ⚡ Instalación Rápida

### Método 1: Pip (Recomendado)
```bash
pip install argentina-compliance-cultural-dataset
```

### Método 2: Desde Código
```bash
git clone https://github.com/adrianlerer/argentina-compliance-cultural-dataset.git
cd argentina-compliance-cultural-dataset
pip install -r requirements.txt
python setup.py install
```

### Método 3: Docker
```bash
docker run -it argentina-compliance:community
```

## 🎯 Uso Básico (3 líneas de código)

```python
from argentina_classifier import classify

# Analizar una frase
result = classify("Un regalito para el inspector")
print(f"Riesgo: {result.risk_level}/5 - {result.category}")
```

## 📊 Ejemplo Completo

```python
from argentina_classifier import ArgentinaComplianceClassifier

# Inicializar clasificador
classifier = ArgentinaComplianceClassifier()

# Frases para analizar
phrases = [
    "Es solo un asadito con el cliente",
    "Mi cuñado tiene una empresa", 
    "Facturamos como consultoría"
]

# Clasificar en lote
results = classifier.classify_batch(phrases)

# Mostrar resultados
for phrase, result in zip(phrases, results):
    print(f"'{phrase}'")
    print(f"  Riesgo: {result.risk_level}/5")
    print(f"  Categoría: {result.category}")
    print(f"  Legal: {result.legal_reference}")
    print(f"  Marcadores: {result.cultural_markers}")
    print(f"  Ventaja: {result.competitive_advantage}")
    print()
```

## 🔧 API Reference

### Clase Principal: `ArgentinaComplianceClassifier`

#### Métodos:

**`classify(text: str) -> ComplianceResult`**
- Clasifica una frase individual
- Retorna objeto `ComplianceResult` con análisis completo

**`classify_batch(texts: List[str]) -> List[ComplianceResult]`**
- Clasifica múltiples frases en lote
- Más eficiente para volúmenes grandes

**`get_stats() -> Dict`**
- Retorna estadísticas del dataset
- Útil para validación y debugging

### Objeto de Resultado: `ComplianceResult`

```python
@dataclass
class ComplianceResult:
    phrase: str                    # Frase analizada
    risk_level: int               # Nivel de riesgo (1-5)
    category: str                 # Categoría de riesgo
    cultural_markers: List[str]   # Marcadores culturales detectados
    legal_reference: str          # Referencia legal Ley 27.401
    explanation: str              # Explicación del análisis
    competitive_advantage: str    # Ventaja vs herramientas internacionales
    confidence_score: float       # Confianza del análisis (0-1)
    ai_validation: str           # Info de validación por IA
```

## 🎮 Demo Interactivo

```bash
python demo.py
```

El demo incluye:
- 🎯 Casos de alto impacto
- 🏢 Análisis por sector
- 🎮 Modo interactivo
- 📊 Comparación vs herramientas internacionales

## 📋 Categorías de Riesgo

| Código | Descripción | Artículo Ley 27.401 |
|---|---|---|
| `SOBORNO` | Actos de corrupción directa | Art. 3 |
| `GASTOS_EXCESIVOS` | Hospitalidad excesiva | Art. 7 |
| `CONFLICTO_INTERES` | Conflictos familiares/personales | Art. 9 |
| `FRAUDE_GASTOS` | Uso indebido de recursos | Art. 23 |
| `TRAFICO_INFLUENCIAS` | Uso de posición para beneficios | Art. 15 |
| `FRAUDE_FISCAL` | Falsificación de información | Art. 27 |
| `CULTURA_RIESGO` | Normalización cultural de riesgos | Art. 22 |
| `ACCION_CLANDESTINA` | Resolución irregular | Art. 15 |

## 🇦🇷 Marcadores Culturales

- **`diminutivo_argentino`**: "regalito", "asadito", "consultorcito"
- **`familia_extendida`**: "cuñado", "hermano", "primo"
- **`eufemismo_local`**: "por izquierda", "gestionar", "arreglar"
- **`informalidad_linguistica`**: "dale", "che", "tranquilo"
- **`minimizacion_cultural`**: "no pasa nada", "siempre", "solo"
- **`tradicion_argentina`**: "asado", "mate", "club"

## ⚠️ Niveles de Riesgo

| Nivel | Descripción | Acción Recomendada |
|---|---|---|
| 1 | 🟢 Riesgo Bajo | Monitoreo |
| 2 | 🟡 Riesgo Moderado | Capacitación |
| 3 | 🟠 Riesgo Alto | Revisión inmediata |
| 4 | 🔴 Riesgo Crítico | Acción correctiva |
| 5 | 🚨 Riesgo Extremo | Investigación formal |

## 📈 Casos de Uso Reales

### 📧 Monitoreo de Emails
```python
# Escanear emails corporativos
def monitor_emails(email_content):
    result = classifier.classify(email_content)
    if result.risk_level >= 4:
        send_alert_to_compliance_team(result)
    return result
```

### 💬 Análisis de Chats
```python
# Monitorear chats de Slack/Teams
def analyze_chat_message(message):
    result = classifier.classify(message.text)
    if result.risk_level >= 3:
        log_risk_event(message.user, result)
    return result
```

### 📊 Dashboard Ejecutivo
```python
# Generar métricas para ejecutivos
def generate_risk_dashboard(communications):
    results = classifier.classify_batch(communications)
    return {
        'total_analyzed': len(results),
        'high_risk_count': sum(1 for r in results if r.risk_level >= 4),
        'risk_by_category': group_by_category(results),
        'cultural_patterns': extract_cultural_trends(results)
    }
```

## 🔧 Configuración Avanzada

### Variables de Entorno
```bash
export ARGENTINA_DATASET_PATH="/path/to/custom/dataset.json"
export ARGENTINA_LOG_LEVEL="INFO"
export ARGENTINA_CONFIDENCE_THRESHOLD="0.8"
```

### Configuración Custom
```python
classifier = ArgentinaComplianceClassifier(
    dataset_path="custom_dataset.json"
)
```

## ❓ Troubleshooting

### Error: Dataset no encontrado
```bash
# Verificar que el archivo existe
ls dataset/frases_culturales_community.json

# Reinstalar si es necesario
pip uninstall argentina-compliance-cultural-dataset
pip install argentina-compliance-cultural-dataset
```

### Error: Importación fallida
```python
# Verificar instalación
import sys
print(sys.path)

# Reinstalar dependencias
pip install -r requirements.txt
```

### Performance Issues
```python
# Para volúmenes grandes, usar batch processing
results = classifier.classify_batch(large_text_list)

# En lugar de:
results = [classifier.classify(text) for text in large_text_list]
```

## 📚 Próximos Pasos

1. **Leer ejemplos**: `examples/basic_usage.py`
2. **Ejecutar demo**: `python demo.py` 
3. **Ver casos de uso**: `docs/USE_CASES.md`
4. **Contribuir**: `CONTRIBUTING.md`
5. **Enterprise**: `enterprise@integridai.com.ar`

## 🤝 Soporte

- **GitHub Issues**: [Reportar bugs](https://github.com/adrianlerer/argentina-compliance-cultural-dataset/issues)
- **Discussions**: [Preguntas y discusión](https://github.com/adrianlerer/argentina-compliance-cultural-dataset/discussions)
- **Email**: `opensource@integridai.com.ar`
- **Enterprise**: `enterprise@integridai.com.ar`