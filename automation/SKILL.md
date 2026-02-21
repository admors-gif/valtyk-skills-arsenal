---
name: Automatización & Integraciones
description: Guía de automatización con n8n, Cal.com API, WhatsApp Business, email marketing automation, y workflows para escalar la operación de la agencia.
---

# 🤖 Automatización & Integraciones — Skill Guide

## Cuándo usar esta skill
- Al configurar Cal.com para un nuevo cliente
- Al crear workflows de n8n para automatizar procesos
- Al integrar WhatsApp, email, o Google Calendar
- Al diseñar el flujo de onboarding de un cliente nuevo

---

## 1. Workflows de n8n para la Agencia

### Workflow: Notificación de Nueva Cita (Cal.com → WhatsApp/Email)
```
Trigger: Cal.com Webhook (nueva reserva)
  ↓
Extraer datos: nombre, email, fecha, hora, servicio
  ↓
Paralelo:
  ├→ Enviar email de confirmación al paciente
  ├→ Enviar WhatsApp al paciente (Twilio/WA Business API)
  └→ Notificar al profesionista por email/WhatsApp
  ↓
Guardar en Google Sheets (registro de citas)
```

### Workflow: Recordatorio de Cita (-24h)
```
Trigger: Schedule (cada hora)
  ↓
Consultar Google Sheets/Cal.com API: citas de mañana
  ↓
Para cada cita:
  ├→ Enviar email de recordatorio
  ├→ Enviar WhatsApp de recordatorio
  └→ Incluir: hora, dirección, Google Maps link
```

### Workflow: Solicitud de Review Post-Cita (+24h)
```
Trigger: Schedule (cada mañana)
  ↓
Consultar citas completadas ayer
  ↓
Para cada cita completada:
  ├→ Enviar email: "¿Cómo fue tu experiencia?"
  └→ Incluir link directo a Google Reviews
```

### Workflow: Reporte Semanal Automático
```
Trigger: Schedule (lunes 8am)
  ↓
Recopilar datos:
  ├→ Google Analytics API: visitas de la semana
  ├→ Cal.com API: citas agendadas
  └→ Google Search Console API: impresiones/clics
  ↓
Formatear reporte
  ↓
Enviar por email al profesionista y a Valtyk
```

### Workflow: Onboarding de Nuevo Cliente
```
Trigger: Formulario de onboarding completado
  ↓
Crear carpeta en Google Drive
  ↓
Crear usuario en Cal.com (API)
  ↓
Configurar event types en Cal.com
  ↓
Crear registro en Google Sheets (clientes)
  ↓
Enviar email de bienvenida al cliente
  ↓
Crear tarea en proyecto (seguimiento)
  ↓
Notificar a Valtyk: "Nuevo cliente onboardeado ✅"
```

---

## 2. Cal.com — Configuración por Cliente

### Checklist de Setup
```
Para cada nuevo cliente en Cal.com:

1. CUENTA
   - [ ] Crear usuario con email del cliente
   - [ ] Asignar contraseña segura
   - [ ] Configurar timezone (America/Mexico_City)
   - [ ] Subir foto de perfil
   - [ ] Configurar bio/descripción
   - [ ] Username personalizado (ej: dra-tabatha)

2. EVENT TYPES
   - [ ] "Primera Consulta" (duración: 40-60 min, precio: $XXX)
   - [ ] "Consulta de Seguimiento" (duración: 20-30 min, precio: $XXX)
   - [ ] "Consulta en Línea" (duración: 30 min, ubicación: Google Meet)
   
   Para cada event type configurar:
   - [ ] Título descriptivo
   - [ ] Duración
   - [ ] Precio (si aplica)
   - [ ] Ubicación (presencial / online / ambos)
   - [ ] Descripción
   - [ ] Buffer time (15 min entre citas)
   - [ ] Booking limits (máx citas por día)
   - [ ] Preguntas al agendar (nombre, teléfono, motivo)

3. DISPONIBILIDAD
   - [ ] Horario de lunes a viernes
   - [ ] Horario de comida bloqueado
   - [ ] Días festivos bloqueados
   - [ ] Vacaciones configuradas

4. INTEGRACIONES
   - [ ] Google Calendar conectado
   - [ ] Webhook configurado para n8n
   - [ ] Email de notificaciones configurado

5. EMBED EN LANDING PAGE
   - [ ] Widget de Cal.com integrado
   - [ ] Estilo personalizado (colores del cliente)
   - [ ] Botón de CTA apuntando al booking
```

