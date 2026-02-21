---
name: Cal.com Setup & Client Onboarding
description: Guía completa paso a paso para configurar Cal.com para un nuevo cliente — crear usuario, bypass email verification, event types, disponibilidad, SMTP, y embed en landing page. Basada en experiencia real con workarounds probados.
---

# 📅 Cal.com Setup & Client Onboarding — Skill Guide

## Cuándo usar esta skill
- Al agregar un nuevo cliente al sistema de reservación Cal.com
- Al crear usuarios, event types, o configurar disponibilidad
- Al integrar el calendario de booking en una landing page
- Al solucionar problemas de 404, verificación de email, o SMTP
- Al actualizar la configuración de un cliente existente

---

## Contexto de la Instancia

```
URL: https://cal.valtyk.com
Image: calcom.docker.scarf.sh/calcom/cal.com
Port: 3005 (internal 3000)
DB: PostgreSQL 14 (container: calcom-db)
Redis: redis:7-alpine (container: calcom-redis)
Network: calcom-network
Hostinger VPS ID: 1375702
Project Name: calcom
```

---

## 1. Crear Usuario para Nuevo Cliente

### Método recomendado: Crear via Admin Panel
1. Login como admin en `https://cal.valtyk.com/auth/login`
2. Settings → Admin → Users → Invite User
3. Enviar invitación con email del cliente

### Método alternativo: Crear via SQL (cuando SMTP no funciona)

> ⚠️ **IMPORTANTE**: Cal.com requiere que el password sea hasheado con bcrypt.
> Puedes generar el hash con: `htpasswd -bnBC 10 "" "MiPassword123!" | tr -d ':'`

```yaml
# docker-compose para ejecutar SQL temporal
services:
  db-task:
    image: postgres:14
    networks:
      - calcom-network
    restart: "no"
    entrypoint:
      - sh
      - -c
      - |
        # Generar hash bcrypt del password
        # Usar hash pre-generado o tool dentro del container
        
        PGPASSWORD=${DB_PASSWORD} psql -h calcom-db -U calcom_user -d calcom -c "
        INSERT INTO \"users\" (
          email, username, name, \"emailVerified\",
          \"completedOnboarding\", \"timeZone\", locale,
          \"identityProvider\", role, password
        ) VALUES (
          'email@cliente.com',
          'nombre-profesional',
          'Dr. Nombre Apellido',
          NOW(),
          true,
          'America/Mexico_City',
          'es',
          'CAL',
          'USER',
          '\$2a\$10\$HASH_AQUI'
        ) RETURNING id, email, username;
        "

networks:
  calcom-network:
    external: true
```

### ⚠️ Gotchas del usuario
- **Email Verification**: Si no hay SMTP configurado, Cal.com no puede enviar emails de verificación. Solución: setear `emailVerified` = `NOW()` directamente en la DB.
- **completedOnboarding**: DEBE ser `true` para que la página pública funcione. Si es `false`, el usuario es redirigido al onboarding y su perfil da 404.
- **Username**: Debe ser lowercase, sin espacios, con guiones. Ejemplo: `dra-tabatha`, `carlos-abogado`.
- **Password length**: El admin de Cal.com requiere passwords de mínimo 15 caracteres. Los usuarios normales no tienen esta restricción.

---

## 2. Bypass Email Verification

Cuando no hay SMTP configurado aún, actualizar directamente en la DB:

```sql
UPDATE "users" 
SET "emailVerified" = NOW() 
WHERE email = 'email@cliente.com';
```

Ejecutar via proyecto temporal de Docker en Hostinger:

```yaml
services:
  db-fix:
    image: postgres:14
    networks:
      - calcom-network
    restart: "no"
    entrypoint:
      - sh
      - -c
      - |
        PGPASSWORD=${DB_PASSWORD} psql -h calcom-db -U calcom_user -d calcom -c "
        UPDATE \"users\" SET \"emailVerified\" = NOW() WHERE email = 'email@cliente.com';
        "
        echo "=== Verification bypassed ==="

networks:
  calcom-network:
    external: true
```

---

## 3. Configurar Disponibilidad

### Via UI (Recomendado)
1. Login como el cliente en Cal.com
2. Settings → Availability → Default Schedule
3. Configurar horarios por día de la semana
4. Guardar

