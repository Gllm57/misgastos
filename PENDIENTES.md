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
- **Inicio más limpio:**
  - Quitar «Si sigues así…».
  - Línea pequeña de cada cuenta.
  - Rayitas entre cifras.
  - Aviso de pagos más pequeño.

## Funciones

- **Comisiones bancarias automáticas:**
  - Comisión fija por cuenta (por ejemplo, mantenimiento mensual).
  - Comisión por operación (porcentaje por Pago Móvil o transferencia).
- **Pagos:** el calendario no deja ir a meses pasados.
- **Borrar la cuenta completa desde la app:** necesita una función en Supabase (Edge Function).
- **Avisos con la app cerrada:** necesitan un servidor de notificaciones.

## Orbe Negocios

Va en otro chat y otro repositorio (`orbe-negocios`). Plan: `negocios/PLAN.md`. Estilo: `negocios/ESTILO.md`.
