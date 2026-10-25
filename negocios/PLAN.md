# Orbe Negocios · plan completo

Este documento es el punto de partida de la app **Orbe Negocios**. Junta lo que se diseñó en la maqueta (https://claude.ai/artifact/G5XgQd56oAYGYSxnKFB5j4) y lo que ya funciona en **Orbe personal** (`index.html` de este repositorio).

---

## 1. Qué es y para quién

Una app para llevar un negocio pequeño desde el teléfono, en dólares y bolívares, sin computadora ni caja registradora.

- **Bodegas y abastos:** venden en mostrador, fían a vecinos y les preocupa la tasa y el inventario.
- **Emprendedores de Instagram y WhatsApp:** venden a domicilio, cobran por Pago Móvil o USDT y no saben cuánto ganan de verdad.
- **Locales con empleados:** tienda, farmacia pequeña o comida rápida. El dueño quiere ver la caja sin estar ahí.

**La promesa:** «Tú vendes. Orbe hace lo repetitivo.»

## 2. Por qué es una app aparte

| | Orbe personal | Orbe Negocios |
|---|---|---|
| Quién la usa | Una persona | Dueño y empleados |
| Datos | Una fila JSON por usuario (`orbe_data`) | Tablas separadas: ventas, productos, clientes… |
| Cómo gana dinero | Plus a $1,99 | Planes de $4,99 a $19,99 |
| Pantalla principal | Saldo y gastos | Ventas de hoy y caja |

Las dos comparten:
- **La misma cuenta:** un solo correo y contraseña sirven para las dos.
- **El mismo diseño.**
- **La misma base:** código de tasas, seguridad y modo sin conexión.

Más adelante, desde Orbe personal se podrá ver «Lo que me pagó el negocio» como un ingreso.

## 3. Qué se reutiliza de Orbe personal

Todo esto ya está probado en `index.html` y se copia o adapta:

- **Tasas:**
  - BCV, euro y paralelo: `ve.dolarapi.com`, con respaldo en `pydolarve.org`.
  - USDT: Binance y CoinGecko.
  - Histórico de tasas.
  - Formato `$1.234,56` / `Bs 1.234,56`.
- **Seguridad:**
  - Código PIN con bloqueo que no se reinicia al recargar (`orbe-lk`).
  - Face ID por WebAuthn.
- **Datos a salvo:**
  - `sanitizeData` / `cleanObj` al cargar.
  - Pantalla de rescate si los datos están dañados. Los datos dañados se guardan aparte, nunca se borran.
- **Copias automáticas** en IndexedDB, y copia antes de restaurar.
- **Sin conexión:** service worker, manifest e iconos para instalar en la pantalla de inicio.
- **Sincronización con Supabase** por REST sin librerías:
  - Inicio de sesión, registro, recuperar clave y renovar sesión.
  - Detección de cambios con `hashOf`.
  - Aviso de conflicto entre dos teléfonos.
- **Diseño y gestos:**
  - Hojas que suben desde abajo.
  - Botón de confirmar fijo abajo, con el mismo estilo en toda la app.
  - El teclado nunca se abre solo.
  - Animaciones suaves.
  - Tutorial paso a paso rápido.
  - Arreglo de la franja inferior en iPhone (`display-mode: standalone`).
- **Análisis con IA** (API de Anthropic) para el resumen de la semana.
- **Avisos** de pagos y vencimientos.

## 4. Módulos de la app

1. **Hoy:**
   - Ventas del día en $ y Bs, comparadas con ayer.
   - Gráfico de ventas por hora.
   - Ganancia, ticket promedio y lo que te deben.
   - Botones rápidos: Vender, Escanear y Cerrar caja.
   - Lista «Orbe trabajó por ti».
2. **Vender:**
   - Cuadrícula de productos y escáner de códigos.
   - Formas de pago: Pago Móvil, efectivo $, efectivo Bs, USDT, Zelle, fiado o pago mixto.
   - Recibo por WhatsApp.
   - El vuelto se calcula en las dos monedas.
3. **Clientes:**
   - Fiados con fecha, abonos parciales y recordatorio automático.
   - Historial de cada cliente.
4. **Inventario:**
   - Por producto: costo, precio, margen, stock y mínimo.
   - Alertas cuando algo se acaba.
   - Ajustes por merma o pérdida.
   - El precio en $ es fijo y el precio en Bs sigue la tasa.
5. **Proveedores:**
   - Lista de proveedores y pedido sugerido según lo que se vende cada semana.
   - Envío del pedido por WhatsApp.
   - Al recibir la mercancía, se suma al stock.
6. **Gastos del negocio:** alquiler, luz, sueldos y compras, para calcular la ganancia real del mes.
7. **Cierre de caja:**
   - Lo esperado contra lo contado en cada forma de pago, y la diferencia.
   - Resumen enviado al dueño.
8. **Automático:** tareas que se prenden y apagan, con el contador de horas ahorradas.
9. **Catálogo en línea** (`orbe.app/<negocio>`): el cliente arma su pedido, elige retiro o delivery y el pedido le llega al negocio en Orbe.
10. **Equipo:**
    - Roles: dueño, encargado y cajero.
    - Turnos y lo que vendió cada uno.
    - El cajero no ve las ganancias.
11. **Reportes:**
    - Ventas por día y por producto, y los productos que más ganan.
    - Exportar a Excel o PDF.
    - Reporte para el contador con el IVA.

## 5. Datos (Supabase)

Como varias personas usan el mismo negocio, no sirve guardar una sola fila JSON como en `orbe_data`. Hacen falta tablas con reglas por negocio. Todas llevan el prefijo `neg_`:

- `neg_negocios`: id, nombre, rif, slug del catálogo, plan, fecha de fin de la prueba.
- `neg_miembros`: negocio, usuario, rol.
- `neg_productos`: nombre, código de barras, costo, precio, stock, mínimo, categoría, proveedor.
- `neg_ventas`: fecha, cajero, total, forma de pago, referencia, cliente, si es fiado.
- `neg_venta_items`: producto, cantidad, precio y costo del momento.
- `neg_clientes`, `neg_abonos`: fiados y pagos parciales.
- `neg_proveedores`, `neg_pedidos`.
- `neg_gastos`, `neg_cierres`.
- `neg_automatizaciones`: cuáles están activas y su historial.
- `neg_pedidos_web`: pedidos que llegan del catálogo.

Las reglas (RLS) se basan en que el usuario sea miembro del negocio, y el rol limita lo que puede ver.

**Proyecto:** el plan gratis de Supabase ya tiene sus 2 proyectos. Se puede usar **a-fuego**, igual que Orbe personal, con el prefijo `neg_`. **a-fuego no se pausa.** Así la cuenta es la misma en las dos apps.

**Sin conexión:** las ventas se guardan primero en el teléfono, en una cola, y suben cuando vuelve el internet. Una bodega no puede dejar de vender porque se cayó la conexión.

## 6. Automatizaciones: qué se puede hacer y cómo

| Tarea | Cómo funciona | Dónde funciona | Costo |
|---|---|---|---|
| Precios en Bs con la tasa | El precio en $ es fijo y el de Bs se calcula al abrir la app | Todos | Gratis |
| Alertas de stock y pedido sugerido | Se calculan en la app | Todos | Gratis |
| Cierre de caja | Se calcula en la app. A las 8 pm llega un aviso para cerrar | Todos | Gratis |
| Escáner de códigos | Cámara con una librería de lectura. iPhone no trae lector propio | Todos | Gratis |
| Catálogo en línea | Página pública que lee los productos y guarda pedidos | Todos | Gratis |
| WhatsApp (recordatorios, recibos, pedidos) | **Fase 1:** la app abre el mensaje ya escrito y el dueño toca «Enviar». **Fase 2:** se envía solo con la API de WhatsApp Business | Todos | Fase 1 gratis. Fase 2 cuesta centavos por mensaje |
| Reporte semanal al contador | Una función en el servidor arma el Excel y lo envía por correo | Servidor | Casi gratis |
| **Confirmar Pago Móvil solo** | Leer el aviso del banco en el teléfono | **Solo app nativa en Android** | Gratis, pero requiere publicar en Play Store |
| Confirmar Pago Móvil en iPhone | Anotar la referencia a mano, o API del banco si algún día existe | iPhone | — |
| Resumen con IA | Igual que en Orbe personal | Todos | Centavos por análisis |

## 7. Planes

| Plan | Mensual | Anual | Incluye |
|---|---|---|---|
| Emprendedor | $4,99 | $49,90 | 1 persona y 50 productos. Ventas en $ y Bs, recordatorio de fiados y catálogo en línea |
| **Negocio** (recomendado) | $9,99 | $99,90 | 3 personas. Escáner, inventario sin límite, Pago Móvil confirmado solo, pedido a proveedores, cierre de caja y recibos |
| Equipo | $19,99 | $199,90 | 10 personas. Sucursales, turnos, reporte al contador con IVA, IA y soporte por WhatsApp |

- 14 días gratis sin tarjeta.
- Al terminar la prueba, la app queda en modo lectura: los datos se ven pero no se pueden editar. Nunca se borra nada.
- **Cobro:**
  - Al principio: Pago Móvil o USDT, con referencia verificada a mano y el plan activado desde el panel.
  - Después: Binance Pay automático.
- **Precio fundador:** los primeros 100 negocios pagan $4,99 en el plan Negocio de por vida, a cambio de dar opiniones.

## 8. Cómo se construye

- **Tipo de app:** app web instalable (PWA), igual que Orbe personal. Sale rápido, funciona en iPhone y Android y se puede probar con bodegas reales en días.
- **Archivos:** como esta app es más grande, conviene separar en varios archivos (pantallas, datos, sincronización) en lugar de uno solo. Sigue sin librerías pesadas.
- **App nativa para Android:** más adelante se envuelve la misma app con Capacitor y se publica en Play Store. Así se puede leer el aviso del banco y confirmar el Pago Móvil solo.
- **Repositorio aparte:** `orbe-negocios`, con su propia demo.

## 9. Fases

1. **Fase 1 · Vender sin internet (2–3 semanas):** Vender, Inventario, Fiados, Hoy, Cierre de caja, tasas, PIN, copias y modo sin conexión. Todo en el teléfono.
2. **Fase 2 · Nube y equipo:**
   - Tablas `neg_` en Supabase.
   - Sincronización con cola sin conexión.
   - Miembros y roles.
3. **Fase 3 · Hacia afuera:**
   - Catálogo en línea.
   - WhatsApp con mensaje listo.
   - Escáner.
   - Proveedores y pedidos.
   - Reportes y Excel.
4. **Fase 4 · Automático de verdad:**
   - App Android con Pago Móvil confirmado solo.
   - Reporte al contador.
   - WhatsApp Business API.
   - IA.
5. **Fase 5 · Cobrar:** planes, prueba de 14 días, panel para activar pagos y Binance Pay.

## 10. Preguntas por decidir

1. ¿Se empieza solo con bodegas o también con emprendedores de Instagram? Cambia la pantalla de Vender: mostrador o pedidos.
2. ¿Hace falta factura fiscal (SENIAT) o basta con un recibo simple? La factura fiscal necesita una imprenta digital autorizada.
3. ¿Nombre del dominio para el catálogo? (`orbe.app/negocio`, `orbenegocios.com`…)
4. ¿Hay una bodega conocida para probar la Fase 1?