### Via SQL (Si la UI no funciona)
```sql
-- Crear schedule base
INSERT INTO "Schedule" (
  "userId", name, "timeZone"
) VALUES (
  USER_ID, 'Horario de Atención', 'America/Mexico_City'
) RETURNING id;

-- Agregar slots (ejemplo: Lun-Vie 9:00-18:00)
-- Días: 1=Lunes, 2=Martes, ... 5=Viernes
INSERT INTO "Availability" ("scheduleId", days, "startTime", "endTime")
VALUES
  (SCHEDULE_ID, '{1}', '1970-01-01 09:00:00', '1970-01-01 18:00:00'),
  (SCHEDULE_ID, '{2}', '1970-01-01 09:00:00', '1970-01-01 18:00:00'),
  (SCHEDULE_ID, '{3}', '1970-01-01 09:00:00', '1970-01-01 18:00:00'),
  (SCHEDULE_ID, '{4}', '1970-01-01 09:00:00', '1970-01-01 18:00:00'),
  (SCHEDULE_ID, '{5}', '1970-01-01 09:00:00', '1970-01-01 18:00:00');
```

---

## 4. Crear Event Types

### ⚠️ REGLA CRÍTICA: Crear via UI, NO via SQL

> **APRENDIZAJE CLAVE**: Los event types creados directamente via SQL pueden resultar en errores 404 en la página pública. Cal.com tiene lógica interna al crear events (genera UUIDs, asociaciones de hosts, metadata) que NO se replican con un simple INSERT.

### Proceso recomendado:
1. **Login como el cliente** en `https://cal.valtyk.com/auth/login`
2. Ir a **Event Types** → **+ New Event Type**
3. Configurar:
   - **Title**: Nombre del servicio (ej: "Consulta Psiquiátrica")
   - **URL slug**: ruta corta (ej: `consulta`)
   - **Duration**: minutos (ej: 40)
   - **Description**: descripción del servicio
   - **Location**: "In Person" con dirección completa O "Google Meet" para online
4. **Guardar** y verificar que la URL pública funciona

### Corregir título/descripción via SQL (si necesario):
```sql
UPDATE "EventType" 
SET title = 'Título Correcto',
    description = 'Descripción completa del servicio.'
WHERE id = EVENT_ID;
```

### Eliminar event type via SQL:
```sql
DELETE FROM "EventType" WHERE id = EVENT_ID;
```

---

## 5. Configurar SMTP para Emails

### Gmail SMTP con App Password

