# Cuentas personales de Orbe (Supabase)

**Estado:** conectado al proyecto **a-fuego** (`homninhiimgcpkbqbycg`), en la tabla `orbe_data`, que ya está creada con sus reglas. Los usuarios de inicio de sesión se comparten con la app de a-fuego.

Orbe guarda los datos de cada persona en su cuenta, y cada quien solo ve los suyos.
Mientras no conectes un proyecto, la app funciona igual que antes (solo en el teléfono) y la sección «Tu cuenta» no aparece en Ajustes.

## Conectar (una sola vez)

1. Crea un proyecto en [supabase.com](https://supabase.com). Ojo: el plan gratis permite 2 proyectos activos.
2. En **SQL Editor**, pega y ejecuta el archivo `orbe.sql` de esta carpeta. Crea la tabla `orbe_data` con reglas para que cada persona solo pueda leer y escribir su propia fila.
3. En **Authentication → URL Configuration**:
   - **Site URL**: la dirección pública de Orbe (por ejemplo `https://tuusuario.github.io/misgastos/`).
   - **Redirect URLs**: la misma dirección.
4. En **Authentication → Providers → Email**, decide si quieres pedir confirmación por correo. Con confirmación es más seguro: la persona recibe un correo y luego entra.
5. En **Project Settings → API**, copia el **Project URL** y la **clave publicable** (o la `anon`).
6. En `index.html`, busca `var CLOUD = { url: "", key: "" };` y pega los dos valores.

La clave publicable puede ir en la app: no da acceso a los datos de nadie. Las reglas de la tabla son las que protegen cada fila.

## Qué se sincroniza

- Viaja: movimientos, cuentas, metas, pagos, plantillas, límites, subcategorías y ajustes de ahorro.
- Se queda en cada teléfono: el código de bloqueo y Face ID, los avisos, las tasas del día y la clave de la IA.
- Si dos teléfonos cambian datos sin conexión, gana el cambio más reciente. Lo que se reemplaza queda guardado en **Copias automáticas** de ese teléfono.

## Pendiente para más adelante

- Borrar la cuenta completa (correo y contraseña) desde la app necesita una función en el servidor (Edge Function). Hoy la app borra los datos de la nube; la cuenta se borra desde el panel de Supabase.
