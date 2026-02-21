---
name: AI Chatbots & Asistentes
description: Guía para implementar chatbots con IA (GPT, Claude) en landing pages, WhatsApp, y sistemas de atención automatizada para clientes de la agencia.
---

# 🤖 AI Chatbots & Asistentes — Skill Guide

## Cuándo usar esta skill
- Al implementar un chatbot en la landing page de un cliente
- Al crear un asistente de WhatsApp con IA
- Al automatizar atención al cliente con GPT
- Al crear flujos conversacionales inteligentes

---

## 1. Chatbot Embebido en Landing Page

### Opción 1: Widget de Chat con OpenAI API
```html
<!-- Botón flotante de chat -->
<div id="chat-widget" class="chat-widget">
  <button id="chat-toggle" class="chat-toggle">
    <span class="chat-icon">💬</span>
    <span class="chat-badge" id="chat-badge" style="display:none">1</span>
  </button>
  <div id="chat-window" class="chat-window" style="display:none">
    <div class="chat-header">
      <img src="/assets/avatar-bot.webp" alt="Asistente" class="chat-avatar">
      <div>
        <strong>Asistente Virtual</strong>
        <small>En línea • Responde al instante</small>
      </div>
      <button id="chat-close" class="chat-close">✕</button>
    </div>
    <div id="chat-messages" class="chat-messages">
      <div class="message bot">
        ¡Hola! 👋 Soy el asistente virtual de la Dra. Tabatha. 
        ¿En qué puedo ayudarte?
      </div>
    </div>
    <div class="chat-input-area">
      <input type="text" id="chat-input" placeholder="Escribe tu pregunta..." />
      <button id="chat-send">→</button>
    </div>
  </div>
</div>
```

### CSS del Widget
```css
.chat-widget {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 9999;
  font-family: 'Inter', sans-serif;
}
.chat-toggle {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea, #764ba2);
  border: none;
  cursor: pointer;
  box-shadow: 0 4px 20px rgba(102,126,234,0.4);
  font-size: 1.5rem;
  transition: transform 0.2s;
  position: relative;
}
.chat-toggle:hover { transform: scale(1.1); }
.chat-badge {
  position: absolute;
  top: -4px;
  right: -4px;
  background: #f43f5e;
  color: white;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  font-size: 0.7rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
.chat-window {
  position: absolute;
  bottom: 72px;
  right: 0;
  width: 380px;
  max-height: 520px;
  background: #1a1b3a;
  border-radius: 16px;
  border: 1px solid rgba(255,255,255,0.1);
  box-shadow: 0 12px 48px rgba(0,0,0,0.4);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.chat-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px;
  background: rgba(255,255,255,0.05);
  border-bottom: 1px solid rgba(255,255,255,0.08);
  color: white;
}
.chat-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
}
.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.message {
  padding: 10px 14px;
  border-radius: 12px;
  max-width: 85%;
  font-size: 0.88rem;
  line-height: 1.5;
  color: white;
}
.message.bot {
  background: rgba(102,126,234,0.2);
  align-self: flex-start;
  border-bottom-left-radius: 4px;
}
.message.user {
  background: #667eea;
  align-self: flex-end;
  border-bottom-right-radius: 4px;
}
.chat-input-area {
  display: flex;
  padding: 12px;
  gap: 8px;
  border-top: 1px solid rgba(255,255,255,0.08);
}
.chat-input-area input {
  flex: 1;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.12);
  padding: 10px 14px;
  border-radius: 10px;
  color: white;
  outline: none;
}
.chat-input-area button {
  background: #667eea;
  border: none;
  border-radius: 10px;
  width: 40px;
  color: white;
  cursor: pointer;
  font-size: 1.1rem;
}
```

### JavaScript con OpenAI API
```javascript
// Configuración
const OPENAI_API_KEY = 'sk-...'; // NUNCA poner en el frontend — usar un proxy/backend
const SYSTEM_PROMPT = `Eres el asistente virtual de la Dra. Tabatha Barron, psiquiatra en Guadalajara.

