# Pendientes de Orbe

Cosas preparadas o decididas para más adelante.

## Atajo de Siri «Agregar gasto» (listo, escondido)

- **Qué es:** di «Oye Siri, agregar gasto», dile el monto y Orbe se abre con el gasto listo para guardar.
- **Está hecho y probado:**
  - Paso a paso con imágenes de la app Atajos, versión para gasto o ingreso.
  - Botón «Probar».
  - Enlace `?gasto=` / `?ingreso=` con `cat`, `cuenta` y `nota` opcionales.
- **Para mostrarlo:** en `index.html`, quitar `hidden` del botón `id="siri-open"` (Ajustes → Tus datos).
- **Ojo:** el iPhone abre el enlace en Safari, que guarda los datos aparte. Para que el gasto llegue a la app instalada, la persona debe iniciar sesión con su cuenta en los dos.

## Correos propios con Resend (requiere dominio)

Ver `supabase/LEEME.md`. Necesario antes de publicar para todo el mundo: registro y recuperación de contraseña.

## Legal y seguridad (te toca a ti)

- **Correo de contacto:** Apple pide uno en la política de privacidad. Cuando tengas el dominio (por ejemplo `soporte@orbeapp.com`), agregarlo en «Política de privacidad» y «Términos de uso».
- **Contraseñas filtradas:** en Supabase (a-fuego) → Authentication → Policies (o Passwords), activar «Leaked password protection» para que no se puedan usar contraseñas que ya se filtraron.
- **Revisión de un abogado** antes de publicar para todo el mundo, sobre todo por el enlace de referido de Binance y las metas compartidas.

## Supabase

En a-fuego, **Authentication → URL Configuration**: poner la dirección pública de Orbe en **Site URL** y **Redirect URLs**.

## Diseño

- **Tableta y computadora:**
  - Barra de abajo con un ancho máximo, centrada.
  - **+** y ✦ junto al contenido, no en la esquina de la pantalla.
- **Banderas de países en Windows:** se ven como letras. Se arregla con imágenes propias.
- **Inicio más limpio:** hecho; ver la sección más abajo.

## Funciones

- **Comisiones bancarias automáticas:** ver la sección «Comisiones automáticas» más abajo.
- **Pagos:** el calendario no deja ir a meses pasados.
- **Avisos con la app cerrada:** necesitan un servidor de notificaciones.

## Inicio más limpio

Hecho: proyección solo al tocar el gráfico, línea de cada cuenta con solo el «≈ $», aviso de pagos compacto, aviso de cuadrar que nunca sale junto al de pagos y tasas plegadas al abrir.

- Las rayitas verticales se quedan: separan bien los montos grandes. Ingresos, Gastos y Ahorrado se pueden tocar y llevan a su detalle.

## Comisiones automáticas

Hoy existe «Cuadrar con el banco», que corrige cualquier diferencia a mano. Esto lo complementa para que Orbe anote solo lo que el banco cobra siempre.

### A. Comisión fija por cuenta

- **Qué es:** cargos que el banco cobra cada cierto tiempo (mantenimiento mensual, cuota de la tarjeta, servicio de la cuenta).
- **Dónde se configura:** al crear o editar la cuenta, en una sección **«Comisiones del banco»** con:
  - Nombre (por ejemplo, «Mantenimiento»).
  - Monto, en la moneda de la cuenta.
  - Frecuencia: mensual, trimestral o anual.
  - Día del cobro.
- **Qué hace Orbe:** el día del cobro anota sola un gasto en **«Comisiones bancarias»** en esa cuenta, con la nota del nombre. Funciona igual que los pagos repetidos que ya existen.
- **Avisos:** la primera vez que lo anota muestra «Se anotó la comisión de mantenimiento: Bs 150». Se puede deshacer.
- **En el mundo:** cada cuenta usa su moneda, así que sirve para cualquier banco.

### B. Comisión por operación

- **Qué es:** cargos por cada movimiento (por ejemplo, el 0,3 % por Pago Móvil, o un monto fijo por transferencia o retiro en cajero).
- **Dónde se configura:** en la misma sección de la cuenta:
  - **Tipo:** porcentaje o monto fijo.
  - **A qué se aplica:** gastos y transferencias que salen de esa cuenta, o solo transferencias.
  - **Mínimo y máximo**, opcional, porque algunos bancos los tienen.
- **Qué hace Orbe:** al anotar un gasto o una transferencia desde esa cuenta, la hoja muestra debajo del monto «+ comisión Bs 1,20». Al guardar, se anotan dos movimientos: el gasto y la comisión aparte, en «Comisiones bancarias».
- **Se puede apagar en cada movimiento**, con un interruptor «Sin comisión esta vez», para operaciones que el banco no cobra.

### C. Resumen de comisiones

- En el detalle de cada cuenta, una línea: «Comisiones este mes: Bs 320 · este año: Bs 2.900».
- Opcional: aviso si un mes la comisión sube mucho frente al promedio.

### Orden sugerido

1. **A (comisión fija):** la más común y la más simple.
2. **C (resumen):** muestra cuánto se va en el banco.
3. **B (por operación):** la más útil en Venezuela, pero toca la hoja de movimientos y requiere más pruebas.

## Modo ahorro forzoso (hecho; lo que falta)

- **Hecho:** Bóveda bloqueada hasta una fecha, % obligatorio de cada ingreso con subida automática, redondeo x2 e impuesto antojo, «Puedes gastar hoy» en Inicio, dónde guardar la Bóveda, aviso para mover el ahorro y retiro anticipado con 72 h de espera (pide el código o Face ID al pedirlo). Maqueta: https://claude.ai/artifact/Rv9Ss3QSwh9Tmit71G84MW
- **Falta:**
  - Pestaña **Asesor** (proyección del mes, retos y preguntas). Por ahora sigue el resumen con IA.
  - Regla «Sobrante del mes» (apartar el 50 % de lo que no se gastó).
  - Recordatorio de mover el ahorro con la app cerrada (necesita el servidor de notificaciones).