### Código para Embedir Cal.com en Landing
```html
<!-- Opción 1: Botón que abre modal -->
<button
  data-cal-link="dra-tabatha/primera-consulta"
  data-cal-config='{"layout":"month_view","theme":"dark"}'
  style="background: var(--primary); color: white; padding: 16px 32px; border-radius: 8px; cursor: pointer;"
>
  Agenda tu Cita
</button>

<!-- Script de Cal.com (agregar antes de </body>) -->
<script>
  (function (C, A, L) {
    let p = function (a, ar) { a.q.push(ar); };
    let d = C.document;
    C.Cal = C.Cal || function () { let cal = C.Cal;
      let ar = arguments;
      if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement("script")).src = A;
        cal.loaded = true; }
      if (ar[0] === L) { const api = function () { p(api, arguments); };
        const namespace = ar[1]; api.q = api.q || [];
        typeof namespace === "string" ? (cal.ns[namespace] = api) && p(api, ar) : p(cal, ar);
        return; }
      p(cal, ar);
    };
  })(window, "https://app.cal.com/embed/embed.js", "init");

  Cal("init", {origin:"https://cal.valtyk.com"});
  Cal("ui", {
    "styles": {"branding": {"brandColor": "#2E86AB"}},
    "hideEventTypeDetails": false,
    "layout": "month_view"
  });
</script>

<!-- Opción 2: Inline embed (calendario visible) -->
<div id="cal-embed" style="width:100%;height:600px;overflow:auto;"></div>
<script>
  Cal("inline", {
    elementOrSelector: "#cal-embed",
    calLink: "dra-tabatha/primera-consulta",
    layout: "month_view",
    config: { theme: "dark" }
  });
</script>
```

---

## 3. WhatsApp Business Automation

### Opción 1: Twilio WhatsApp API
```javascript
// Enviar mensaje de confirmación de cita
const accountSid = 'TWILIO_SID';
const authToken = 'TWILIO_TOKEN';
const client = require('twilio')(accountSid, authToken);

async function sendWhatsAppConfirmation(phone, patientName, date, time, doctorName) {
  await client.messages.create({
    from: 'whatsapp:+14155238886', // número de Twilio
    to: `whatsapp:+52${phone}`,
    body: `✅ *Cita Confirmada*\n\n` +
          `Hola ${patientName},\n\n` +
          `Tu cita con ${doctorName} está confirmada:\n` +
          `📅 ${date}\n` +
          `🕐 ${time}\n` +
          `📍 Clínica Naluum, Guadalajara\n\n` +
          `Si necesitas reagendar, responde a este mensaje.\n\n` +
          `_Valtyk Solutions_`
  });
}
```

### Opción 2: WhatsApp Business Cloud API (gratis hasta 1000 msgs/mes)
```
Setup:
1. Crear cuenta en Meta Business Suite
2. Crear app en developers.facebook.com
3. Activar WhatsApp en la app
4. Obtener token de acceso
5. Registrar número de WhatsApp Business

En n8n:
- Usar nodo "HTTP Request"
- POST a https://graph.facebook.com/v18.0/{phone-number-id}/messages
- Header: Authorization: Bearer {token}
- Body: template message con variables
```

### Templates de Mensajes WhatsApp

```
📅 CONFIRMACIÓN:
"✅ Cita confirmada

Hola {{nombre}}, tu cita con {{doctor}} es:
📅 {{fecha}}
🕐 {{hora}}
📍 {{dirección}}

¿Necesitas reagendar? Responde aquí."

⏰ RECORDATORIO (24h antes):
"⏰ Recordatorio de cita

Hola {{nombre}}, recuerda que mañana tienes cita con {{doctor}}:
📅 {{fecha}}
🕐 {{hora}}
📍 {{dirección}}

📱 Google Maps: {{link_maps}}

¡Te esperamos!"

⭐ POST-CITA (24h después):
"Hola {{nombre}} 👋

¿Cómo te fue en tu consulta con {{doctor}}?

Si tu experiencia fue positiva, nos ayudaría mucho tu opinión:
⭐ {{link_review}}

¡Gracias!"
```

---

## 4. Email Automation (SMTP)

### Configuración SMTP en Cal.com
```env
# Opción 1: Gmail SMTP
EMAIL_FROM=citas@valtyk.com
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=tucorreo@gmail.com
SMTP_PASSWORD=app-password-de-16-chars
SMTP_SECURE=false

# Opción 2: Brevo (ex Sendinblue) — 300 emails/día gratis
EMAIL_FROM=citas@valtyk.com
SMTP_HOST=smtp-relay.brevo.com
SMTP_PORT=587
SMTP_USER=tu-email-brevo
SMTP_PASSWORD=tu-smtp-key

# Opción 3: Resend — 3000 emails/mes gratis
EMAIL_FROM=citas@valtyk.com
SMTP_HOST=smtp.resend.com
SMTP_PORT=465
SMTP_USER=resend
SMTP_PASSWORD=re_xxxxxxxxxxxx
SMTP_SECURE=true
```