REGLAS:
- Responde siempre en español
- Sé amable, empático y profesional
- NO des diagnósticos médicos
- Para cualquier urgencia, sugiere ir a urgencias
- Para agendar cita, envía al link: https://cal.valtyk.com/dra-tabatha
- Horario: Lunes a Viernes 9am-6pm
- Ubicación: Clínica Naluum, Guadalajara
- Servicios: Consulta psiquiátrica ($800), Seguimiento ($500), Consulta en línea ($700)
- Respuestas máximo 3 líneas`;

async function sendToGPT(messages) {
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${OPENAI_API_KEY}`
    },
    body: JSON.stringify({
      model: 'gpt-4o-mini', // Más barato y rápido
      messages: [
        { role: 'system', content: SYSTEM_PROMPT },
        ...messages
      ],
      temperature: 0.7,
      max_tokens: 200
    })
  });
  const data = await response.json();
  return data.choices[0].message.content;
}
```

### Proxy Seguro con n8n (Recomendado)
```
Workflow en n8n:
  Trigger: Webhook POST /api/chat
  ↓
  Recibir mensaje del usuario
  ↓
  Enviar a OpenAI API (con la key guardada en n8n)
  ↓
  Devolver respuesta al frontend
  ↓
  Guardar conversación en Google Sheets (para análisis)
```

---

## 2. Chatbot de WhatsApp con IA

### Arquitectura
```
Usuario envía WhatsApp
  ↓
Twilio/Meta recibe → Webhook a n8n
  ↓
n8n procesa:
  1. Identifica intención (agendar, preguntar, urgencia)
  2. Si es pregunta → Envía a OpenAI → Responde
  3. Si es agendar → Crea cita en Cal.com → Confirma
  4. Si es urgencia → Alerta al profesionista
  ↓
Respuesta enviada por WhatsApp
```

### Intenciones Comunes
```
AGENDAR_CITA → "quiero cita", "agendar", "consulta"
PREGUNTAR_PRECIO → "cuánto cuesta", "precio", "costo"
PREGUNTAR_HORARIO → "horario", "qué días", "disponibilidad"
PREGUNTAR_UBICACION → "dónde", "dirección", "cómo llego"
CANCELAR_CITA → "cancelar", "reagendar", "no puedo ir"
URGENCIA → "emergencia", "crisis", "me quiero hacer daño"
OTRO → Cualquier otra cosa → Responder con IA
```

---

## 3. Embeddings para FAQ Inteligente

### Concepto
```
En lugar de solo GPT (que puede inventar respuestas),
usa embeddings + RAG para que el chatbot SOLO responda
con información real del profesionista.

Pasos:
1. Crear base de conocimiento (FAQ del doctor, servicios, precios)
2. Convertir a embeddings con OpenAI
3. Cuando el usuario pregunta → buscar respuesta similar
4. Usar GPT solo para formatear la respuesta
```

### Base de Conocimiento (ejemplo)
```json
[
  {
    "pregunta": "¿Cuánto cuesta la consulta?",
    "respuesta": "La consulta inicial cuesta $800 MXN y dura 40 minutos. El seguimiento cuesta $500 MXN."
  },
  {
    "pregunta": "¿Ofrecen consultas en línea?",
    "respuesta": "Sí, ofrecemos consultas por videollamada con la misma calidad de atención. Costo: $700 MXN."
  },
  {
    "pregunta": "¿Qué condiciones trata la doctora?",
    "respuesta": "Depresión, ansiedad, insomnio, TDAH, trastorno bipolar, estrés postraumático, entre otros."
  }
]
```

---

## 4. Costos Estimados

```
GPT-4o-mini:
  Input: $0.15 / 1M tokens
  Output: $0.60 / 1M tokens
  ~$0.001 por conversación (~3 mensajes)
  1000 conversaciones/mes ≈ $1 USD

GPT-4o:
  Input: $2.50 / 1M tokens
  Output: $10.00 / 1M tokens
  ~$0.01 por conversación
  1000 conversaciones/mes ≈ $10 USD

WhatsApp Business API (Meta):
  1000 conversaciones/mes gratis
  Después: ~$0.03-0.08 por conversación
```

---

## 5. Herramientas
- [OpenAI API](https://platform.openai.com/) — GPT-4o-mini
- [Botpress](https://botpress.com/) — Builder de chatbots visual, gratis
- [Typebot](https://typebot.io/) — Open source, self-hosted
- [n8n](https://n8n.io/) — Orquestar flujo del chatbot
