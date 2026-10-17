# Genera minimal.html a partir de index.html: misma app y mismos datos, con estilo minimalista.
# Uso: python3 tools/build-minimal.py  (vuelve a correrlo cada vez que cambie index.html)
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

def rep(a, b):
    global src
    assert src.count(a) == 1, a[:80]
    src = src.replace(a, b)

rep("family=Inter:wght@400;500;600;700", "family=Inter:wght@300;400;500;600;700")
rep("<title>Mis gastos</title>", "<title>Mis gastos · Minimal</title>")
# El enlace de Ajustes lleva de vuelta al estilo clásico
rep('<a class="set-row" id="style-link" href="minimal.html"><span class="tx"><b>Estilo minimalista</b><small>La misma app y tus mismos datos, con un diseño más simple.</small>',
    '<a class="set-row" id="style-link" href="index.html"><span class="tx"><b>Estilo clásico</b><small>Vuelve al diseño anterior. Tus datos son los mismos.</small>')
# El asistente pasa al menú del +
rep('<button type="button" class="dial-item" role="menuitem" data-dial="mov">',
    '<button type="button" class="dial-item" role="menuitem" data-dial="ai"><span>Asistente</span><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"></path></svg></span></button>\n      <button type="button" class="dial-item" role="menuitem" data-dial="mov">')

