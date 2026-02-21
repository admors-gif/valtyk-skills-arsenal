---
name: Hosting & DevOps
description: Guía de infraestructura — Nginx Proxy Manager, SSL, Docker, Firebase Hosting, DNS, Hostinger VPS, y deploy de aplicaciones.
---

# 🔒 Hosting & DevOps — Skill Guide

## Cuándo usar esta skill
- Al desplegar una landing page nueva
- Al configurar dominios y SSL
- Al administrar el VPS de Hostinger
- Al crear containers Docker
- Al configurar Nginx Proxy Manager

---

## 1. Arquitectura de Infraestructura Valtyk

```
Internet
  │
  ├── valtyk.com (DNS → Hostinger VPS)
  │     └── Nginx Proxy Manager (:80/:443)
  │          ├── cal.valtyk.com → Cal.com Docker (:3005)
  │          ├── n8n.valtyk.com → n8n Docker (:5678)
  │          └── [cliente].valtyk.com → Firebase Hosting
  │
  ├── Firebase Hosting (Landing Pages)
  │     ├── tabatha-barron.valtyk.com
  │     ├── [futuro-cliente].valtyk.com
  │     └── ...
  │
  └── Hostinger VPS (Services)
        ├── Cal.com (agendamiento)
        ├── n8n (automatización)
        ├── Nginx Proxy Manager (reverse proxy)
        └── [futuras apps]
```

---

## 2. Firebase Hosting — Deploy de Landing Pages

### Setup Inicial (una sola vez)
```bash
# Instalar Firebase CLI
npm install -g firebase-tools

# Login
firebase login

# Inicializar proyecto
firebase init hosting
# → Seleccionar proyecto existente: valtyk-landings
# → Public directory: public
# → SPA: Yes
```

### Agregar Nuevo Cliente
```bash
# 1. Agregar target en Firebase
firebase target:apply hosting nombre-cliente nombre-cliente

# 2. Configurar firebase.json
# Agregar nuevo hosting site

# 3. Deploy
firebase deploy --only hosting:nombre-cliente
```

### firebase.json Template
```json
{
  "hosting": {
    "site": "nombre-cliente",
    "public": "public",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
    "headers": [
      {
        "source": "**/*.@(css|js)",
        "headers": [{"key": "Cache-Control", "value": "max-age=31536000"}]
      },
      {
        "source": "**/*.@(jpg|jpeg|gif|png|svg|webp|ico)",
        "headers": [{"key": "Cache-Control", "value": "max-age=31536000"}]
      }
    ],
    "rewrites": [{"source": "**", "destination": "/index.html"}]
  }
}
```

### DNS para Subdominio
```
En Hostinger DNS Manager:
  Tipo: CNAME
  Nombre: nombre-cliente
  Valor: valtyk-landings.web.app
  TTL: 3600

Luego en Firebase Console:
  → Hosting → Custom domain → nombre-cliente.valtyk.com
  → Verificar ownership
  → SSL automático (tarda ~24h)
```

---

## 3. Docker & Docker Compose

### Comandos Esenciales
```bash
# Ver containers corriendo
docker ps

# Ver todos (incluyendo parados)
docker ps -a

# Logs de un container
docker logs -f nombre-container --tail 100

# Reiniciar container
docker restart nombre-container

# Entrar a un container
docker exec -it nombre-container bash

# Recursos usados
docker stats

# Limpiar recursos no usados
docker system prune -a
```

### Docker Compose Cheatsheet
```bash
# Levantar proyecto
docker compose up -d

# Bajar proyecto
docker compose down

# Reconstruir
docker compose up -d --build --force-recreate

# Ver logs
docker compose logs -f

# Ver estado
docker compose ps
```

---

## 4. Nginx Proxy Manager

### Agregar Nuevo Proxy Host
```
1. Login a NPM: https://npm.valtyk.com (o IP:81)
2. Proxy Hosts → Add Proxy Host
3. Configurar:
   Domain: servicio.valtyk.com
   Scheme: http
   Forward Hostname: IP-del-container o nombre-del-service
   Forward Port: puerto-del-servicio
   ✓ Block Common Exploits
   ✓ Websockets Support (si aplica)
4. SSL Tab:
   ✓ Force SSL
   ✓ HTTP/2 Support
   ✓ HSTS Enabled
   → Request new SSL Certificate (Let's Encrypt)
   ✓ I agree to Let's Encrypt terms
```

---

## 5. Hostinger VPS — Mantenimiento

### Monitoreo
```bash
# Uso de disco
df -h

# Uso de memoria
free -h

# Uso de CPU
top -bn1 | head -5

# Procesos Docker
docker stats --no-stream

# Espacio usado por Docker
docker system df
```

### Backups
```bash
# Backup de volumen Docker
docker run --rm -v calcom-db-data:/data -v $(pwd):/backup \
  alpine tar czf /backup/calcom-db-$(date +%Y%m%d).tar.gz -C /data .

# Backup programado (crontab)
crontab -e
# Agregar:
0 3 * * * /root/scripts/backup.sh
```

### Seguridad Básica
```bash
# Actualizar sistema
apt update && apt upgrade -y

# Firewall (UFW)
ufw allow 22    # SSH
ufw allow 80    # HTTP
ufw allow 443   # HTTPS
ufw enable

# Fail2ban (proteger SSH)
apt install fail2ban -y
systemctl enable fail2ban
```

---

## 6. SSL Certificates

### Let's Encrypt (vía NPM)
```
Automático con Nginx Proxy Manager:
  → Se renueva automáticamente cada 90 días
  → Wildcard: necesita DNS challenge con Cloudflare
```

### Troubleshooting SSL
```
"SSL Certificate Error":
  1. Verificar DNS apunta al VPS correcto
  2. Puerto 80 y 443 abiertos en firewall
  3. Esperar propagación DNS (hasta 48h)
  4. En NPM: eliminar certificado → crear uno nuevo

"Mixed Content":
  → Asegurar que TODOS los recursos usan https://
  → Buscar: http:// en el HTML y cambiar a https:// o //
```

---

## 7. Checklist de Deploy

```
Antes de lanzar cualquier servicio:
□ DNS configurado correctamente
□ SSL activado y funcionando
□ Firewall permite puertos necesarios
□ Docker container corriendo y healthy
□ Logs sin errores
□ Backup del servicio anterior (si es update)
□ Test desde móvil y desktop
□ Performance aceptable (< 3s de carga)
□ Monitoreo configurado (uptime)
```
