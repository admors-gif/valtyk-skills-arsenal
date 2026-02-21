---
name: Project Management
description: Gestión de proyectos con múltiples clientes — workflows, tracking, herramientas, y organización para escalar la agencia.
---

# 📋 Project Management — Skill Guide

## Cuándo usar esta skill
- Al manejar múltiples clientes simultáneamente
- Al planificar sprints de trabajo
- Al organizar entregables y deadlines
- Al comunicarte con clientes sobre progreso

---

## 1. Framework de Gestión (Kanban Simple)

### Columnas del Board
```
📥 BACKLOG       → Ideas y requests pendientes
📋 TO DO         → Aprobado, listo para empezar
🔨 IN PROGRESS   → Trabajando activamente
👀 REVIEW        → Esperando feedback del cliente
✅ DONE          → Completado y entregado
📦 DEPLOYED      → Live en producción
```

### Herramientas Gratuitas
```
Notion (recomendada):
  ✓ Boards, listas, calendarios
  ✓ Templates preconstruidos
  ✓ Compartir con clientes
  ✓ API para automatizar
  🔗 https://notion.so

Trello:
  ✓ Kanban visual simple
  ✓ Power-ups gratuitos
  ✓ Fácil de usar
  🔗 https://trello.com

GitHub Projects:
  ✓ Integrado con código
  ✓ Issues como tareas
  ✓ Automaciones con Actions
  🔗 Ya lo tienes

Linear:
  ✓ Moderno y rápido
  ✓ Plan gratis para equipos pequeños
  🔗 https://linear.app
```

---

## 2. Template de Proyecto por Cliente

### Estructura de Carpetas
```
clients/
  └── dra-tabatha-barron/
       ├── README.md           ← Info del cliente
       ├── public/             ← Landing page
       │    ├── index.html
       │    ├── styles/
       │    └── assets/
       ├── firebase.json       ← Config de hosting
       ├── .firebaserc         ← Target de Firebase
       ├── docs/               ← Documentos
       │    ├── propuesta.pdf
       │    └── contrato.pdf
       └── notes/              ← Notas internas
            ├── onboarding.md
            └── feedback.md
```

### README del Cliente
```markdown
# Dra. Tabatha Barron — Psiquiatra
## Info del Proyecto
- **Estado:** 🟢 Activo
- **Paquete:** Growth ($5,000 setup + $1,200/mes)
- **Fecha inicio:** Feb 2026
- **URL:** tabatha-barron.valtyk.com
- **Cal.com:** cal.valtyk.com/dra-tabatha

## Contacto
- Email: tabatha@ejemplo.com
- WhatsApp: +52 33 XXXX XXXX

## Entregables
- [x] Landing page
- [x] Cal.com configurado
- [ ] Google Business Profile
- [ ] SMTP configurado
- [ ] Google Analytics

## Pagos
| Fecha | Concepto | Monto | Estado |
|-------|----------|-------|--------|
| Feb 2026 | Setup (50%) | $2,500 | ✅ Pagado |
| Feb 2026 | Setup (50%) | $2,500 | ⏳ Pendiente |
| Mar 2026 | Mensualidad | $1,200 | 📅 Programado |
```

---

## 3. Workflow Semanal

```
LUNES:
  □ Revisar tareas pendientes de todos los clientes
  □ Priorizar trabajo de la semana
  □ Revisar reportes de analytics

MARTES-JUEVES:
  □ Ejecutar tareas de desarrollo
  □ Crear contenido/copy
  □ Reuniones con clientes (si aplica)

VIERNES:
  □ Review del trabajo de la semana
  □ Enviar updates a clientes
  □ Planificar siguiente semana
  □ Hacer backups

PRIMER LUNES DEL MES:
  □ Generar reportes mensuales
  □ Enviar reportes a clientes
  □ Revisar pagos/cobranza
  □ Evaluar métricas del negocio
```

---

## 4. Comunicación con Clientes

### Canales
```
WhatsApp → Comunicación rápida, preguntas urgentes
Email → Updates formales, reportes, propuestas
Llamada → Onboarding, reviews, estrategia
Loom → Explicar cambios visuales (grabación de pantalla gratis)
```

### Templates de Comunicación

#### Update Semanal
```
Hola Dr./Dra. [Nombre] 👋

Update de esta semana:

✅ Completado:
- [Tarea 1]
- [Tarea 2]

🔨 En progreso:
- [Tarea 3] — estará listo el [fecha]

📋 Necesito de usted:
- [Info o aprobación que necesitas]

¿Alguna duda? ¡Aquí estoy!

Saludos,
Tomas — Valtyk
```

#### Solicitud de Feedback
```
Hola Dr./Dra. [Nombre],

Su [landing page / reporte / etc.] está lista para revisión:
🔗 [link]

Por favor revise y confirme:
1. ¿Los textos están correctos?
2. ¿Las fotos son las que desea?
3. ¿Algo que quiera cambiar?

Si todo está bien, responda "Aprobado ✅" y procedemos 
al lanzamiento.

Saludos,
Tomas
```

---

## 5. Tracking de Horas (Opcional)

```
Herramientas gratuitas:
  - Toggl Track (gratis hasta 5 personas)
  - Clockify (gratis ilimitado)

¿Para qué trackear horas?
  - Saber cuánto realmente cuesta cada cliente
  - Identificar clientes que toman demasiado tiempo
  - Justificar subida de precios
  - Entender tu rentabilidad real

Meta: Cada cliente no debe tomar más de 8h/mes
  en mantenimiento (paquete Growth)
```