CSS = r'''
/* ================= Mis gastos · Minimal ================= */
:root { --min-w: 300; }
/* Cifras grandes en peso ligero */
.balance-amount, .sav-big, .hh-v, .ad-bal, .ph-v, .hero-v, .cx-amt, .amt-card #monto, .sheet .amt-card #monto, .cv-tot b, .rleg-tot b, .acc-tot strong, .hist-cat-sum .v { font-weight: 300 !important; letter-spacing: -0.05em !important; }
.balance-amount { font-size: clamp(2.8rem, 13vw, 3.4rem) !important; }
.flow .v, .rleg-i b, .acc-bal, .cv-amt b, .ha, .hh-row b, .stat b, .ai-stat .v { font-weight: 400 !important; }
.top h1 { font-size: 1.45rem !important; font-weight: 500 !important; }
.gv-title, .ad-title .gv-title { font-size: 1.7rem !important; font-weight: 500 !important; }
.phead h2, .gv-h2, .gv-mh { font-size: 1rem !important; font-weight: 500 !important; }
/* Botones sin relleno: solo el icono */
.chev, .eye, .gv-add, .set-btn, .cal-nav, .dots, .rates-tog, .phead .eye, .gv-actions .eye, .del, .x, .cx-clear { background: none !important; box-shadow: none !important; border: 0 !important; color: var(--muted) !important; }
.gv-add { color: var(--accent) !important; }
.rc-ic { background: none !important; color: var(--muted) !important; width: auto !important; }
/* Píldoras y segmentos pasan a texto subrayado */
.secondary { background: none !important; border: 0 !important; color: var(--ink) !important; padding: 0 6px !important; font-weight: 500 !important; min-height: 40px; }
.primary, .sav-pri { background: var(--ink) !important; color: var(--bg) !important; border: 0 !important; }
.seg { background: none !important; padding: 0 !important; gap: 18px !important; border: 0 !important; }
.seg button { background: none !important; box-shadow: none !important; border-radius: 0 !important; padding: 4px 0 !important; min-height: 0 !important; color: var(--muted) !important; border-bottom: 1.5px solid transparent !important; flex: none !important; }
.seg button[aria-pressed="true"] { color: var(--ink) !important; border-bottom-color: var(--ink) !important; }
.type-seg { gap: 24px !important; }
:root:not(#mg) .type-seg button[aria-pressed="true"][data-type="gasto"] { color: var(--out) !important; border-bottom-color: var(--out) !important; background: none !important; }
:root:not(#mg) .type-seg button[aria-pressed="true"][data-type="ingreso"] { color: var(--in) !important; border-bottom-color: var(--in) !important; background: none !important; }
.type-seg button[aria-pressed="false"] { opacity: 1 !important; color: var(--muted) !important; }
.hist-chips button, .hist-cats button { background: none !important; border: 0 !important; border-radius: 0 !important; padding: 6px 0 !important; margin-right: 12px; color: var(--muted) !important; border-bottom: 1.5px solid transparent !important; }
.hist-chips button[aria-pressed="true"] { color: var(--ink) !important; border-bottom-color: var(--ink) !important; background: none !important; }
.hist-cats button[aria-pressed="true"] { color: var(--c) !important; border-bottom-color: var(--c) !important; background: none !important; }
.hist-search input, .sheet input:not([type="checkbox"]):not([type="radio"]):not([readonly]):not(#monto):not(#cx-amt), .sheet select, .sheet .pick, .sheet .cat-btn, .sheet textarea { background: none !important; border: 0 !important; border-bottom: 1px solid var(--line) !important; border-radius: 0 !important; padding-left: 0 !important; }
#mes-btn { background: none !important; padding: 0 !important; }
.ph-chip { background: none !important; border: 0 !important; padding: 0 10px 0 0 !important; }
/* Iconos de cuentas y movimientos: un punto de color */
.acc-av { width: 8px !important; height: 8px !important; min-width: 8px; border-radius: 50% !important; background: var(--c) !important; border: 0 !important; font-size: 0 !important; color: transparent !important; flex: none; }
.acc-av > * { display: none !important; }
.acc-av.big { width: 12px !important; height: 12px !important; }
.hic { width: 8px !important; height: 8px !important; border-radius: 50% !important; background: var(--muted) !important; }
.hic svg { display: none !important; }
.hic.k-in { background: var(--in) !important; } .hic.k-out { background: var(--out) !important; } .hic.k-sv { background: var(--accent) !important; }
.ai-item .b { background: none !important; }
/* Gráficos de trazo fino */
.rings circle { stroke-width: 4px !important; }
.ring .trk, .ring .bar { stroke-width: 2.4 !important; }
.trend .ln { stroke-width: 1.6 !important; }
.trend .area { opacity: 0.6; }
.sav-chart path[stroke-width] { stroke-width: 1.6; }
.acc-seg, .cv-seg { height: 3px !important; }
.gbar, .hero-bar, .bn-track, .prog, .cv-bar { height: 3px !important; }
/* Bloques sin cajas */
.bn-entry, .bk-nudge, .earn-box, .earn-add, .goal-list .goal { background: none !important; border: 0 !important; border-top: 1px solid var(--line) !important; border-radius: 0 !important; box-shadow: none !important; padding-left: 0 !important; padding-right: 0 !important; }
.bn-entry .bn-ic, .bk-nudge .bk-ic, .earn-ic { background: none !important; }
.goal-list { grid-template-columns: 1fr !important; gap: 0 !important; }
.goal-list .goal { padding-top: 12px !important; padding-bottom: 12px !important; }
.goal-list .goal-head { flex-direction: row !important; align-items: center !important; gap: 14px !important; }
.goal-list .goal-head .ring { width: 36px !important; height: 36px !important; }
.goal-list .goal-head .ring .pct { font-size: 0.6rem !important; }
.goal-list .goal-add { border-top: 1px solid var(--line); }
.goal-list .goal-add button { border: 0 !important; background: none !important; color: var(--accent) !important; justify-content: flex-start !important; padding: 14px 0 !important; min-height: 0 !important; }
/* Barra inferior: solo iconos, el + en el centro */
body, body.tb-min { --tbh: 64px; --tbx: 0px; }
.tabbar { left: 0 !important; right: 0 !important; bottom: 0 !important; height: calc(66px + env(safe-area-inset-bottom, 0px)) !important; padding: 0 30px env(safe-area-inset-bottom, 0px) !important; border-radius: 0 !important; border: 0 !important; box-shadow: none !important; -webkit-backdrop-filter: none !important; backdrop-filter: none !important; background: linear-gradient(to top, var(--bg) 62%, color-mix(in srgb, var(--bg) 0%, transparent)) !important; }
.tab-lens { display: none !important; }
.tab > :not(svg) { display: none !important; }
.tab { flex-direction: column; gap: 6px !important; color: var(--muted) !important; }
.tab svg { width: 22px !important; height: 22px !important; stroke-width: 1.7 !important; }
.tab::after { content: ""; width: 4px; height: 4px; border-radius: 50%; background: currentColor; opacity: 0; transition: opacity 0.25s; }
.tab[aria-current="true"] { color: var(--ink) !important; }
.tab[aria-current="true"]::after { opacity: 1; }
.tab[data-tab="1"] { margin-right: 76px; }
.fab { left: calc(50% - 25px) !important; right: auto !important; bottom: calc(10px + env(safe-area-inset-bottom, 0px)) !important; width: 50px !important; height: 50px !important; font-size: 1.7rem !important; z-index: 18 !important; box-shadow: 0 8px 20px -6px color-mix(in srgb, var(--accent) 60%, transparent) !important; }
.fab::after { display: none !important; }
.ai-fab { display: none !important; }
.dial-menu { right: calc(50% - 19px) !important; align-items: flex-end !important; bottom: calc(84px + env(safe-area-inset-bottom, 0px)) !important; }
.dial-item { white-space: nowrap; background: none !important; border: 0 !important; box-shadow: none !important; }
body.dial-open .dial { background: color-mix(in srgb, var(--bg) 82%, transparent) !important; -webkit-backdrop-filter: blur(8px); backdrop-filter: blur(8px); }
'''
rep("</style>", CSS + "</style>")
JS = '''<script>
document.addEventListener("click", function (e) { if (e.target.closest('[data-dial="ai"]')) { var b = document.getElementById("ai-btn"); if (b) b.click(); } });
</script>
</body>'''
rep("</body>", JS)
open(os.path.join(ROOT, "minimal.html"), "w", encoding="utf-8").write(src)
print("minimal.html generado")
