"""Gera os SVGs do README de perfil (tema claro e escuro).

Uso: python3 gen_assets.py <diretorio-saida>
"""
import sys
from pathlib import Path
from xml.sax.saxutils import escape as esc

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "dark": dict(
        bg="#0d1117", card="#161b22", card2="#1c2330", border="#30363d",
        text="#e6edf3", muted="#8b949e", faint="#21262d",
        a1="#22d3ee", a2="#3b82f6", a3="#a78bfa", ok="#3fb950",
        chip="#1f2937", chiptext="#c9d1d9", grid="#ffffff", gridop="0.035",
    ),
    "light": dict(
        bg="#ffffff", card="#f6f8fa", card2="#eef2f7", border="#d0d7de",
        text="#1f2328", muted="#59636e", faint="#eaeef2",
        a1="#0891b2", a2="#2563eb", a3="#7c3aed", ok="#1a7f37",
        chip="#eaeef2", chiptext="#30363d", grid="#000000", gridop="0.04",
    ),
}


def t(x, y, s, size, fill, weight=400, family=SANS, anchor="start", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{esc(s)}</text>')


def chips(x, y, items, c, size=12, h=24, gap=8, cw=7.2):
    out, cx = [], x
    for it in items:
        w = len(it) * cw + 20
        out.append(f'<rect x="{cx}" y="{y}" width="{w:.0f}" height="{h}" rx="{h/2}" fill="{c["chip"]}" stroke="{c["border"]}"/>')
        out.append(t(cx + w / 2, y + h / 2 + 4.2, it, size, c["chiptext"], 500, MONO, "middle"))
        cx += w + gap
    return "".join(out)


def svg(w, h, body, c, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{esc(title)}"><title>{esc(title)}</title>{body}</svg>')


def defs(c, uid):
    return f'''<defs>
<linearGradient id="g{uid}" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="{c["a1"]}"/><stop offset="0.55" stop-color="{c["a2"]}"/><stop offset="1" stop-color="{c["a3"]}"/></linearGradient>
<radialGradient id="glow{uid}" cx="0.82" cy="0.2" r="0.6"><stop offset="0" stop-color="{c["a2"]}" stop-opacity="0.22"/><stop offset="1" stop-color="{c["a2"]}" stop-opacity="0"/></radialGradient>
<radialGradient id="glowb{uid}" cx="0.05" cy="1" r="0.5"><stop offset="0" stop-color="{c["a1"]}" stop-opacity="0.14"/><stop offset="1" stop-color="{c["a1"]}" stop-opacity="0"/></radialGradient>
<pattern id="grid{uid}" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{c["grid"]}" stroke-opacity="{c["gridop"]}"/></pattern>
</defs>'''


# ---------------------------------------------------------------- banner
def banner(c):
    W, H = 1200, 340
    b = [defs(c, "b"),
         f'<style>.blink{{animation:bl 1.1s steps(1) infinite}}@keyframes bl{{50%{{opacity:0}}}}'
         f'.pulse{{animation:pu 2.4s ease-in-out infinite}}@keyframes pu{{0%,100%{{opacity:1}}50%{{opacity:.35}}}}'
         f'@media (prefers-reduced-motion:reduce){{.blink,.pulse{{animation:none}}}}</style>',
         f'<rect width="{W}" height="{H}" rx="18" fill="{c["bg"]}"/>',
         f'<rect width="{W}" height="{H}" rx="18" fill="url(#gridb)"/>',
         f'<rect width="{W}" height="{H}" rx="18" fill="url(#glowb)"/>',
         f'<rect width="{W}" height="{H}" rx="18" fill="url(#glowbb)"/>',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{c["border"]}"/>',
         f'<rect x="56" y="58" width="44" height="4" rx="2" fill="url(#gb)"/>',
         t(56, 92, "FULL STACK DEVELOPER  ·  TERESINA, PI", 15, c["muted"], 600, MONO, extra='letter-spacing="1.5"'),
         t(54, 160, "Darlan Velozo", 64, c["text"], 700, extra='letter-spacing="-1.5"'),
         t(56, 204, "Construo produtos SaaS e opero sistemas", 24, c["muted"], 400),
         t(56, 238, "que não podem cair.", 24, c["muted"], 400),
         chips(56, 268, ["Python", "Django", "React", "PostgreSQL", "IA"], c, 15, 32, 10, 9.2),
         ]
    # terminal card
    x, y, w, h = 742, 54, 402, 232
    b += [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{c["card"]}" stroke="{c["border"]}"/>',
          f'<path d="M{x} {y+12}a12 12 0 0 1 12-12h{w-24}a12 12 0 0 1 12 12v22H{x}z" fill="{c["card2"]}"/>',
          f'<line x1="{x}" y1="{y+34}" x2="{x+w}" y2="{y+34}" stroke="{c["border"]}"/>',
          f'<circle cx="{x+18}" cy="{y+17}" r="5" fill="#ff5f57"/><circle cx="{x+36}" cy="{y+17}" r="5" fill="#febc2e"/><circle cx="{x+54}" cy="{y+17}" r="5" fill="#28c840"/>',
          t(x + w / 2, y + 22, "~/darlan — zsh", 14, c["muted"], 500, MONO, "middle")]
    lines = [
        [("$ ", c["a1"]), ("whoami", c["text"])],
        [("produto & produção", c["muted"])],
        [("$ ", c["a1"]), ("ls ~/produtos", c["text"])],
        [("arminda/  ", c["a2"]), ("pdv-vitrine/  ", c["a2"]), ("bluemetrics/", c["a2"])],
        [("$ ", c["a1"]), ("pytest -q", c["text"])],
        [("●", c["ok"]), (" 694 passed", c["ok"]), (" · deploy ok", c["muted"])],
    ]
    ly = y + 64
    for ln in lines:
        spans = "".join(f'<tspan fill="{col}">{esc(s)}</tspan>' for s, col in ln)
        b.append(f'<text x="{x+22}" y="{ly}" font-family="{MONO}" font-size="16" xml:space="preserve">{spans}</text>')
        ly += 28
    b.append(f'<rect class="blink" x="{x+22}" y="{ly-15}" width="9" height="18" fill="{c["a1"]}"/>')
    return svg(W, H, "".join(b), c, "Darlan Velozo — Full Stack Developer")


# ---------------------------------------------------------------- metrics
METRICS = [
    ("8 anos", "de Django em produção"),
    ("3", "SaaS no ar · 2 próprios"),
    ("694", "testes no Arminda"),
    ("11 ms", "antes: horas via API"),
    ("3 ERPs", "integrados na operação"),
]


def metrics(c):
    W, H = 1200, 150
    n = len(METRICS)
    cw = W / n
    b = [defs(c, "m"), f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="{c["card"]}" stroke="{c["border"]}"/>']
    for i, (big, small) in enumerate(METRICS):
        cx = cw * i + cw / 2
        if i:
            b.append(f'<line x1="{cw*i}" y1="30" x2="{cw*i}" y2="{H-30}" stroke="{c["border"]}"/>')
        b.append(t(cx, 72, big, 42, "url(#gm)", 700, anchor="middle", extra='letter-spacing="-0.5"'))
        b.append(t(cx, 108, small, 18, c["muted"], 400, anchor="middle"))
    return svg(W, H, "".join(b), c, "Números: " + "; ".join(f"{a} {b_}" for a, b_ in METRICS))


# ---------------------------------------------------------------- project cards
PROJECTS = {
    "arminda": dict(
        name="Arminda", status="em produção", kind="PRODUTO PRÓPRIO",
        tag="Folha de pagamento e RH para prefeituras",
        bullets=["No ar em 2 municípios, migração self-service",
                 "eSocial completo, validado no XSD oficial",
                 "Multi-tenant por schema · 694 testes · CI"],
        stack=["Django", "React", "Postgres", "Celery"], accent="a1"),
    "vape": dict(
        name="PDV & Vitrine", status="em produção", kind="PRODUTO PRÓPRIO",
        tag="SaaS de varejo multi-loja",
        bullets=["PDV, caixa, estoque e vitrine online",
                 "Checkout Pix próprio, sem gateway",
                 "Reserva com lock de linha · v1.7 · CI"],
        stack=["Django", "DRF", "React", "TypeScript"], accent="a2"),
    "hubtrix": dict(
        name="Hubtrix", status="em produção", kind="CO-DESENVOLVEDOR",
        tag="CRM, marketing e CS para provedores de internet",
        bullets=["190+ commits no core, vários ISPs no ar",
                 "Módulos de Cobrança e Analytics",
                 "ERP, WhatsApp e LLMs integrados"],
        stack=["Django", "Channels", "Redis", "LLMs"], accent="a3"),
    "bluemetrics": dict(
        name="BlueMetrics", status="em desenvolvimento", kind="PRODUTO PRÓPRIO",
        tag="BI B2B sobre o ERP Conta Azul",
        bullets=["OAuth2 + sync financeiro e vendas",
                 "Isolamento por Row-Level Security",
                 "Insights por IA · cobrança via Stripe"],
        stack=["Django", "Next.js", "Postgres", "Claude"], accent="a1"),
}


def card(p, c, key):
    W, H = 584, 300
    acc = c[p["accent"]]
    live = p["status"] == "em produção"
    dot = c["ok"] if live else "#d29922"
    b = [defs(c, key), f'<style>.pulse{{animation:pu 2.4s ease-in-out infinite}}@keyframes pu{{0%,100%{{opacity:1}}50%{{opacity:.3}}}}@media (prefers-reduced-motion:reduce){{.pulse{{animation:none}}}}</style>',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="{c["card"]}" stroke="{c["border"]}"/>',
         f'<path d="M0.5 14.5a14 14 0 0 1 14-14h{W-29}a14 14 0 0 1 14 14v-1" fill="none"/>',
         f'<rect x="28" y="0.5" width="64" height="3" rx="1.5" fill="{acc}"/>',
         t(28, 42, p["kind"], 13.5, acc, 700, MONO, extra='letter-spacing="1.4"')]
    sw = len(p["status"]) * 8.4 + 38
    b += [f'<rect x="{W-28-sw}" y="22" width="{sw}" height="30" rx="15" fill="{c["bg"]}" stroke="{c["border"]}"/>',
          f'<circle class="{"pulse" if live else ""}" cx="{W-28-sw+15}" cy="37" r="5" fill="{dot}"/>',
          t(W - 28 - sw + 28, 42.5, p["status"], 14.5, c["muted"], 500)]
    b += [t(28, 92, p["name"], 36, c["text"], 700, extra='letter-spacing="-0.6"'),
          t(28, 124, p["tag"], 19, c["muted"], 400)]
    y = 166
    for s in p["bullets"]:
        b.append(f'<path d="M30 {y-5}l5 5 9-10" fill="none" stroke="{acc}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" transform="translate(0 -1)"/>')
        b.append(t(56, y, s, 17.5, c["text"], 400))
        y += 31
    b.append(f'<line x1="28" y1="{H-62}" x2="{W-28}" y2="{H-62}" stroke="{c["faint"]}"/>')
    b.append(chips(28, H - 46, p["stack"], c, 14.5, 30, 9, 8.9))
    return svg(W, H, "".join(b), c, f'{p["name"]} — {p["tag"]}')


# ---------------------------------------------------------------- timeline
STEPS = [
    ("2018", "Técnico · IFPI", "1º certificado em Django"),
    ("OLIMPÍADAS", "Medalhista", "matemática · nac. e intern."),
    ("GRADUAÇÃO", "ADS · IFPI", "Análise e Desenv. de Sistemas"),
    ("PRODUÇÃO", "Provedor de internet", "ERP, cobrança, APIs e bots"),
    ("HOJE", "SaaS próprios", "Arminda · PDV & Vitrine"),
]


def timeline(c):
    W, H = 1200, 196
    n = len(STEPS)
    pad = 110
    step = (W - 2 * pad) / (n - 1)
    b = [defs(c, "t"), f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="{c["card"]}" stroke="{c["border"]}"/>',
         f'<rect x="{pad}" y="60.5" width="{W-2*pad}" height="3" rx="1.5" fill="url(#gt)"/>']
    for i, (when, what, sub) in enumerate(STEPS):
        x = pad + step * i
        last = i == n - 1
        b.append(f'<circle cx="{x}" cy="62" r="{9 if last else 7}" fill="{c["card"]}" stroke="{c["a2"] if not last else c["a3"]}" stroke-width="3"/>')
        if last:
            b.append(f'<circle cx="{x}" cy="62" r="3.5" fill="{c["a3"]}"/>')
        b.append(t(x, 40, when, 15, c["a1"] if not last else c["a3"], 700, MONO, "middle", 'letter-spacing="1"'))
        b.append(t(x, 110, what, 21, c["text"], 600, anchor="middle"))
        b.append(t(x, 140, sub, 16, c["muted"], 400, anchor="middle"))
    return svg(W, H, "".join(b), c, "Trajetória: " + " → ".join(f"{a}: {b_}" for a, b_, _ in STEPS))


# ---------------------------------------------------------------- section header
def header(title, sub, c, key):
    W, H = 1200, 64
    b = [defs(c, key),
         f'<rect x="0" y="18" width="5" height="30" rx="2.5" fill="url(#g{key})"/>',
         t(22, 42, title, 26, c["text"], 700, extra='letter-spacing="-0.4"')]
    if sub:
        b.append(t(W, 42, sub, 13, c["muted"], 500, MONO, "end"))
    return svg(W, H, "".join(b), c, title)


HEADERS = {
    "produtos": ("Produtos que construí", "do zero · em produção"),
    "impacto": ("Impacto em produção", "resultados medidos"),
    "colabora": ("Onde colaboro", "orgs e repositórios de terceiros"),
    "stack": ("Stack", "por profundidade de uso"),
    "trajetoria": ("Trajetória", "2018 → hoje"),
    "escrita": ("Escrevo sobre isso", "engenharia em provedores"),
}

for mode, c in THEMES.items():
    (OUT / f"banner-{mode}.svg").write_text(banner(c))
    (OUT / f"metrics-{mode}.svg").write_text(metrics(c))
    (OUT / f"timeline-{mode}.svg").write_text(timeline(c))
    for k, p in PROJECTS.items():
        (OUT / f"card-{k}-{mode}.svg").write_text(card(p, c, k))
print("ok", len(list(OUT.glob("*.svg"))))
