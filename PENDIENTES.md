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

## Supabase

En a-fuego, **Authentication → URL Configuration**: poner la dirección pública de Orbe en **Site URL** y **Redirect URLs**.

## Diseño

- **Tableta y computadora:**
  - Barra de abajo con un ancho máximo, centrada.
  - **+** y ✦ junto al contenido, no en la esquina de la pantalla.
- **Banderas de países en Windows:** se ven como letras. Se arregla con imágenes propias.
- **Inicio más limpio:** ver la sección «Inicio más limpio» más abajo.

## Funciones

- **Comisiones bancarias automáticas:** ver la sección «Comisiones automáticas» más abajo.
- **Pagos:** el calendario no deja ir a meses pasados.
- **Borrar la cuenta completa desde la app:** necesita una función en Supabase (Edge Function).
- **Avisos con la app cerrada:** necesitan un servidor de notificaciones.

## Inicio más limpio

Ideas para que el Inicio muestre menos texto y se lea de un vistazo. Cada una se puede hacer por separado.

1. **Quitar «Si sigues así: $X el 31»** (debajo del gráfico del saldo).
   - Es la proyección de cómo terminarás el mes.
   - Opciones:
     - Quitarla.
     - Mostrarla solo al tocar el gráfico.
     - Dejar solo la línea punteada del gráfico, sin el texto.
2. **Simplificar la línea pequeña de cada cuenta** («3% · ≈ $34,26»).
   - Hoy se corta en pantallas chicas.
   - Opciones:
     - Solo el porcentaje («3%»).
     - Solo el equivalente en dólares, debajo del saldo de la derecha.
     - Quitarla y dejar solo nombre y saldo.
3. **Quitar las rayitas verticales** entre Ingresos, Gastos y Ahorrado, y entre las tasas del día. El espacio en blanco ya separa las cifras.
4. **Aviso de pagos más pequeño** («Internet venció · $25,00 y 1 más»).
   - Opciones:
     - Una sola línea más baja, sin ícono grande.
     - Un punto rojo con número sobre la pestaña Pagos, sin aviso en el Inicio.
     - Mostrarlo solo los días que algo vence o venció.
5. **Aviso de cuadrar la cuenta** (nuevo): que use el mismo tamaño compacto que el de pagos, y que nunca salgan los dos a la vez. Primero va el de pagos.
6. **Tasas del día plegadas por defecto** para quien no las usa a diario. Se abren con la flecha que ya existe.

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
