-- Orbe: cuentas personales. Cada persona guarda todos sus datos en una sola fila, solo visible para ella.
-- Ejecútalo una vez en Supabase (SQL Editor) del proyecto que use Orbe.

create table if not exists public.orbe_data (
  user_id uuid primary key references auth.users (id) on delete cascade,
  data jsonb not null,
  updated_at timestamptz not null default now()
);

alter table public.orbe_data enable row level security;

create policy "orbe: leer lo propio" on public.orbe_data
  for select to authenticated using ((select auth.uid()) = user_id);
create policy "orbe: crear lo propio" on public.orbe_data
  for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "orbe: cambiar lo propio" on public.orbe_data
  for update to authenticated using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
create policy "orbe: borrar lo propio" on public.orbe_data
  for delete to authenticated using ((select auth.uid()) = user_id);
