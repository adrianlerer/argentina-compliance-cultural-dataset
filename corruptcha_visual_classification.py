#!/usr/bin/env python3
"""
🚀 CORRUPTCHA VISUAL CLASSIFICATION 🚀
Micro-tareas visuales estilo Google CAPTCHA para compliance argentino

Inspirado en el modelo perro/muffin de Google pero para INTEGRIDAD EMPRESARIAL

✅ Visual + Text Classification | ✅ Crowdsourced Training | ✅ Cultural Intelligence
✅ Gamification | ✅ Quality Control | ✅ Revenue Generation

"La IA que entiende cómo hablan los argentinos en los negocios"
"""

import random
import json
import uuid
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
import base64
import io

@dataclass
class VisualTask:
    """Tarea visual de clasificación CORRUPTCHA"""
    task_id: str
    task_type: str  # "risk_classification", "euphemism_detection", "family_networks"
    question: str
    options: List[Dict[str, Any]]  # Cada opción tiene texto, imagen opcional, metadata
    correct_answer: Optional[str] = None
    difficulty_level: int = 1  # 1-5
    cultural_context: str = "argentina"
    legal_reference: str = ""
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

class CorruptchaVisualEngine:
    """
    Motor de clasificación visual CORRUPTCHA
    Genera micro-tareas estilo Google perro/muffin pero para compliance
    """
    
    def __init__(self):
        self.task_templates = self._load_task_templates()
        self.cultural_scenarios = self._load_cultural_scenarios()
        self.visual_elements = self._load_visual_elements()
        
        print("🚀 CORRUPTCHA Visual Engine initialized")
        print("📊 Inspirado en Google perro/muffin para compliance argentino")
    
    def _load_task_templates(self) -> Dict[str, Any]:
        """Cargar templates de tareas visuales"""
        
        return {
            "risk_classification": {
                "question_template": "¿Cuál de estas situaciones representa MAYOR riesgo bajo Ley 27.401?",
                "description": "Clasificar nivel de riesgo en situaciones empresariales",
                "options_count": 4,
                "time_limit": 30  # segundos
            },
            "euphemism_detection": {
                "question_template": "¿Cuál de estas expresiones es un EUFEMISMO de actividad irregular?",
                "description": "Detectar eufemismos culturales argentinos",
                "options_count": 4,
                "time_limit": 25
            },
            "family_networks": {
                "question_template": "¿Cuál indica CONFLICTO DE INTERESES por vínculos familiares?",
                "description": "Identificar redes familiares en contexto empresarial",
                "options_count": 3,
                "time_limit": 20
            },
            "hospitality_assessment": {
                "question_template": "¿Cuál excede los límites razonables de hospitalidad empresarial?",
                "description": "Evaluar gastos de representación y hospitalidad",
                "options_count": 4,
                "time_limit": 30
            },
            "contract_anomalies": {
                "question_template": "¿Cuál de estos términos contractuales sugiere irregularidades?",
                "description": "Detectar cláusulas sospechosas en contratos",
                "options_count": 3,
                "time_limit": 35
            }
        }
    
    def _load_cultural_scenarios(self) -> Dict[str, List[Dict[str, Any]]]:
        """Cargar escenarios culturales por categoría"""
        
        return {
            "risk_classification": [
                {
                    "text": "Reunión de coordinación con proveedor",
                    "risk_level": "LOW",
                    "cultural_markers": [],
                    "visual_cue": "📋 Reunión formal"
                },
                {
                    "text": "Un regalito de fin de año para el inspector",
                    "risk_level": "HIGH", 
                    "cultural_markers": ["diminutivo_argentino", "funcionario_publico"],
                    "visual_cue": "🎁 Regalo + 👨‍💼 Funcionario"
                },
                {
                    "text": "Cena de trabajo con cliente potencial",
                    "risk_level": "MEDIUM",
                    "cultural_markers": ["hospitalidad_comercial"],
                    "visual_cue": "🍽️ Cena de negocios"
                },
                {
                    "text": "Mi cuñado puede conseguirnos el contrato",
                    "risk_level": "HIGH",
                    "cultural_markers": ["familia_extendida", "trafico_influencias"],
                    "visual_cue": "👨‍👨‍👦 Familia + 📄 Contrato"
                }
            ],
            "euphemism_detection": [
                {
                    "text": "Vamos a gestionar el tema con el municipio",
                    "is_euphemism": True,
                    "meaning": "Posible soborno o influencia irregular",
                    "visual_cue": "🏛️ Municipio + 💰 Gestión"
                },
                {
                    "text": "Presentamos la documentación requerida",
                    "is_euphemism": False,
                    "meaning": "Procedimiento normal",
                    "visual_cue": "📄 Documentos oficiales"
                },
                {
                    "text": "Lo acomodamos por izquierda como siempre",
                    "is_euphemism": True,
                    "meaning": "Procedimiento irregular habitual",
                    "visual_cue": "⬅️ Por izquierda + 🔄 Repetición"
                },
                {
                    "text": "Seguimos el proceso establecido en el reglamento",
                    "is_euphemism": False,
                    "meaning": "Cumplimiento normativo",
                    "visual_cue": "📚 Reglamento + ✅ Cumplimiento"
                }
            ],
            "family_networks": [
                {
                    "text": "El director de compras es profesional independiente",
                    "has_conflict": False,
                    "relationship_type": "none",
                    "visual_cue": "👤 Profesional independiente"
                },
                {
                    "text": "Mi hermano dirige la empresa contratista",
                    "has_conflict": True,
                    "relationship_type": "hermano",
                    "visual_cue": "👬 Hermanos + 🏢 Empresa"
                },
                {
                    "text": "El proveedor recomendado es primo del gerente",
                    "has_conflict": True,
                    "relationship_type": "primo",
                    "visual_cue": "👨‍👨‍👦‍👦 Primos + 🤝 Recomendación"
                }
            ]
        }
    
    def _load_visual_elements(self) -> Dict[str, str]:
        """Cargar elementos visuales (emojis como placeholder)"""
        
        return {
            "high_risk": "🚨",
            "medium_risk": "⚠️", 
            "low_risk": "✅",
            "family": "👨‍👩‍👧‍👦",
            "money": "💰",
            "government": "🏛️",
            "business": "🏢",
            "document": "📄",
            "gift": "🎁",
            "meeting": "🤝",
            "dinner": "🍽️",
            "contract": "📋"
        }
    
    def generate_visual_task(self, task_type: str, difficulty: int = 3) -> VisualTask:
        """Generar tarea visual de clasificación"""
        
        if task_type not in self.task_templates:
            task_type = "risk_classification"  # Default
        
        template = self.task_templates[task_type]
        scenarios = self.cultural_scenarios.get(task_type, [])
        
        # Seleccionar escenarios según dificultad
        selected_scenarios = self._select_scenarios_by_difficulty(scenarios, template["options_count"], difficulty)
        
        # Construir opciones
        options = []
        correct_answer = None
        
        for i, scenario in enumerate(selected_scenarios):
            option = {
                "id": f"option_{i+1}",
                "text": scenario["text"],
                "visual_cue": scenario.get("visual_cue", ""),
                "metadata": {
                    "cultural_markers": scenario.get("cultural_markers", []),
                    "risk_level": scenario.get("risk_level"),
                    "is_euphemism": scenario.get("is_euphemism"),
                    "has_conflict": scenario.get("has_conflict")
                }
            }
            options.append(option)
            
            # Determinar respuesta correcta según tipo de tarea
            if task_type == "risk_classification" and scenario.get("risk_level") == "HIGH":
                correct_answer = option["id"]
            elif task_type == "euphemism_detection" and scenario.get("is_euphemism") == True:
                correct_answer = option["id"]
            elif task_type == "family_networks" and scenario.get("has_conflict") == True:
                correct_answer = option["id"]
        
        # Shufflear opciones
        random.shuffle(options)
        
        # Actualizar correct_answer después del shuffle
        if correct_answer:
            for option in options:
                if any(
                    (task_type == "risk_classification" and option["metadata"].get("risk_level") == "HIGH") or
                    (task_type == "euphemism_detection" and option["metadata"].get("is_euphemism") == True) or
                    (task_type == "family_networks" and option["metadata"].get("has_conflict") == True)
                    for _ in [None]  # Trick to make this work in any()
                ):
                    correct_answer = option["id"]
                    break
        
        task = VisualTask(
            task_id=str(uuid.uuid4()),
            task_type=task_type,
            question=template["question_template"],
            options=options,
            correct_answer=correct_answer,
            difficulty_level=difficulty,
            legal_reference="Art. 22 Ley 27.401"
        )
        
        return task
    
    def _select_scenarios_by_difficulty(self, scenarios: List[Dict[str, Any]], count: int, difficulty: int) -> List[Dict[str, Any]]:
        """Seleccionar escenarios basado en nivel de dificultad"""
        
        if difficulty <= 2:
            # Fácil: incluir casos obvios
            high_risk = [s for s in scenarios if s.get("risk_level") == "HIGH" or s.get("is_euphemism") == True or s.get("has_conflict") == True]
            low_risk = [s for s in scenarios if s.get("risk_level") == "LOW" or s.get("is_euphemism") == False or s.get("has_conflict") == False]
            
            selected = high_risk[:1] + low_risk[:count-1]
            
        elif difficulty >= 4:
            # Difícil: casos ambiguos
            medium_risk = [s for s in scenarios if s.get("risk_level") == "MEDIUM"]
            others = [s for s in scenarios if s not in medium_risk]
            
            selected = medium_risk + others[:count-len(medium_risk)]
            
        else:
            # Medio: mix balanceado
            selected = random.sample(scenarios, min(count, len(scenarios)))
        
        # Completar si faltan opciones
        while len(selected) < count and scenarios:
            selected.append(random.choice(scenarios))
            
        # Si aún faltan, duplicar existentes
        while len(selected) < count:
            if selected:
                selected.append(random.choice(selected))
            else:
                # Fallback scenario
                selected.append({
                    "text": "Procedimiento estándar de la empresa",
                    "risk_level": "LOW",
                    "is_euphemism": False,
                    "has_conflict": False,
                    "cultural_markers": [],
                    "visual_cue": "✅ Procedimiento normal"
                })
            
        return selected[:count]
    
    def validate_user_response(self, task: VisualTask, user_answer: str, response_time: float) -> Dict[str, Any]:
        """Validar respuesta del usuario"""
        
        is_correct = (task.correct_answer == user_answer)
        
        # Scoring basado en correctitud y tiempo
        base_score = 100 if is_correct else 0
        time_bonus = max(0, 30 - response_time) * 2  # Bonus por rapidez (max 30 seg)
        final_score = min(100, base_score + time_bonus)
        
        # Encontrar la opción seleccionada
        selected_option = None
        for option in task.options:
            if option["id"] == user_answer:
                selected_option = option
                break
        
        return {
            "is_correct": is_correct,
            "score": final_score,
            "response_time": response_time,
            "selected_option": selected_option,
            "correct_option": next((opt for opt in task.options if opt["id"] == task.correct_answer), None),
            "cultural_learning": self._generate_cultural_explanation(task, selected_option, is_correct)
        }
    
    def _generate_cultural_explanation(self, task: VisualTask, selected_option: Optional[Dict[str, Any]], is_correct: bool) -> str:
        """Generar explicación cultural para el usuario"""
        
        if not selected_option:
            return "Respuesta no válida."
        
        if is_correct:
            explanations = {
                "risk_classification": f"✅ Correcto! '{selected_option['text']}' representa un riesgo alto porque contiene marcadores culturales argentinos que indican posible violación de Ley 27.401.",
                "euphemism_detection": f"✅ Correcto! '{selected_option['text']}' es un eufemismo típico argentino para encubrir actividades irregulares.",
                "family_networks": f"✅ Correcto! Esta situación indica conflicto de intereses por vínculos familiares, muy común en contexto empresarial argentino."
            }
        else:
            explanations = {
                "risk_classification": f"❌ Incorrecto. '{selected_option['text']}' no es la opción de mayor riesgo. Las herramientas internacionales como SAP GRC tampoco detectarían estos patrones culturales argentinos.",
                "euphemism_detection": f"❌ Incorrecto. '{selected_option['text']}' no es un eufemismo. En Argentina usamos expresiones específicas para encubrir irregularidades que las herramientas globales no comprenden.",
                "family_networks": f"❌ Incorrecto. Esta situación no presenta conflicto familiar directo. En Argentina, las redes familiares en negocios son más sutiles que lo que detectan herramientas internacionales."
            }
        
        base_explanation = explanations.get(task.task_type, "Análisis cultural completado.")
        
        # Agregar contexto educativo
        educational_context = "\n\n💡 CORRUPTCHA detecta estos patrones únicos que SAP GRC, PwC Risk y EY Compliance NO identifican porque no comprenden el contexto cultural argentino."
        
        return base_explanation + educational_context
    
    def generate_gamified_session(self, user_level: int = 1, session_length: int = 10) -> Dict[str, Any]:
        """Generar sesión gamificada de entrenamiento"""
        
        session = {
            "session_id": str(uuid.uuid4()),
            "user_level": user_level,
            "tasks": [],
            "total_score": 0,
            "cultural_intelligence_gained": 0,
            "session_stats": {
                "correct_answers": 0,
                "total_tasks": session_length,
                "avg_response_time": 0,
                "cultural_patterns_learned": set()
            }
        }
        
        # Generar tareas progresivas
        for i in range(session_length):
            # Aumentar dificultad gradualmente
            difficulty = min(5, user_level + (i // 3))
            
            # Variar tipos de tarea
            task_types = list(self.task_templates.keys())
            task_type = task_types[i % len(task_types)]
            
            task = self.generate_visual_task(task_type, difficulty)
            session["tasks"].append(asdict(task))
        
        return session

# Demo y testing
def demo_corruptcha_visual():
    """Demo del sistema de clasificación visual CORRUPTCHA"""
    
    print("\n" + "="*100)
    print("🚀 CORRUPTCHA VISUAL CLASSIFICATION - DEMO")
    print("Micro-tareas visuales estilo Google perro/muffin para compliance argentino")
    print("✅ Inspirado en el modelo CAPTCHA de Google")
    print("="*100)
    
    engine = CorruptchaVisualEngine()
    
    # Generar diferentes tipos de tareas
    task_types = ["risk_classification", "euphemism_detection", "family_networks"]
    
    for i, task_type in enumerate(task_types, 1):
        print(f"\n📊 TAREA {i}: {task_type.upper().replace('_', ' ')}")
        print("-" * 60)
        
        # Generar tarea
        task = engine.generate_visual_task(task_type, difficulty=3)
        
        print(f"❓ {task.question}")
        print(f"🎯 Tipo: {task.task_type}")
        print(f"⚡ Dificultad: {task.difficulty_level}/5")
        print(f"📜 Referencia: {task.legal_reference}")
        
        print(f"\n📋 OPCIONES:")
        for j, option in enumerate(task.options, 1):
            visual_cue = option.get("visual_cue", "")
            print(f"  {j}. {visual_cue} {option['text']}")
        
        # Simular respuesta correcta
        correct_option = next((opt for opt in task.options if opt["id"] == task.correct_answer), None)
        if correct_option:
            print(f"\n✅ RESPUESTA CORRECTA: {correct_option['text']}")
        
        # Simular validación
        response_time = random.uniform(5.0, 25.0)
        validation = engine.validate_user_response(task, task.correct_answer, response_time)
        
        print(f"📊 RESULTADO:")
        print(f"  • Correcto: {validation['is_correct']}")
        print(f"  • Score: {validation['score']}/100")
        print(f"  • Tiempo: {response_time:.1f}s")
        
        print(f"\n💡 EXPLICACIÓN CULTURAL:")
        print(f"  {validation['cultural_learning']}")
    
    # Generar sesión gamificada
    print(f"\n🎮 GENERANDO SESIÓN GAMIFICADA:")
    print("-" * 60)
    
    session = engine.generate_gamified_session(user_level=2, session_length=5)
    
    print(f"Session ID: {session['session_id']}")
    print(f"Nivel usuario: {session['user_level']}")
    print(f"Total tareas: {session['session_stats']['total_tasks']}")
    
    print(f"\n📋 TAREAS EN LA SESIÓN:")
    for i, task_data in enumerate(session['tasks'], 1):
        task_obj = VisualTask(**task_data)
        print(f"  {i}. {task_obj.task_type} (Dificultad {task_obj.difficulty_level})")
        print(f"     '{task_obj.question}'")
        print(f"     Opciones: {len(task_obj.options)}")
    
    print(f"\n🏆 COMPARACIÓN vs GOOGLE CAPTCHA:")
    print("┌─────────────────────┬─────────────────────┐")
    print("│   GOOGLE CAPTCHA    │    CORRUPTCHA       │")  
    print("├─────────────────────┼─────────────────────┤")
    print("│ 🐕 vs 🧁 (perro/muffin) │ 🚨 vs ✅ (riesgo/normal)  │")
    print("│ Entrenamiento IA    │ Inteligencia cultural│")
    print("│ Reconocimiento      │ Compliance argentino │")
    print("│ visual general      │ específico          │")
    print("│ Revenue: ads        │ Revenue: B2B SaaS   │")
    print("│ Usuarios: millones  │ Usuarios: empresas  │")
    print("└─────────────────────┴─────────────────────┘")
    
    print(f"\n💰 MODELO DE MONETIZACIÓN:")
    print("✅ Empresas necesitan verificar compliance")
    print("✅ Empleados clasifican casos reales argentinos")  
    print("✅ Generamos dataset cultural único")
    print("✅ Vendemos IA entrenada + datasets + APIs")
    print("✅ Competimos vs SAP GRC con ventaja cultural")
    
    print(f"\n🚀 VENTAJA vs HERRAMIENTAS INTERNACIONALES:")
    print("❌ SAP GRC: Busca 'bribery' → No detecta 'regalito'")
    print("❌ PwC Risk: Busca 'corruption' → No detecta 'por izquierda'")  
    print("❌ EY Compliance: Genérico → No detecta 'cuñado', 'primo'")
    print("✅ CORRUPTCHA: Entrenado con CASOS REALES argentinos")
    print("✅ Dataset cultural que NO EXISTE en mercado global")
    
    print(f"\n⚡ PRÓXIMOS PASOS:")
    print("1. 🎨 Crear interfaz visual real (React + Canvas)")
    print("2. 📱 App móvil para micro-tareas gamificadas")
    print("3. 🤖 Integrar con Moonshot AI para análisis avanzado")
    print("4. 📊 Dashboard analytics para empresas")
    print("5. 🌎 Expansión: Brasil (jeitinho), Colombia, México")

if __name__ == "__main__":
    demo_corruptcha_visual()