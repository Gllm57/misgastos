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

- **Correos propios con Resend (antes de publicar Orbe para todo el mundo).** El correo que trae Supabase es de prueba: envía muy pocos correos por hora y no garantiza que lleguen, así que fallarían el registro y la recuperación de contraseña. Se necesita un dominio propio (por ejemplo `orbeapp.com`). Pasos:
  1. En resend.com: **Domains → Add Domain**, copiar los registros DNS donde se compró el dominio y esperar a que salga **Verified**. Luego **API Keys → Create API Key** (Sending access).
  2. En Supabase (a-fuego), **Authentication → Emails → SMTP Settings → Enable Custom SMTP**: remitente `no-reply@tudominio.com`, nombre `Orbe`, host `smtp.resend.com`, puerto `465`, usuario `resend`, contraseña la clave `re_...`. La clave se pega solo ahí, nunca en el código.
  3. **Authentication → Rate Limits**: subir el límite de correos a unos 100 por hora.
  4. Opcional: correos de confirmación y de recuperar contraseña en español con el estilo de Orbe (**Authentication → Emails → Templates**).

- Borrar la cuenta completa (correo y contraseña) desde la app necesita una función en el servidor (Edge Function). Hoy la app borra los datos de la nube; la cuenta se borra desde el panel de Supabase.