### Email Templates (HTML)
```html
<!-- Template base para emails de cita -->
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: 'Helvetica', Arial, sans-serif; background: #f5f5f5; margin: 0; padding: 20px; }
    .container { max-width: 600px; margin: 0 auto; background: white; border-radius: 12px; overflow: hidden; }
    .header { background: linear-gradient(135deg, #2E86AB, #1a5276); padding: 30px; text-align: center; color: white; }
    .content { padding: 30px; }
    .cta-btn { display: inline-block; background: #2E86AB; color: white; padding: 14px 28px; border-radius: 8px; text-decoration: none; }
    .footer { padding: 20px; text-align: center; color: #888; font-size: 12px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>✅ Cita Confirmada</h1>
    </div>
    <div class="content">
      <p>Hola <strong>{{nombre}}</strong>,</p>
      <p>Tu cita ha sido agendada exitosamente:</p>
      <table style="width:100%; margin: 20px 0;">
        <tr><td>📅 Fecha:</td><td><strong>{{fecha}}</strong></td></tr>
        <tr><td>🕐 Hora:</td><td><strong>{{hora}}</strong></td></tr>
        <tr><td>👩‍⚕️ Doctor:</td><td><strong>{{doctor}}</strong></td></tr>
        <tr><td>📍 Lugar:</td><td><strong>{{direccion}}</strong></td></tr>
      </table>
      <p style="text-align:center;">
        <a href="{{google_maps_link}}" class="cta-btn">Ver ubicación en Maps</a>
      </p>
    </div>
    <div class="footer">
      <p>Powered by Valtyk Solutions</p>
    </div>
  </div>
</body>
</html>
```

---

## 5. Google OAuth Setup (para Calendar sync)

### Pasos para configurar Google Calendar en Cal.com
```
1. Ir a Google Cloud Console
   → https://console.cloud.google.com

2. Crear proyecto nuevo: "Valtyk-CalCom"

3. Activar APIs:
   → Google Calendar API
   → Google People API (opcional)

4. Configurar OAuth Consent Screen:
   → Type: External
   → App name: "Valtyk Bookings"
   → User support email: tu email
   → Authorized domains: valtyk.com
   → Scopes: calendar.events, calendar.readonly

5. Crear Credentials:
   → OAuth 2.0 Client ID
   → Type: Web application
   → Authorized redirect URIs:
     https://cal.valtyk.com/api/integrations/googlecalendar/callback
   → Guardar Client ID y Client Secret

6. Agregar a Docker env:
   GOOGLE_API_CREDENTIALS={"client_id":"xxx","client_secret":"xxx"}

7. En Cal.com admin/settings:
   → Integrations → Google Calendar → Connect
   → El cliente autoriza con su Google
```

---

## 6. Workflow de Onboarding de Cliente (SOP)

### Proceso Paso a Paso
```
DÍA 1-2: RECOPILACIÓN
━━━━━━━━━━━━━━━━━━━━
□ Enviar formulario de onboarding al cliente:
  - Nombre completo y título
  - Especialidad
  - Servicios que ofrece (con precios y duración)
  - Dirección del consultorio/negocio
  - Teléfono profesional
  - Email profesional
  - Horarios de atención
  - Fotos profesionales (retrato, consultorio, logo)
  - Bio/historia profesional
  - Redes sociales existentes
  - Colores/branding preferidos
  - Competidores relevantes

□ Recibir anticipo (50% del setup)

DÍA 3-5: DESARROLLO
━━━━━━━━━━━━━━━━━━━
□ Crear landing page basada en template
□ Personalizar colores, textos, imágenes
□ Implementar Schema markup
□ Configurar SEO on-page
□ Crear cuenta Cal.com del cliente
□ Configurar event types
□ Configurar disponibilidad
□ Embedir Cal.com en landing
□ Configurar Google Analytics

DÍA 6-8: OPTIMIZACIÓN
━━━━━━━━━━━━━━━━━━━━━
□ Crear Google Business Profile
□ Optimizar GBP (fotos, posts, servicios)
□ Configurar Google Search Console
□ Enviar sitemap
□ Verificar Core Web Vitals
□ Test en mobile

DÍA 9-10: REVISIÓN
━━━━━━━━━━━━━━━━━━
□ Enviar preview al cliente
□ Incorporar feedback
□ Hacer ajustes finales

DÍA 11-14: LANZAMIENTO
━━━━━━━━━━━━━━━━━━━━━━
□ Deplegar landing page
□ Configurar dominio/subdominio
□ Verificar SSL
□ Activar automations (n8n)
□ Enviar email de lanzamiento al cliente
□ Explicar cómo funciona el sistema
□ Recibir pago restante (50%)

POST-LANZAMIENTO:
━━━━━━━━━━━━━━━━━
□ Monitorear Analytics (semana 1)
□ Verificar indexación en Google
□ Primer reporte (30 días)
□ Solicitar review/testimonio al cliente
```

---

## 7. Herramientas & Cuentas Necesarias

### Cuentas que Valtyk necesita tener:
```
GRATIS:
✓ Google Cloud Console (OAuth, APIs)
✓ Google Analytics 4
✓ Google Search Console
✓ Google Business Profile (por cliente)
✓ Firebase (hosting)
✓ Cal.com self-hosted (ya lo tienes)
✓ n8n self-hosted (ya lo tienes)
✓ Canva (plan gratis)
✓ Gamma.app (plan gratis)

OPCIONALES (de pago):
○ Brevo/Resend (SMTP, gratis hasta cierto volumen)
○ Twilio ($0.005/msg WhatsApp)
○ Cloudflare (DNS gratis, proxy gratis)
○ Custom domain (~$200 MXN/año)
```
