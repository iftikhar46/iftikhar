import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Iftikhar Hussain Shah | Senior Laravel Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS + Animations ─────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:ital,wght@0,400;0,500;1,400&family=Instrument+Serif:ital@0;1&display=swap');

/* ─── Reset & Base ─── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background: #050a0e !important;
    color: #e8f4f0 !important;
    font-family: 'DM Mono', monospace;
}

[data-testid="stHeader"], [data-testid="stToolbar"],
[data-testid="stSidebarCollapsedControl"] { display: none !important; }

.block-container { padding: 0 !important; max-width: 100% !important; }

/* ─── Scrollbar ─── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #050a0e; }
::-webkit-scrollbar-thumb { background: #00e5a0; border-radius: 2px; }

/* ─── Keyframes ─── */
@keyframes fadeUp   { from { opacity:0; transform:translateY(40px); } to { opacity:1; transform:translateY(0); } }
@keyframes fadeIn   { from { opacity:0; } to { opacity:1; } }
@keyframes slideIn  { from { opacity:0; transform:translateX(-60px); } to { opacity:1; transform:translateX(0); } }
@keyframes pulse    { 0%,100% { box-shadow:0 0 0 0 rgba(0,229,160,.4); } 70% { box-shadow:0 0 0 14px rgba(0,229,160,0); } }
@keyframes scanline { 0% { transform:translateY(-100%); } 100% { transform:translateY(100vh); } }
@keyframes blink    { 0%,100% { opacity:1; } 50% { opacity:0; } }
@keyframes float    { 0%,100% { transform:translateY(0px); } 50% { transform:translateY(-12px); } }
@keyframes rotate   { from { transform:rotate(0deg); } to { transform:rotate(360deg); } }
@keyframes shimmer  { 0% { background-position: -200% center; } 100% { background-position: 200% center; } }
@keyframes glow     { 0%,100% { text-shadow: 0 0 20px rgba(0,229,160,.3); } 50% { text-shadow: 0 0 40px rgba(0,229,160,.8), 0 0 80px rgba(0,229,160,.4); } }
@keyframes matrix   { 0% { opacity:1; transform:translateY(0); } 100% { opacity:0; transform:translateY(100px); } }
@keyframes borderAnim { 0% { border-color:#00e5a0; } 50% { border-color:#00b8d9; } 100% { border-color:#00e5a0; } }
@keyframes progressFill { from { width:0; } to { width:var(--w); } }

/* ─── Noise overlay ─── */
body::before {
    content:'';
    position:fixed; inset:0; pointer-events:none; z-index:0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
    background-size: 200px 200px;
    opacity: .4;
}

/* ─── Scanline ─── */
body::after {
    content:'';
    position:fixed; left:0; top:-100%; width:100%; height:2px;
    background:linear-gradient(transparent, rgba(0,229,160,.06), transparent);
    pointer-events:none; z-index:1;
    animation: scanline 8s linear infinite;
}

/* ─── HERO ─── */
.hero {
    min-height: 100vh;
    display: flex; flex-direction: column; justify-content: center; align-items: flex-start;
    padding: 6rem 6vw 4rem;
    position: relative; overflow: hidden;
    background: radial-gradient(ellipse 80% 60% at 70% 50%, rgba(0,229,160,.07) 0%, transparent 60%),
                radial-gradient(ellipse 40% 40% at 20% 80%, rgba(0,184,217,.05) 0%, transparent 50%),
                #050a0e;
}

.hero-eyebrow {
    font-family:'DM Mono', monospace;
    font-size:.75rem; letter-spacing:.25em;
    color:#00e5a0; text-transform:uppercase;
    animation: fadeUp .6s ease both;
    display:flex; align-items:center; gap:.75rem;
}
.hero-eyebrow::before {
    content:''; display:inline-block; width:32px; height:1px; background:#00e5a0;
}

.hero-name {
    font-family:'Syne', sans-serif;
    font-size: clamp(3.2rem, 9vw, 8rem);
    font-weight:800; line-height:.95;
    color:#e8f4f0;
    margin:.6rem 0 .4rem;
    animation: fadeUp .7s .15s ease both;
}

.hero-name span {
    background: linear-gradient(135deg, #00e5a0 0%, #00b8d9 50%, #00e5a0 100%);
    background-size: 200% auto;
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    background-clip:text;
    animation: shimmer 3s linear infinite, fadeUp .7s .15s ease both;
}

.hero-title {
    font-family:'Instrument Serif', serif;
    font-style:italic;
    font-size:clamp(1.1rem, 2.5vw, 1.6rem);
    color:rgba(232,244,240,.55);
    margin-bottom:2rem;
    animation: fadeUp .7s .3s ease both;
}

.hero-desc {
    max-width:52ch;
    font-size:.9rem; line-height:1.9;
    color:rgba(232,244,240,.6);
    animation: fadeUp .7s .45s ease both;
    margin-bottom:2.5rem;
    border-left:2px solid rgba(0,229,160,.3);
    padding-left:1.25rem;
}

.hero-cta {
    display:flex; gap:1rem; flex-wrap:wrap;
    animation: fadeUp .7s .6s ease both;
}

.btn-primary {
    font-family:'DM Mono', monospace;
    font-size:.8rem; letter-spacing:.12em; text-transform:uppercase;
    padding:.85rem 2rem;
    background:#00e5a0; color:#050a0e;
    border:none; border-radius:2px;
    cursor:pointer; font-weight:500;
    transition: transform .2s, box-shadow .2s;
    animation: pulse 2.5s infinite;
    text-decoration:none; display:inline-block;
}
.btn-primary:hover { transform:translateY(-3px); box-shadow:0 12px 30px rgba(0,229,160,.35); }

.btn-secondary {
    font-family:'DM Mono', monospace;
    font-size:.8rem; letter-spacing:.12em; text-transform:uppercase;
    padding:.85rem 2rem;
    background:transparent; color:#00e5a0;
    border:1px solid rgba(0,229,160,.4);
    border-radius:2px; cursor:pointer; font-weight:500;
    transition: transform .2s, border-color .2s, box-shadow .2s;
    text-decoration:none; display:inline-block;
    animation: borderAnim 3s ease infinite;
}
.btn-secondary:hover { transform:translateY(-3px); border-color:#00e5a0; box-shadow:0 12px 30px rgba(0,229,160,.15); }

/* ─── Grid deco ─── */
.hero-grid {
    position:absolute; right:5vw; top:50%;
    transform:translateY(-50%);
    width:380px; height:380px;
    animation: float 6s ease-in-out infinite, fadeIn 1s .8s ease both;
    opacity:.12;
}
.hero-grid circle { animation: rotate 20s linear infinite; transform-origin:50% 50%; }

/* ─── Status badge ─── */
.status-badge {
    display:inline-flex; align-items:center; gap:.5rem;
    padding:.4rem 1rem; border-radius:20px;
    background:rgba(0,229,160,.08);
    border:1px solid rgba(0,229,160,.2);
    font-size:.72rem; color:#00e5a0;
    margin-bottom:1.5rem;
    animation: fadeIn 1s 1s ease both;
}
.status-dot { width:8px; height:8px; border-radius:50%; background:#00e5a0; animation:pulse 1.5s infinite; }

/* ─── Section wrapper ─── */
.section {
    padding: 6rem 6vw;
    position: relative;
}
.section-alt { background: rgba(0,229,160,.02); border-top:1px solid rgba(0,229,160,.06); border-bottom:1px solid rgba(0,229,160,.06); }

.section-label {
    font-family:'DM Mono', monospace;
    font-size:.7rem; letter-spacing:.3em; text-transform:uppercase;
    color:#00e5a0;
    margin-bottom:.6rem;
    display:flex; align-items:center; gap:.75rem;
    animation: slideIn .6s ease both;
}
.section-label::after { content:''; flex:1; height:1px; background:linear-gradient(to right, rgba(0,229,160,.3), transparent); max-width:200px; }

.section-title {
    font-family:'Syne', sans-serif;
    font-size:clamp(2rem, 4vw, 3.2rem);
    font-weight:700; color:#e8f4f0;
    margin-bottom:.5rem; line-height:1.1;
}
.section-sub {
    color:rgba(232,244,240,.45);
    font-size:.88rem; margin-bottom:3.5rem;
    max-width:50ch;
}

/* ─── Stats bar ─── */
.stats-row {
    display:grid; grid-template-columns:repeat(auto-fit, minmax(160px,1fr));
    gap:1px; background:rgba(0,229,160,.1);
    border:1px solid rgba(0,229,160,.1);
    margin: 4rem 6vw;
    animation: fadeUp .8s .3s ease both;
}
.stat-cell {
    padding:2.5rem 2rem; background:#050a0e;
    text-align:center;
    transition: background .3s;
}
.stat-cell:hover { background:rgba(0,229,160,.05); }
.stat-number {
    font-family:'Syne', sans-serif;
    font-size:3rem; font-weight:800;
    color:#00e5a0;
    animation: glow 3s ease infinite;
    display:block;
}
.stat-label {
    font-size:.72rem; letter-spacing:.15em; text-transform:uppercase;
    color:rgba(232,244,240,.4);
    margin-top:.4rem; display:block;
}

/* ─── Skills grid ─── */
.skills-grid {
    display:grid;
    grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));
    gap:1.5rem;
}

.skill-card {
    border:1px solid rgba(0,229,160,.12);
    padding:2rem; border-radius:4px;
    background:rgba(255,255,255,.015);
    transition: transform .3s, border-color .3s, box-shadow .3s;
    animation: fadeUp .6s ease both;
    position:relative; overflow:hidden;
}
.skill-card::before {
    content:''; position:absolute; top:0; left:0; right:0; height:2px;
    background:linear-gradient(90deg, transparent, #00e5a0, transparent);
    transform:translateX(-100%); transition:transform .4s;
}
.skill-card:hover { transform:translateY(-6px); border-color:rgba(0,229,160,.35); box-shadow:0 20px 50px rgba(0,229,160,.08); }
.skill-card:hover::before { transform:translateX(100%); }

.skill-icon { font-size:1.8rem; margin-bottom:1rem; display:block; }
.skill-name {
    font-family:'Syne', sans-serif;
    font-size:1.05rem; font-weight:700; color:#e8f4f0;
    margin-bottom:.5rem;
}
.skill-desc { font-size:.8rem; line-height:1.7; color:rgba(232,244,240,.45); }

/* ─── Progress bars ─── */
.prog-row { margin:.9rem 0; }
.prog-label { display:flex; justify-content:space-between; font-size:.75rem; color:rgba(232,244,240,.55); margin-bottom:.4rem; }
.prog-track { height:3px; background:rgba(255,255,255,.07); border-radius:2px; overflow:hidden; }
.prog-fill {
    height:100%; border-radius:2px;
    background:linear-gradient(90deg, #00e5a0, #00b8d9);
    animation:progressFill 1.4s cubic-bezier(.22,1,.36,1) both;
}

/* ─── Timeline ─── */
.timeline { position:relative; padding-left:2rem; }
.timeline::before { content:''; position:absolute; left:0; top:0; bottom:0; width:1px; background:linear-gradient(to bottom, #00e5a0, rgba(0,229,160,.1)); }

.tl-item { position:relative; margin-bottom:3rem; animation:fadeUp .6s ease both; }
.tl-dot {
    position:absolute; left:-2.4rem; top:.3rem;
    width:10px; height:10px; border-radius:50%;
    background:#00e5a0; border:2px solid #050a0e;
    box-shadow:0 0 0 3px rgba(0,229,160,.2);
}
.tl-period { font-size:.7rem; letter-spacing:.15em; text-transform:uppercase; color:#00e5a0; margin-bottom:.35rem; }
.tl-role { font-family:'Syne', sans-serif; font-size:1.15rem; font-weight:700; color:#e8f4f0; margin-bottom:.2rem; }
.tl-company { font-size:.8rem; color:rgba(232,244,240,.45); margin-bottom:.75rem; }
.tl-desc { font-size:.82rem; line-height:1.8; color:rgba(232,244,240,.55); }

/* ─── Project cards ─── */
.projects-grid { display:grid; grid-template-columns:repeat(auto-fit, minmax(320px,1fr)); gap:1.5rem; }

.project-card {
    border:1px solid rgba(0,229,160,.1);
    border-radius:4px; overflow:hidden;
    background:rgba(255,255,255,.01);
    transition:transform .3s, box-shadow .3s;
    animation:fadeUp .6s ease both;
}
.project-card:hover { transform:translateY(-8px); box-shadow:0 30px 60px rgba(0,229,160,.1); }

.project-header {
    padding:2rem; border-bottom:1px solid rgba(0,229,160,.07);
    background:rgba(0,229,160,.03);
    display:flex; justify-content:space-between; align-items:flex-start;
}
.project-title { font-family:'Syne', sans-serif; font-size:1.1rem; font-weight:700; color:#e8f4f0; }
.project-type { font-size:.65rem; letter-spacing:.15em; text-transform:uppercase; color:#00e5a0; padding:.3rem .7rem; border:1px solid rgba(0,229,160,.3); border-radius:2px; white-space:nowrap; }
.project-body { padding:1.75rem; }
.project-desc { font-size:.82rem; line-height:1.75; color:rgba(232,244,240,.5); margin-bottom:1.25rem; }
.project-tags { display:flex; flex-wrap:wrap; gap:.5rem; }
.tag { font-size:.65rem; letter-spacing:.1em; text-transform:uppercase; padding:.25rem .65rem; background:rgba(0,229,160,.07); border:1px solid rgba(0,229,160,.15); border-radius:2px; color:rgba(0,229,160,.8); }

/* ─── Tech stack ─── */
.tech-grid { display:flex; flex-wrap:wrap; gap:1rem; }
.tech-pill {
    display:flex; align-items:center; gap:.5rem;
    padding:.6rem 1.2rem;
    border:1px solid rgba(0,229,160,.15);
    border-radius:2px; background:rgba(0,229,160,.04);
    font-size:.78rem; color:rgba(232,244,240,.7);
    transition:transform .2s, border-color .2s;
    animation:fadeIn .5s ease both;
}
.tech-pill:hover { transform:translateY(-3px); border-color:rgba(0,229,160,.4); color:#00e5a0; }
.tech-pill span { font-size:1rem; }

/* ─── Contact ─── */
.contact-grid { display:grid; grid-template-columns:1fr 1fr; gap:4rem; }
@media(max-width:700px) { .contact-grid { grid-template-columns:1fr; } }

.contact-item {
    display:flex; align-items:flex-start; gap:1.25rem;
    padding:1.5rem; border:1px solid rgba(0,229,160,.1);
    border-radius:4px; transition:border-color .3s;
}
.contact-item:hover { border-color:rgba(0,229,160,.35); }
.contact-icon { font-size:1.4rem; flex-shrink:0; margin-top:.1rem; }
.contact-label { font-size:.68rem; letter-spacing:.2em; text-transform:uppercase; color:#00e5a0; margin-bottom:.25rem; }
.contact-value { font-size:.85rem; color:rgba(232,244,240,.7); word-break:break-all; }

/* ─── Footer ─── */
.footer {
    padding:2rem 6vw; text-align:center;
    border-top:1px solid rgba(0,229,160,.07);
    font-size:.72rem; color:rgba(232,244,240,.25);
    letter-spacing:.1em;
}
.footer span { color:rgba(0,229,160,.5); }

/* ─── Terminal badge ─── */
.terminal {
    font-family:'DM Mono', monospace;
    font-size:.78rem; line-height:1.8;
    background:rgba(0,0,0,.5);
    border:1px solid rgba(0,229,160,.15);
    border-radius:4px; padding:1.5rem;
    margin-top:3rem;
    position:relative;
}
.terminal::before { content:'● ● ●'; position:absolute; top:.6rem; left:1rem; font-size:.6rem; color:rgba(232,244,240,.2); letter-spacing:.3rem; }
.terminal-body { margin-top:.6rem; }
.t-prompt { color:rgba(0,229,160,.7); }
.t-cmd { color:#e8f4f0; }
.t-out { color:rgba(232,244,240,.4); }
.cursor { display:inline-block; width:8px; height:13px; background:#00e5a0; vertical-align:text-bottom; animation:blink 1s step-end infinite; }

/* Stagger delays for cards */
.skill-card:nth-child(1){ animation-delay:.05s; }
.skill-card:nth-child(2){ animation-delay:.12s; }
.skill-card:nth-child(3){ animation-delay:.19s; }
.skill-card:nth-child(4){ animation-delay:.26s; }
.skill-card:nth-child(5){ animation-delay:.33s; }
.skill-card:nth-child(6){ animation-delay:.40s; }

.project-card:nth-child(1){ animation-delay:.05s; }
.project-card:nth-child(2){ animation-delay:.15s; }
.project-card:nth-child(3){ animation-delay:.25s; }

.tl-item:nth-child(1){ animation-delay:.05s; }
.tl-item:nth-child(2){ animation-delay:.15s; }
.tl-item:nth-child(3){ animation-delay:.25s; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<section class="hero">

  <!-- floating SVG grid -->
  <svg class="hero-grid" viewBox="0 0 380 380" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="190" cy="190" r="170" stroke="#00e5a0" stroke-width=".5" stroke-dasharray="4 8"/>
    <circle cx="190" cy="190" r="130" stroke="#00b8d9" stroke-width=".5" stroke-dasharray="2 6"/>
    <circle cx="190" cy="190" r="90"  stroke="#00e5a0" stroke-width=".5" stroke-dasharray="1 4"/>
    <line x1="20" y1="190" x2="360" y2="190" stroke="#00e5a0" stroke-width=".3"/>
    <line x1="190" y1="20" x2="190" y2="360" stroke="#00e5a0" stroke-width=".3"/>
    <rect x="140" y="140" width="100" height="100" stroke="#00b8d9" stroke-width=".4" stroke-dasharray="3 5"/>
    <circle cx="190" cy="190" r="8" fill="#00e5a0" opacity=".6"/>
  </svg>

  <div class="status-badge">
    <span class="status-dot"></span>
    Available for new opportunities
  </div>

  <p class="hero-eyebrow">Senior Full-Stack Engineer</p>

  <h1 class="hero-name">Iftikhar<br><span>Hussain Shah</span></h1>

  <p class="hero-title">5 Years · Laravel PHP · ERP &amp; CRM Systems · AI-Augmented Development</p>

  <p class="hero-desc">
    I build robust enterprise-grade web systems — from real-estate ERP platforms
    to AI-integrated CRM solutions. Specialising in Laravel ecosystems, RESTful
    architecture, and modern DevOps pipelines that scale.
  </p>

  <div class="hero-cta">
    <a class="btn-primary" href="mailto:iftikhar@example.com">Get in Touch ↗</a>
    <a class="btn-secondary" href="#projects">View Projects →</a>
  </div>

  <div class="terminal" style="max-width:480px; margin-top:3rem;">
    <div class="terminal-body">
      <div><span class="t-prompt">~/portfolio $</span> <span class="t-cmd">whoami</span></div>
      <div class="t-out">Iftikhar Hussain Shah — Backend Architect &amp; API Specialist</div>
      <div style="margin-top:.4rem"><span class="t-prompt">~/portfolio $</span> <span class="t-cmd">skills --top 3</span></div>
      <div class="t-out">Laravel · Vue.js · AI/LLM Integration</div>
      <div style="margin-top:.4rem"><span class="t-prompt">~/portfolio $</span> <span class="t-cmd">status</span></div>
      <div class="t-out">⚡ Open to senior / lead roles &nbsp;<span class="cursor"></span></div>
    </div>
  </div>

</section>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# STATS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="stats-row">
  <div class="stat-cell">
    <span class="stat-number">5+</span>
    <span class="stat-label">Years Experience</span>
  </div>
  <div class="stat-cell">
    <span class="stat-number">30+</span>
    <span class="stat-label">Projects Delivered</span>
  </div>
  <div class="stat-cell">
    <span class="stat-number">12+</span>
    <span class="stat-label">ERP/CRM Modules</span>
  </div>
  <div class="stat-cell">
    <span class="stat-number">4</span>
    <span class="stat-label">Industry Sectors</span>
  </div>
  <div class="stat-cell">
    <span class="stat-number">99%</span>
    <span class="stat-label">Client Satisfaction</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# CORE SKILLS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<section class="section">
  <p class="section-label">Expertise</p>
  <h2 class="section-title">Core Competencies</h2>
  <p class="section-sub">A full-stack practitioner with a back-end-first mindset, deeply versed in enterprise architecture patterns.</p>

  <div class="skills-grid">

    <div class="skill-card">
      <span class="skill-icon">🔷</span>
      <p class="skill-name">Laravel &amp; PHP Ecosystem</p>
      <p class="skill-desc">Expert-level Laravel 10/11 — Eloquent ORM, Queues, Events, Sanctum/Passport auth, Livewire, Filament admin panels. PSR-12 clean code advocate.</p>
      <div style="margin-top:1.2rem;">
        <div class="prog-row"><div class="prog-label"><span>Laravel</span><span>97%</span></div><div class="prog-track"><div class="prog-fill" style="--w:97%"></div></div></div>
        <div class="prog-row"><div class="prog-label"><span>PHP 8.x</span><span>93%</span></div><div class="prog-track"><div class="prog-fill" style="--w:93%"></div></div></div>
        <div class="prog-row"><div class="prog-label"><span>Livewire / Filament</span><span>88%</span></div><div class="prog-track"><div class="prog-fill" style="--w:88%"></div></div></div>
      </div>
    </div>

    <div class="skill-card">
      <span class="skill-icon">🗄️</span>
      <p class="skill-name">Database Architecture</p>
      <p class="skill-desc">Designing high-performance relational schemas for ERP/CRM use-cases. MySQL, PostgreSQL, Redis caching, query optimisation, and full-text search.</p>
      <div style="margin-top:1.2rem;">
        <div class="prog-row"><div class="prog-label"><span>MySQL / PostgreSQL</span><span>92%</span></div><div class="prog-track"><div class="prog-fill" style="--w:92%"></div></div></div>
        <div class="prog-row"><div class="prog-label"><span>Redis</span><span>83%</span></div><div class="prog-track"><div class="prog-fill" style="--w:83%"></div></div></div>
        <div class="prog-row"><div class="prog-label"><span>Query Optimisation</span><span>90%</span></div><div class="prog-track"><div class="prog-fill" style="--w:90%"></div></div></div>
      </div>
    </div>

    <div class="skill-card">
      <span class="skill-icon">🤖</span>
      <p class="skill-name">AI &amp; LLM Integration</p>
      <p class="skill-desc">Integrating OpenAI GPT-4o, Claude API, and local LLMs into ERP workflows — AI-assisted data entry, smart search, document summarisation, and chatbots.</p>
      <div style="margin-top:1.2rem;">
        <div class="prog-row"><div class="prog-label"><span>OpenAI / Claude APIs</span><span>85%</span></div><div class="prog-track"><div class="prog-fill" style="--w:85%"></div></div></div>
        <div class="prog-row"><div class="prog-label"><span>Prompt Engineering</span><span>80%</span></div><div class="prog-track"><div class="prog-fill" style="--w:80%"></div></div></div>
        <div class="prog-row"><div class="prog-label"><span>RAG / Vector DBs</span><span>70%</span></div><div class="prog-track"><div class="prog-fill" style="--w:70%"></div></div></div>
      </div>
    </div>

    <div class="skill-card">
      <span class="skill-icon">⚙️</span>
      <p class="skill-name">API Design &amp; Microservices</p>
      <p class="skill-desc">RESTful and GraphQL API design. Microservice decomposition, inter-service messaging with RabbitMQ/Kafka, and OpenAPI 3.x documentation.</p>
      <div style="margin-top:1.2rem;">
        <div class="prog-row"><div class="prog-label"><span>REST API</span><span>95%</span></div><div class="prog-track"><div class="prog-fill" style="--w:95%"></div></div></div>
        <div class="prog-row"><div class="prog-label"><span>GraphQL</span><span>72%</span></div><div class="prog-track"><div class="prog-fill" style="--w:72%"></div></div></div>
        <div class="prog-row"><div class="prog-label"><span>RabbitMQ / Kafka</span><span>68%</span></div><div class="prog-track"><div class="prog-fill" style="--w:68%"></div></div></div>
      </div>
    </div>

    <div class="skill-card">
      <span class="skill-icon">🖥️</span>
      <p class="skill-name">Frontend — Vue &amp; Inertia</p>
      <p class="skill-desc">Vue 3 + Pinia + Vite for reactive SPA dashboards. Inertia.js for seamless Laravel-Vue monolith workflows. Tailwind CSS, Chart.js data visualisations.</p>
      <div style="margin-top:1.2rem;">
        <div class="prog-row"><div class="prog-label"><span>Vue 3</span><span>82%</span></div><div class="prog-track"><div class="prog-fill" style="--w:82%"></div></div></div>
        <div class="prog-row"><div class="prog-label"><span>Inertia.js</span><span>85%</span></div><div class="prog-track"><div class="prog-fill" style="--w:85%"></div></div></div>
        <div class="prog-row"><div class="prog-label"><span>Tailwind CSS</span><span>88%</span></div><div class="prog-track"><div class="prog-fill" style="--w:88%"></div></div></div>
      </div>
    </div>

    <div class="skill-card">
      <span class="skill-icon">🚀</span>
      <p class="skill-name">DevOps &amp; Cloud</p>
      <p class="skill-desc">CI/CD pipelines with GitHub Actions. Docker / Docker Compose. AWS EC2, S3, RDS deployments. Forge, Envoyer, and Nginx server management.</p>
      <div style="margin-top:1.2rem;">
        <div class="prog-row"><div class="prog-label"><span>Docker</span><span>80%</span></div><div class="prog-track"><div class="prog-fill" style="--w:80%"></div></div></div>
        <div class="prog-row"><div class="prog-label"><span>AWS</span><span>74%</span></div><div class="prog-track"><div class="prog-fill" style="--w:74%"></div></div></div>
        <div class="prog-row"><div class="prog-label"><span>CI/CD</span><span>82%</span></div><div class="prog-track"><div class="prog-fill" style="--w:82%"></div></div></div>
      </div>
    </div>

  </div>
</section>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# EXPERIENCE TIMELINE
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<section class="section section-alt">
  <p class="section-label">Career</p>
  <h2 class="section-title">Experience</h2>
  <p class="section-sub">Five years of shipping production software across real estate, finance, and enterprise SaaS.</p>

  <div class="timeline">

    <div class="tl-item">
      <div class="tl-dot"></div>
      <p class="tl-period">2023 — Present</p>
      <p class="tl-role">Senior Laravel Developer</p>
      <p class="tl-company">Enterprise Software Studio — Remote</p>
      <p class="tl-desc">
        Leading backend architecture for a multi-tenant real-estate ERP platform serving 30+ agencies.
        Introduced AI-assisted property valuation module using GPT-4o API, cutting manual appraisal time by 60%.
        Mentored a team of 4 junior developers; enforced TDD with PHPUnit &amp; Pest.
        Migrated monolith to service-oriented architecture on AWS — 99.9% uptime achieved.
      </p>
    </div>

    <div class="tl-item">
      <div class="tl-dot"></div>
      <p class="tl-period">2021 — 2023</p>
      <p class="tl-role">Full-Stack Laravel Developer</p>
      <p class="tl-company">PropTech Solutions Pvt. Ltd — Rawalpindi</p>
      <p class="tl-desc">
        Built a CRM system for real-estate brokerages from scratch: lead pipeline management, automated
        follow-up sequences, commission tracking, and contract generation via PDF APIs.
        Integrated WhatsApp Business API and Twilio SMS for automated client communication.
        Reduced lead response time from 4 hours to under 8 minutes with Laravel Queues.
      </p>
    </div>

    <div class="tl-item">
      <div class="tl-dot"></div>
      <p class="tl-period">2019 — 2021</p>
      <p class="tl-role">Junior PHP Developer</p>
      <p class="tl-company">WebCraft Agency — Islamabad</p>
      <p class="tl-desc">
        Developed and maintained custom Laravel applications for SME clients across retail, e-commerce,
        and hospitality verticals. Built reusable Blade component libraries and payment gateway integrations
        (Stripe, JazzCash). Gained solid foundations in RESTful API design and MySQL optimisation.
      </p>
    </div>

  </div>
</section>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PROJECTS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<section class="section" id="projects">
  <p class="section-label">Work</p>
  <h2 class="section-title">Featured Projects</h2>
  <p class="section-sub">Handpicked deliverables demonstrating depth across ERP, CRM, and AI-augmented products.</p>

  <div class="projects-grid">

    <div class="project-card">
      <div class="project-header">
        <p class="project-title">RealEstate360 ERP</p>
        <span class="project-type">ERP · SaaS</span>
      </div>
      <div class="project-body">
        <p class="project-desc">
          Multi-tenant ERP platform for real-estate agencies. Covers inventory management, sales
          pipeline, agent commission ledgers, document management, and a GPT-4o-powered
          AI assistant for property queries and report generation.
        </p>
        <div class="project-tags">
          <span class="tag">Laravel 11</span><span class="tag">Vue 3</span>
          <span class="tag">Inertia</span><span class="tag">PostgreSQL</span>
          <span class="tag">OpenAI API</span><span class="tag">AWS S3</span>
        </div>
      </div>
    </div>

    <div class="project-card">
      <div class="project-header">
        <p class="project-title">LeadFlow CRM</p>
        <span class="project-type">CRM · Automation</span>
      </div>
      <div class="project-body">
        <p class="project-desc">
          End-to-end CRM for real-estate brokers: lead capture from 10+ portals, automated
          WhatsApp &amp; SMS drip campaigns, deal tracking, and AI-assisted follow-up
          suggestion engine trained on historical closing data.
        </p>
        <div class="project-tags">
          <span class="tag">Laravel</span><span class="tag">Livewire</span>
          <span class="tag">Redis</span><span class="tag">Twilio</span>
          <span class="tag">WhatsApp API</span><span class="tag">Claude AI</span>
        </div>
      </div>
    </div>

    <div class="project-card">
      <div class="project-header">
        <p class="project-title">FinOps Tracker</p>
        <span class="project-type">Finance · ERP Module</span>
      </div>
      <div class="project-body">
        <p class="project-desc">
          Accounting and financial operations module plugged into existing ERP ecosystems.
          Features accounts payable/receivable, multi-currency support, bank reconciliation,
          automated VAT reporting, and exportable audit trails in PDF/Excel.
        </p>
        <div class="project-tags">
          <span class="tag">Laravel</span><span class="tag">MySQL</span>
          <span class="tag">Filament</span><span class="tag">Spatie</span>
          <span class="tag">Laravel Excel</span><span class="tag">DomPDF</span>
        </div>
      </div>
    </div>

    <div class="project-card">
      <div class="project-header">
        <p class="project-title">DocuScan AI</p>
        <span class="project-type">AI · Document Processing</span>
      </div>
      <div class="project-body">
        <p class="project-desc">
          Automated property document intake system. Uses OCR + LLM pipeline to extract key
          fields from title deeds, NOC certificates, and mortgage papers — pushing structured
          data directly into ERP records with 94% accuracy.
        </p>
        <div class="project-tags">
          <span class="tag">Python</span><span class="tag">FastAPI</span>
          <span class="tag">Laravel API</span><span class="tag">Tesseract</span>
          <span class="tag">GPT-4o Vision</span><span class="tag">Pinecone</span>
        </div>
      </div>
    </div>

    <div class="project-card">
      <div class="project-header">
        <p class="project-title">PropPortal Mobile API</p>
        <span class="project-type">API · Mobile Backend</span>
      </div>
      <div class="project-body">
        <p class="project-desc">
          Headless REST API backend for a cross-platform property listing mobile app (Flutter).
          JWT auth, geolocation-based search, saved search alerts via FCM push notifications,
          and real-time chat between buyers and agents via WebSockets.
        </p>
        <div class="project-tags">
          <span class="tag">Laravel Sanctum</span><span class="tag">WebSockets</span>
          <span class="tag">FCM</span><span class="tag">Elasticsearch</span>
          <span class="tag">Redis</span><span class="tag">Docker</span>
        </div>
      </div>
    </div>

    <div class="project-card">
      <div class="project-header">
        <p class="project-title">HR &amp; Payroll Module</p>
        <span class="project-type">ERP · HR</span>
      </div>
      <div class="project-body">
        <p class="project-desc">
          Integrated HR module for a 500-employee real-estate group: biometric attendance sync,
          leave management, payroll computation with tax slabs, loan deductions, and
          self-service employee portal with role-based access.
        </p>
        <div class="project-tags">
          <span class="tag">Laravel</span><span class="tag">Vue 3</span>
          <span class="tag">Filament</span><span class="tag">Spatie Roles</span>
          <span class="tag">Charts.js</span><span class="tag">MySQL</span>
        </div>
      </div>
    </div>

  </div>
</section>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TECH STACK
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<section class="section section-alt">
  <p class="section-label">Toolbox</p>
  <h2 class="section-title">Full Tech Stack</h2>
  <p class="section-sub">Technologies I use day-to-day to deliver production-ready systems.</p>

  <div class="tech-grid">
    <div class="tech-pill"><span>🔷</span> Laravel 10/11</div>
    <div class="tech-pill"><span>🐘</span> PHP 8.2</div>
    <div class="tech-pill"><span>💚</span> Vue 3 + Pinia</div>
    <div class="tech-pill"><span>⚡</span> Inertia.js</div>
    <div class="tech-pill"><span>🌬️</span> Tailwind CSS</div>
    <div class="tech-pill"><span>🔥</span> Livewire 3</div>
    <div class="tech-pill"><span>🎯</span> Filament 3</div>
    <div class="tech-pill"><span>🗃️</span> MySQL 8</div>
    <div class="tech-pill"><span>🐘</span> PostgreSQL 16</div>
    <div class="tech-pill"><span>🔴</span> Redis</div>
    <div class="tech-pill"><span>🔍</span> Elasticsearch</div>
    <div class="tech-pill"><span>🐳</span> Docker</div>
    <div class="tech-pill"><span>☁️</span> AWS EC2 / S3</div>
    <div class="tech-pill"><span>⚙️</span> GitHub Actions</div>
    <div class="tech-pill"><span>🤖</span> OpenAI GPT-4o</div>
    <div class="tech-pill"><span>🧠</span> Claude API</div>
    <div class="tech-pill"><span>📌</span> Pinecone</div>
    <div class="tech-pill"><span>🐍</span> Python / FastAPI</div>
    <div class="tech-pill"><span>📦</span> RabbitMQ</div>
    <div class="tech-pill"><span>💬</span> Twilio / WA API</div>
    <div class="tech-pill"><span>🧪</span> Pest / PHPUnit</div>
    <div class="tech-pill"><span>📝</span> Swagger / OpenAPI</div>
    <div class="tech-pill"><span>🔐</span> Laravel Sanctum</div>
    <div class="tech-pill"><span>🌐</span> Nginx</div>
  </div>
</section>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<section class="section">
  <p class="section-label">Contact</p>
  <h2 class="section-title">Let's Build Something</h2>
  <p class="section-sub">Open to senior engineering roles, technical leadership, and freelance ERP/CRM projects.</p>

  <div class="contact-grid">
    <div>
      <div class="contact-item" style="margin-bottom:1rem;">
        <span class="contact-icon">📧</span>
        <div>
          <p class="contact-label">Email</p>
          <p class="contact-value">iftikhar.hshah@gmail.com</p>
        </div>
      </div>
      <div class="contact-item" style="margin-bottom:1rem;">
        <span class="contact-icon">💼</span>
        <div>
          <p class="contact-label">LinkedIn</p>
          <p class="contact-value">linkedin.com/in/iftikhar-hussain-shah</p>
        </div>
      </div>
      <div class="contact-item" style="margin-bottom:1rem;">
        <span class="contact-icon">🐙</span>
        <div>
          <p class="contact-label">GitHub</p>
          <p class="contact-value">github.com/iftikhar-hshah</p>
        </div>
      </div>
      <div class="contact-item">
        <span class="contact-icon">📍</span>
        <div>
          <p class="contact-label">Location</p>
          <p class="contact-value">Rawalpindi, Pakistan · Open to Remote</p>
        </div>
      </div>
    </div>

    <div>
      <div class="terminal">
        <div class="terminal-body">
          <div><span class="t-prompt">$ </span><span class="t-cmd">cat availability.txt</span></div>
          <div class="t-out" style="margin-top:.4rem;">
            Status    : ✅ Available<br>
            Notice    : Immediate<br>
            Preferred : Remote / Hybrid<br>
            Timezone  : PKT (UTC+5)<br>
            Rate      : Negotiable
          </div>
          <div style="margin-top:.8rem;"><span class="t-prompt">$ </span><span class="t-cmd">cat specialisations.txt</span></div>
          <div class="t-out" style="margin-top:.4rem;">
            ✔ ERP &amp; CRM Architecture<br>
            ✔ Real Estate Tech Platforms<br>
            ✔ AI/LLM Feature Integration<br>
            ✔ API Design &amp; Microservices<br>
            ✔ Team Lead &amp; Code Review
          </div>
          <div style="margin-top:.8rem;"><span class="t-prompt">$ </span><span class="cursor"></span></div>
        </div>
      </div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
  Crafted with <span>⚡</span> by Iftikhar Hussain Shah &nbsp;·&nbsp; 2025 &nbsp;·&nbsp;
  Built with <span>Streamlit + Laravel spirit</span>
</div>
""", unsafe_allow_html=True)