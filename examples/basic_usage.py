#!/usr/bin/env python3
"""
Basic Usage Examples - Argentina Compliance Cultural Dataset
Shows how to use the classifier in real scenarios
"""

from argentina_classifier import ArgentinaComplianceClassifier

def example_basic_classification():
    """Example 1: Basic phrase classification"""
    print("🔍 EJEMPLO 1: Clasificación básica de frase")
    print("-" * 50)
    
    classifier = ArgentinaComplianceClassifier()
    
    phrase = "Es solo un asadito con el cliente"
    result = classifier.classify(phrase)
    
    print(f"Frase: '{phrase}'")
    print(f"Riesgo: {result.risk_level}/5")
    print(f"Categoría: {result.category}")
    print(f"Referencia legal: {result.legal_reference}")
    print(f"Marcadores culturales: {result.cultural_markers}")
    print(f"Ventaja competitiva: {result.competitive_advantage}")

def example_batch_processing():
    """Example 2: Batch processing of multiple phrases"""
    print("\n📊 EJEMPLO 2: Procesamiento en lote")
    print("-" * 50)
    
    classifier = ArgentinaComplianceClassifier()
    
    phrases = [
        "Un regalito para el inspector",
        "Mi cuñado maneja ese sector", 
        "Facturamos como consultoría",
        "Lo arreglamos por izquierda",
        "Necesitamos gestionar esto rápido"
    ]
    
    results = classifier.classify_batch(phrases)
    
    for phrase, result in zip(phrases, results):
        print(f"'{phrase}' → Riesgo: {result.risk_level}/5 ({result.category})")

def example_risk_monitoring():
    """Example 3: Risk monitoring and alerting"""
    print("\n🚨 EJEMPLO 3: Monitoreo de riesgos y alertas")
    print("-" * 50)
    
    classifier = ArgentinaComplianceClassifier()
    
    # Simulated email/chat content
    communications = [
        "Reunión de directorio mañana a las 10",  # Low risk
        "Regalito para acelerar la habilitación",  # High risk
        "Revisar presupuesto del trimestre",  # Low risk  
        "Mi hermano puede resolver esto",  # High risk
        "Enviar propuesta al cliente",  # Low risk
    ]
    
    high_risk_threshold = 4
    alerts = []
    
    for comm in communications:
        result = classifier.classify(comm)
        if result.risk_level >= high_risk_threshold:
            alerts.append({
                'text': comm,
                'risk_level': result.risk_level,
                'category': result.category,
                'legal_ref': result.legal_reference
            })
    
    print(f"📧 Comunicaciones analizadas: {len(communications)}")
    print(f"🚨 Alertas generadas: {len(alerts)}")
    
    for alert in alerts:
        print(f"   ALERTA: '{alert['text']}'")
        print(f"   Riesgo: {alert['risk_level']}/5 - {alert['category']}")
        print(f"   Legal: {alert['legal_ref']}")

def example_sector_analysis():
    """Example 4: Sector-specific analysis"""
    print("\n🏢 EJEMPLO 4: Análisis específico por sector")
    print("-" * 50)
    
    classifier = ArgentinaComplianceClassifier()
    
    sector_examples = {
        "Construcción": [
            "El primo del intendente nos ayuda con los permisos",
            "Contratamos a la empresa del cuñado"
        ],
        "Energía": [
            "Asado con los directivos de YPF",
            "Regalito para agilizar el permiso ambiental"
        ],
        "Salud": [
            "Colaboración con el inspector de ANMAT", 
            "Gestionar la habilitación del laboratorio"
        ]
    }
    
    for sector, phrases in sector_examples.items():
        print(f"\n🎯 {sector.upper()}:")
        for phrase in phrases:
            result = classifier.classify(phrase)
            print(f"   '{phrase}'")
            print(f"   → Riesgo: {result.risk_level}/5 - {result.category}")

def example_legal_mapping():
    """Example 5: Legal reference mapping"""
    print("\n⚖️  EJEMPLO 5: Mapeo de referencias legales")
    print("-" * 50)
    
    classifier = ArgentinaComplianceClassifier()
    
    legal_cases = [
        "Un regalito para el inspector",  # Art. 3 - Soborno
        "Mi cuñado tiene una empresa",   # Art. 9 - Conflicto
        "Facturamos como consultoría",   # Art. 27 - Registros
        "Dale que siempre se hizo así"   # Art. 22 - Cultura
    ]
    
    print("📋 Mapeo automático a artículos Ley 27.401:")
    for phrase in legal_cases:
        result = classifier.classify(phrase)
        print(f"   '{phrase}'")
        print(f"   → {result.legal_reference}")
        print(f"   → Categoría: {result.category}")

if __name__ == "__main__":
    print("🇦🇷 ARGENTINA COMPLIANCE CULTURAL DATASET")
    print("Ejemplos de uso - Community Edition")
    print("=" * 60)
    
    # Run all examples
    example_basic_classification()
    example_batch_processing() 
    example_risk_monitoring()
    example_sector_analysis()
    example_legal_mapping()
    
    print(f"\n✅ Ejemplos completados!")
    print(f"📚 Más documentación: README.md")
    print(f"💼 Enterprise: enterprise@integridai.com.ar")