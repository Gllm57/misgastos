// Orbe: borra la cuenta de quien llama (correo, contraseña y todos sus datos).
// La persona se identifica con su sesión (Authorization: Bearer <access_token>).
// Antes de borrar, las metas compartidas que lidera pasan al miembro más antiguo;
// si no queda nadie, la meta se borra. Lo demás (orbe_data, sg_members, sg_aportes)
// se borra solo por «on delete cascade».
import { createClient } from "npm:@supabase/supabase-js@2.45.4";

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, apikey, content-type, x-client-info",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (b: unknown, status = 200) =>
  new Response(JSON.stringify(b), { status, headers: { ...CORS, "Content-Type": "application/json" } });

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  if (req.method !== "POST") return json({ error: "method" }, 405);

  const jwt = (req.headers.get("Authorization") || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return json({ error: "no_session" }, 401);

  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, {
    auth: { persistSession: false, autoRefreshToken: false },
  });
  const { data: u, error: ue } = await admin.auth.getUser(jwt);
  if (ue || !u?.user) return json({ error: "no_session" }, 401);
  const uid = u.user.id;

  // Metas compartidas que lidera: pasarlas al miembro más antiguo que no sea él
  const { data: goals, error: ge } = await admin.from("sg_goals").select("id").eq("leader", uid);
  if (ge) return json({ error: "db", detail: ge.message }, 500);
  for (const g of goals || []) {
    const { data: next } = await admin.from("sg_members").select("user_id")
      .eq("goal_id", g.id).neq("user_id", uid).order("joined_at", { ascending: true }).limit(1);
    if (next && next[0]) {
      const { error } = await admin.from("sg_goals").update({ leader: next[0].user_id }).eq("id", g.id);
      if (error) return json({ error: "db", detail: error.message }, 500);
    }
  }

  const { error: de } = await admin.auth.admin.deleteUser(uid);
  if (de) return json({ error: "delete", detail: de.message }, 500);
  return json({ ok: true });
});