1. **Obtener App Password de Gmail**:
   - Ir a [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   - Seleccionar "Mail" → Crear
   - Copiar el password de 16 caracteres (sin espacios)

2. **Agregar variables al proyecto Cal.com en Hostinger**:
   
   Usar `mcp_hostinger_VPS_createNewProjectV1` para actualizar el proyecto `calcom` con estas variables de entorno adicionales:

   ```env
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=correo@gmail.com
   SMTP_PASSWORD=xxxx xxxx xxxx xxxx  # Sin espacios al guardarlo
   ```

   Y estas variables en el docker-compose del servicio calcom:
   ```yaml
   - EMAIL_FROM=citas@valtyk.com
   - EMAIL_FROM_NAME=Valtyk Bookings
   - SMTP_HOST=${SMTP_HOST}
   - SMTP_PORT=${SMTP_PORT}
   - SMTP_FROM=${SMTP_USER}
   - SMTP_USER=${SMTP_USER}
   - SMTP_PASSWORD=${SMTP_PASSWORD}
   ```

3. **Reiniciar Cal.com** para que tome las nuevas variables:
   ```
   mcp_hostinger_VPS_restartProjectV1(calcom, 1375702)
   ```

### Alternativas SMTP gratuitas:
| Servicio | Límite Gratis | Host | Puerto |
|----------|--------------|------|--------|
| Gmail | 500/día | smtp.gmail.com | 587 |
| Brevo | 300/día | smtp-relay.brevo.com | 587 |
| Resend | 3000/mes | smtp.resend.com | 465 |

---

## 6. Integrar Cal.com en Landing Page

### Paso 1: Agregar el embed script en `<head>`

```html
<!-- Cal.com Embed -->
<script type="text/javascript">
  (function (C, A, L) { let p = function (a, ar) { a.q.push(ar); }; let d = C.document; C.Cal = C.Cal || function () { let cal = C.Cal; let ar = arguments; if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement("script")).src = A; cal.loaded = true; } if (ar[0] === L) { const api = function () { p(api, arguments); }; const namespace = ar[1]; api.q = api.q || []; if(typeof namespace === "string"){cal.ns[namespace] = cal.ns[namespace] || api;p(cal.ns[namespace], ar);p(cal, ["initNamespace", namespace]);} else p(cal, ar); return;} p(cal, ar); }; })(window, "https://cal.valtyk.com/embed/embed.js", "init");
  Cal("init", {origin:"https://cal.valtyk.com"});
  Cal("ui", {
    "theme": "light",
    "styles": {"branding": {"brandColor": "#6C63FF"}},
    "hideEventTypeDetails": false,
    "layout": "month_view"
  });
</script>
```

> **NOTA**: La URL del embed script DEBE apuntar a tu instancia: `https://cal.valtyk.com/embed/embed.js`, NO a `app.cal.com`.

### Paso 2: Botones CTA con popup modal

Agregar `data-cal-link` a cualquier botón/enlace para que abra el calendario en popup:

```html
<a href="#booking"
   class="btn btn--primary btn--lg"
   data-cal-link="USERNAME/SLUG"
   data-cal-config='{"layout":"month_view","theme":"light"}'>
  <i data-lucide="calendar-check"></i>
  Agenda tu Consulta
</a>
```

Reemplazar:
- `USERNAME` → username del cliente (ej: `dra-tabatha`)
- `SLUG` → slug del event type (ej: `consulta`)

### Paso 3: Sección de booking inline (calendario embebido)

```html
<!-- BOOKING SECTION -->
<section class="section section--alt booking" id="booking">
  <div class="container">
    <div class="section__header reveal">
      <span class="overline">Agenda en Línea</span>
      <h2>Reserva tu <span class="text-gradient">Consulta</span></h2>
      <p class="lead max-w-prose mx-auto">
        Selecciona el día y horario que mejor se adapte a tu agenda.
        La confirmación es inmediata.
      </p>
    </div>

    <div class="booking__calendar reveal" id="bookingCalendar">
      <div class="booking__loading" id="bookingLoading">
        <div class="booking__spinner"></div>
        <p>Cargando calendario...</p>
      </div>
    </div>

    <div class="booking__alt reveal text-center" style="margin-top: var(--space-8)">
      <p class="booking__alt-text">
        ¿Prefieres agendar por WhatsApp? 
        <a href="https://wa.me/52XXXXXXXXXX?text=MENSAJE" 
           target="_blank" rel="noopener" class="booking__wa-link">Escríbeme aquí</a>
      </p>
    </div>
  </div>
</section>
```

### Paso 4: Script de inicialización inline embed

Agregar antes de `</body>`:

```html
<script>
  (function() {
    function initCalEmbed() {
      if (!window.Cal) {
        setTimeout(initCalEmbed, 500);
        return;
      }

      var calContainer = document.getElementById('bookingCalendar');
      var loadingEl = document.getElementById('bookingLoading');
      
      var embedDiv = document.createElement('div');
      embedDiv.id = 'cal-embed-inline';
      embedDiv.style.width = '100%';
      embedDiv.style.minHeight = '600px';
      embedDiv.style.overflow = 'auto';
      calContainer.appendChild(embedDiv);

      Cal('inline', {
        elementOrSelector: '#cal-embed-inline',
        calLink: 'USERNAME/SLUG',
        layout: 'month_view',
        config: { theme: 'light' }
      });

      setTimeout(function() {
        if (loadingEl) loadingEl.style.display = 'none';
      }, 2000);
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function() {
        setTimeout(initCalEmbed, 1000);
      });
    } else {
      setTimeout(initCalEmbed, 1000);
    }
  })();
</script>
```

### Paso 5: CSS para la sección de booking

```css
/* BOOKING SECTION */
.booking {
    padding-bottom: var(--space-16);
}

.booking__calendar {
    max-width: 1100px;
    margin: 0 auto;
    background: var(--color-white);
    border-radius: var(--radius-2xl);
    box-shadow: var(--shadow-xl);
    border: 1px solid var(--color-gray-100);
    overflow: hidden;
    min-height: 650px;
    position: relative;
}

.booking__loading {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: var(--space-4);
    background: var(--color-white);
    z-index: 1;
}

.booking__spinner {
    width: 40px;
    height: 40px;
    border: 3px solid var(--color-gray-200);
    border-top-color: var(--color-primary);
    border-radius: 50%;
    animation: booking-spin 0.8s ease-in-out infinite;
}

@keyframes booking-spin {
    to { transform: rotate(360deg); }
}

.booking__alt-text {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: var(--space-2);
    font-size: var(--text-sm);
    color: var(--color-gray-600);
}

.booking__wa-link {
    color: var(--color-primary);
    font-weight: var(--weight-semibold);
    text-decoration: underline;
    text-underline-offset: 3px;
}

@media (max-width: 480px) {
    .booking__calendar {
        min-height: 480px;
        margin-left: calc(-1 * var(--space-4));
        margin-right: calc(-1 * var(--space-4));
    }
}
```

---

## 7. Ejecutar SQL Temporal (via Hostinger MCP)

Patrón reutilizable para ejecutar cualquier SQL contra la DB de Cal.com:

```python
# Usar mcp_hostinger_VPS_createNewProjectV1

project_name = "calcom-sql-task"  # Nombre descriptivo
virtualMachineId = 1375702

content = """
services:
  db-task:
    image: postgres:14
    networks:
      - calcom-network
    restart: "no"
    entrypoint:
      - sh
      - -c
      - |
        echo "=== Ejecutando SQL ==="
        PGPASSWORD=DB_PASSWORD psql -h calcom-db -U calcom_user -d calcom -c "
        TU_QUERY_AQUI;
        "
        echo "=== DONE ==="

networks:
  calcom-network:
    external: true
"""

# Después de ejecutar:
# 1. Verificar logs: mcp_hostinger_VPS_getProjectLogsV1
# 2. Limpiar: mcp_hostinger_VPS_deleteProjectV1
```

> **SIEMPRE** eliminar el proyecto temporal después de obtener los logs.

---

## 8. Troubleshooting

### Error 404 en página de booking
**Causa 1**: `completedOnboarding` es `false`
```sql
UPDATE "users" SET "completedOnboarding" = true WHERE id = USER_ID;
```

**Causa 2**: Event type creado via SQL (falta metadata interna)
→ Eliminar el event creado por SQL y recrearlo via la UI

**Causa 3**: Cache de Cal.com
→ Reiniciar el proyecto: `mcp_hostinger_VPS_restartProjectV1`

### Contenedor calcom-app "Dead" o "Created" pero no arranca
**Causa**: Conflicto de nombres al recrear el proyecto
**Solución**:
1. `mcp_hostinger_VPS_stopProjectV1` → esperar
2. `mcp_hostinger_VPS_startProjectV1` → esperar
3. Verificar con `mcp_hostinger_VPS_getProjectContainersV1`

### No se envían emails de confirmación
1. Verificar SMTP vars: `mcp_hostinger_VPS_getProjectContentsV1`
2. Gmail App Password sin espacios en el env
3. Cuenta Gmail con 2FA habilitado (requisito para App Passwords)
4. Reiniciar Cal.com después de cambiar env vars

### Caracteres especiales en el navegador (acentos)
Los subagentes del browser tienen problemas escribiendo `á`, `é`, `í`, `ó`, `ú`, `ñ` directamente.
**Workaround**: Usar JavaScript para insertar texto con acentos:
```javascript
document.querySelector('input[name="title"]').value = 'Consulta Psiquiátrica';
document.querySelector('input[name="title"]').dispatchEvent(new Event('input', {bubbles: true}));
```

---

## 9. Docker Compose Template Completo (Cal.com)

```yaml
services:
  database:
    container_name: calcom-db
    image: postgres:14
    restart: always
    volumes:
      - calcom-db-data:/var/lib/postgresql/data/
    environment:
      POSTGRES_USER: calcom_user
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: calcom
    networks:
      - calcom-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U calcom_user -d calcom"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    container_name: calcom-redis
    image: redis:7-alpine
    restart: always
    volumes:
      - calcom-redis-data:/data
    networks:
      - calcom-network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  calcom:
    container_name: calcom-app
    image: calcom.docker.scarf.sh/calcom/cal.com
    restart: always
    networks:
      - calcom-network
    ports:
      - "3005:3000"
    environment:
      - NEXT_PUBLIC_WEBAPP_URL=${NEXT_PUBLIC_WEBAPP_URL}
      - NEXT_PUBLIC_LICENSE_CONSENT=agree
      - NEXTAUTH_SECRET=${NEXTAUTH_SECRET}
      - CALENDSO_ENCRYPTION_KEY=${CALENDSO_ENCRYPTION_KEY}
      - DATABASE_URL=postgresql://calcom_user:${POSTGRES_PASSWORD}@database:5432/calcom
      - DATABASE_DIRECT_URL=postgresql://calcom_user:${POSTGRES_PASSWORD}@database:5432/calcom
      - REDIS_URL=redis://redis:6379
      - NODE_ENV=production
      - CALCOM_TELEMETRY_DISABLED=1
      - EMAIL_FROM=${EMAIL_FROM}
      - EMAIL_FROM_NAME=${EMAIL_FROM_NAME}
      - SMTP_HOST=${SMTP_HOST}
      - SMTP_PORT=${SMTP_PORT}
      - SMTP_FROM=${SMTP_USER}
      - SMTP_USER=${SMTP_USER}
      - SMTP_PASSWORD=${SMTP_PASSWORD}
      - CALCOM_LICENSE_KEY=${CALCOM_LICENSE_KEY}
      - CAL_SIGNATURE_TOKEN=${CAL_SIGNATURE_TOKEN}
      - CALCOM_PRIVATE_API_ROUTE=${CALCOM_PRIVATE_API_ROUTE}
    depends_on:
      database:
        condition: service_healthy
      redis:
        condition: service_healthy

volumes:
  calcom-db-data:
  calcom-redis-data:

networks:
  calcom-network:
    name: calcom-network
    external: false
```

### Environment Variables Template:
```env
POSTGRES_PASSWORD=STRONG_PASSWORD_HERE
NEXT_PUBLIC_WEBAPP_URL=https://cal.valtyk.com
NEXTAUTH_SECRET=RANDOM_32_CHAR_STRING
CALENDSO_ENCRYPTION_KEY=RANDOM_32_CHAR_STRING
CALCOM_LICENSE_KEY=YOUR_LICENSE_KEY
CAL_SIGNATURE_TOKEN=YOUR_SIGNATURE_TOKEN
CALCOM_PRIVATE_API_ROUTE=https://goblin.cal.com
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-gmail-app-password
EMAIL_FROM=citas@valtyk.com
EMAIL_FROM_NAME=Valtyk Bookings
```

---

## 10. Checklist de Onboarding por Cliente

```
PRE-SETUP:
□ Obtener datos del cliente (nombre, especialidad, servicios, horarios)
□ Definir username (ej: dra-nombre, nombre-profesion)
□ Definir event types (título, duración, precio, ubicación)
□ Generar password seguro para el cliente

CUENTA:
□ Crear usuario (UI o SQL)
□ Bypass email verification (si no hay SMTP)
□ Verificar completedOnboarding = true
□ Verificar que el perfil público carga: /USERNAME

DISPONIBILIDAD:
□ Configurar schedule (horarios por día)
□ Configurar timezone (America/Mexico_City para MX)
□ Bloquear horarios de comida si aplica

EVENT TYPES:
□ Crear via UI (nunca via SQL)
□ Configurar título, slug, duración, descripción
□ Configurar ubicación (In Person + dirección)
□ Verificar que la URL pública funciona: /USERNAME/SLUG
□ Verificar que aparecen slots disponibles

SMTP:
□ Obtener Gmail App Password (o configurar servicio SMTP)
□ Agregar variables SMTP al docker-compose
□ Reiniciar Cal.com
□ Verificar envío (hacer booking de prueba)

LANDING PAGE:
□ Agregar Cal.com embed script en <head>
□ Actualizar CTAs principales con data-cal-link
□ Agregar sección de booking inline (#booking)
□ Agregar script de inicialización inline
□ Agregar CSS para la sección de booking
□ Mantener WhatsApp como opción alternativa
□ Deploy y verificar que funciona end-to-end

POST-DEPLOY:
□ Hacer reserva de prueba end-to-end
□ Verificar email de confirmación (si SMTP está activo)
□ Eliminar reserva de prueba
□ Guardar credenciales en archivo de cliente
□ Documentar la configuración
```
