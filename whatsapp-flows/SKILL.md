---
name: WhatsApp Business Flows
description: Guía avanzada de WhatsApp Business — flujos conversacionales, catálogos, respuestas automáticas, y integración con la landing page.
---

# 💬 WhatsApp Business Flows — Skill Guide

## Cuándo usar esta skill
- Al configurar WhatsApp Business para un cliente
- Al crear flujos automáticos de conversación
- Al integrar WhatsApp con la landing page
- Al crear un catálogo de servicios en WhatsApp

---

## 1. WhatsApp Button Flotante (Landing Page)

### HTML + CSS
```html
<!-- Botón flotante de WhatsApp -->
<a href="https://wa.me/5233XXXXXXXX?text=Hola%2C%20quiero%20agendar%20una%20consulta%20con%20la%20Dra.%20Tabatha"
   class="whatsapp-float"
   target="_blank"
   rel="noopener"
   aria-label="Contactar por WhatsApp">
  <svg viewBox="0 0 24 24" width="28" height="28" fill="white">
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/>
    <path d="M12 0C5.373 0 0 5.373 0 12c0 2.625.846 5.059 2.284 7.034L.789 23.492a.5.5 0 00.611.611l4.458-1.495A11.94 11.94 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 22c-2.327 0-4.47-.747-6.22-2.016l-.435-.324-2.636.884.884-2.636-.324-.435A9.96 9.96 0 012 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z"/>
  </svg>
</a>

<style>
.whatsapp-float {
  position: fixed;
  bottom: 24px;
  left: 24px;
  width: 56px;
  height: 56px;
  background: #25D366;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 16px rgba(37,211,102,0.4);
  z-index: 999;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  text-decoration: none;
}
.whatsapp-float:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 24px rgba(37,211,102,0.5);
}

/* Animación de attention */
@keyframes whatsapp-pulse {
  0% { box-shadow: 0 0 0 0 rgba(37,211,102,0.4); }
  70% { box-shadow: 0 0 0 15px rgba(37,211,102,0); }
  100% { box-shadow: 0 0 0 0 rgba(37,211,102,0); }
}
.whatsapp-float {
  animation: whatsapp-pulse 2s infinite;
}
</style>
```

### Mensaje Pre-llenado con Contexto
```javascript
// Botón de WhatsApp contextualizado según la sección
document.querySelectorAll('[data-wa-service]').forEach(btn => {
  const service = btn.dataset.waService;
  const messages = {
    'general': 'Hola, quiero información sobre los servicios de la Dra. Tabatha.',
    'primera-consulta': 'Hola, quiero agendar mi primera consulta psiquiátrica.',
    'seguimiento': 'Hola, necesito agendar mi consulta de seguimiento.',
    'en-linea': 'Hola, me interesa una consulta en línea.',
    'urgente': 'Hola, necesito atención urgente. ¿Hay disponibilidad hoy?'
  };
  const msg = encodeURIComponent(messages[service] || messages['general']);
  btn.href = `https://wa.me/5233XXXXXXXX?text=${msg}`;
});
```

---

## 2. WhatsApp Business App — Setup

### Configuración Básica
```
1. Descargar WhatsApp Business (no el normal)
2. Registrar con número del profesionista
3. Perfil de negocio:
   → Nombre: "Dra. Tabatha Barron — Psiquiatra"
   → Categoría: Salud
   → Descripción: "Consultas psiquiátricas..."
   → Dirección: Con mapa
   → Horario: L-V 9am-6pm
   → Email
   → Website: landing page
4. Catálogo:
   → Servicio 1: "Consulta Psiquiátrica Inicial" — $800
   → Servicio 2: "Consulta de Seguimiento" — $500
   → Servicio 3: "Consulta en Línea" — $700
5. Respuestas rápidas:
   → /horario → "Nuestro horario es..."
   → /precio → "Los precios de consulta son..."
   → /ubicacion → "Estamos en... [link]"
   → /agendar → "Para agendar: [link cal.com]"
```

---

## 3. Respuestas Automáticas

### Mensaje de Bienvenida
```
¡Hola! 👋 Gracias por contactarnos.

Soy el asistente de la Dra. Tabatha Barron, psiquiatra 
en Guadalajara.

¿En qué podemos ayudarte?
1️⃣ Agendar primera consulta
2️⃣ Consulta de seguimiento
3️⃣ Consulta en línea
4️⃣ Precios y servicios
5️⃣ Ubicación y horarios

Responde con el número de tu opción ✨
```

### Mensaje de Ausencia
```
¡Hola! 👋 Por el momento estamos fuera de horario.

Nuestro horario de atención es:
📅 Lunes a Viernes
🕘 9:00 AM - 6:00 PM

Puedes agendar tu cita directamente aquí:
📋 https://cal.valtyk.com/dra-tabatha

¡Te atenderemos lo antes posible! 😊
```

---

## 4. WhatsApp Cloud API (Avanzado)

### Enviar Template Message
```javascript
// Enviar confirmación de cita (template aprobado por Meta)
async function sendWhatsAppTemplate(phone, name, date, time) {
  const response = await fetch(
    `https://graph.facebook.com/v18.0/${PHONE_NUMBER_ID}/messages`,
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${ACCESS_TOKEN}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        messaging_product: 'whatsapp',
        to: phone,
        type: 'template',
        template: {
          name: 'appointment_confirmation',
          language: { code: 'es_MX' },
          components: [
            {
              type: 'body',
              parameters: [
                { type: 'text', text: name },
                { type: 'text', text: date },
                { type: 'text', text: time }
              ]
            }
          ]
        }
      })
    }
  );
  return response.json();
}
```

---

## 5. Tracking de WhatsApp

```javascript
// Trackear clics en WhatsApp con Google Analytics
document.querySelector('.whatsapp-float').addEventListener('click', () => {
  gtag('event', 'whatsapp_click', {
    event_category: 'conversion',
    event_label: 'floating_button'
  });
});
```
