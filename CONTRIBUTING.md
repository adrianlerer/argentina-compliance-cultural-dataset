# 🤝 Contribuir al Argentina Compliance Cultural Dataset

¡Gracias por tu interés en contribuir! Este proyecto necesita la comunidad argentina de compliance para crecer.

## 🇦🇷 ¿Cómo Puedes Ayudar?

### 1. 📝 Agregar Frases Culturales
**¿Escuchaste eufemismos argentinos que no están en el dataset?**

```json
{
  "id": "ARG_XXX",
  "phrase": "Tu frase aquí",
  "category": "CATEGORIA_RIESGO",
  "risk_level": 3,
  "cultural_markers": ["marcador1", "marcador2"],
  "legal_reference": "Art. X Ley 27.401",
  "explanation": "Por qué es riesgoso culturalmente",
  "competitive_advantage": "Por qué herramientas internacionales no lo detectan"
}
```

### 2. 🏢 Casos por Sector
- **Construcción**: Modismos de obras, licitaciones
- **Energía**: Jerga de Vaca Muerta, petrolera
- **Salud**: Eufemismos regulatorios ANMAT
- **Fintech**: Patrones BCRA, CNV
- **Agro**: Cultura empresarial rural

### 3. 🌍 Expansión Regional
- **Córdoba**: \"Culia\", modismos locales
- **Mendoza**: Jerga vitivinícola
- **Tucumán**: Cultura azucarera
- **Neuquén**: Modismos energéticos
- **Salta**: Patrones mineros

## 🔧 Proceso de Contribución

### Paso 1: Fork del Repo
```bash
# Fork desde GitHub UI, luego:
git clone https://github.com/tu-usuario/argentina-compliance-cultural-dataset.git
cd argentina-compliance-cultural-dataset
```

### Paso 2: Crear Branch
```bash
git checkout -b nueva-feature-descripcion
```

### Paso 3: Hacer Cambios
- Agregar frases en `dataset/frases_culturales_community.json`
- Seguir formato JSON existente
- Validar con `python argentina_classifier.py`

### Paso 4: Testing
```bash
# Probar que funciona
python demo.py

# Verificar nueva frase
python -c \"from argentina_classifier import classify; print(classify('tu nueva frase'))\"
```

### Paso 5: Pull Request
```bash
git add .
git commit -m \"feat: agregar frases sector construcción\"
git push origin nueva-feature-descripcion
```

Luego crear PR desde GitHub con:
- **Título**: Descripción clara de los cambios
- **Descripción**: Contexto cultural y legal
- **Testing**: Cómo probaste los cambios

## 📋 Guidelines

### ✅ Qué Aceptamos
- ✅ Frases auténticas usadas en empresas argentinas
- ✅ Eufemismos que herramientas internacionales no detectan
- ✅ Patrones culturales específicos por sector/región
- ✅ Referencias legales precisas a Ley 27.401
- ✅ Explicaciones claras del riesgo cultural

### ❌ Qué NO Aceptamos
- ❌ Frases genéricas sin contexto cultural
- ❌ Contenido ofensivo o discriminatorio
- ❌ Referencias legales incorrectas
- ❌ Duplicados de frases existentes
- ❌ Patrones de otros países sin adaptación argentina

### 📏 Estándares de Calidad
- **Autenticidad**: ¿Se usa realmente en empresas argentinas?
- **Riesgo Legal**: ¿Mapea correctamente a Ley 27.401?
- **Ventaja Competitiva**: ¿Herramientas internacionales lo pierden?
- **Marcadores Culturales**: ¿Tiene patrones lingüísticos argentinos?

## 🏆 Contributors Hall of Fame

### 🥇 Core Contributors
- **@adrianlerer** - Creator & maintainer

### 🥈 Major Contributors
- **Tu nombre aquí** - Próximo major contributor

### 🥉 Community Contributors
*Lista se actualiza con cada PR aceptado*

## 📚 Recursos para Contributors

### 📖 Documentación Legal
- [Texto completo Ley 27.401](https://www.argentina.gob.ar/normativa/nacional/ley-27401-2017-281041)
- [Guía implementación OA](https://www.argentina.gob.ar/anticorrupcion)
- [Jurisprudencia actualizada](https://www.cij.gov.ar)

### 🎓 Cultural Context
- [Lunfardo argentino](https://es.wikipedia.org/wiki/Lunfardo)
- [Modismos empresariales](https://www.academia.org.ar)
- [Regionalismos por provincia](https://www.rae.es)

### 🔧 Technical Resources
- [JSON Formatter](https://jsonformatter.org)
- [Regex Tester](https://regex101.com)
- [Python Style Guide](https://pep8.org)

## ❓ Preguntas Frecuentes

### Q: ¿Puedo contribuir si no soy abogado?
**A**: ¡Sí! Necesitamos personas que conozcan la cultura empresarial argentina. Los aspectos legales los validamos nosotros.

### Q: ¿Qué pasa con mi contribución?
**A**: Tu contribución queda bajo licencia MIT. Te damos crédito como contributor y tu aporte ayuda a todas las empresas argentinas.

### Q: ¿Puedo agregar frases de mi empresa?
**A**: Sí, pero asegúrate de anonimizarlas y que no contengan información confidencial.

### Q: ¿Cómo sé si mi frase es \"auténticamente argentina\"?
**A**: Si la usarías en una reunión de negocios informal en Argentina, pero un extranjero no la entendería, probablemente es perfecta.

### Q: ¿Hay versión enterprise?
**A**: Sí, contacta `enterprise@integridai.com.ar` para features avanzadas, más frases y soporte comercial.

## 📞 Contacto

- **GitHub Issues**: [Reportar problemas](https://github.com/adrianlerer/argentina-compliance-cultural-dataset/issues)
- **Email**: `opensource@integridai.com.ar`
- **LinkedIn**: [IntegriDAI Argentina](https://linkedin.com/company/integridai)

## 🎯 Roadmap de Contribuciones

### 🚧 Necesitamos Ahora (High Priority)
- [ ] Frases sector construcción (10+ frases)
- [ ] Eufemismos energéticos Vaca Muerta (5+ frases)
- [ ] Modismos financieros/crypto (8+ frases)
- [ ] Jerga agropecuaria (12+ frases)

### 🔮 Futuras Expansiones
- [ ] Dataset regional por provincias
- [ ] Análisis por generación (Gen X, Millennials, Gen Z)
- [ ] Integración con sistemas de chat empresariales
- [ ] API REST para integraciones

---

## 🇦🇷 Compromiso con Argentina

Este proyecto es sobre **soberanía digital argentina**. Cada contribución fortalece nuestra capacidad de tener herramientas que nos entiendan culturalmente.

**\"Porque entendemos cómo hablamos cuando creemos que nadie nos escucha.\"**

---

### 🚀 ¿Listo para contribuir?

1. **Fork** este repo
2. **Agrega** tu frase cultural argentina  
3. **Crea** PR con contexto
4. **Celebramos** juntos la soberanía digital

**¡Tu contribución puede salvar a una empresa argentina de una multa millonaria!** 🎯