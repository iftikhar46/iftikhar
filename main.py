import streamlit as st

st.set_page_config(
    page_title="Iftikhar Hussain Shah | Senior Laravel Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Inject all CSS + hide Streamlit chrome ───────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Mono:wght@400;500&family=Instrument+Serif:ital@1&display=swap');

/* hide streamlit ui */
#MainMenu, header, footer,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stHeader"] { display:none !important; }
.block-container { padding:0 !important; max-width:100% !important; }
section[data-testid="stMain"] > div { padding:0 !important; }

/* global */
html,body,[data-testid="stAppViewContainer"]{
  background:#050a0e !important;
  color:#e8f4f0;
  font-family:'DM Mono',monospace;
}

/* scrollbar */
::-webkit-scrollbar{width:4px;}
::-webkit-scrollbar-track{background:#050a0e;}
::-webkit-scrollbar-thumb{background:#00e5a0;border-radius:2px;}

/* animations */
@keyframes fadeUp{from{opacity:0;transform:translateY(32px)}to{opacity:1;transform:translateY(0)}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(0,229,160,.45)}70%{box-shadow:0 0 0 14px rgba(0,229,160,0)}}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
@keyframes shimmer{0%{background-position:-200% center}100%{background-position:200% center}}
@keyframes glow{0%,100%{text-shadow:0 0 18px rgba(0,229,160,.35)}50%{text-shadow:0 0 36px rgba(0,229,160,.8)}}
@keyframes progFill{from{width:0}to{width:var(--w)}}
@keyframes cardIn{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}
@keyframes scanline{0%{top:-4px}100%{top:100vh}}
@keyframes borderA{0%,100%{border-color:rgba(0,229,160,.4)}50%{border-color:rgba(0,184,217,.55)}}

/* noise */
body::before{content:'';position:fixed;inset:0;pointer-events:none;z-index:0;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.03'/%3E%3C/svg%3E");
  background-size:180px;opacity:.4;}

/* scanline */
.scanline{position:fixed;left:0;top:-4px;width:100%;height:3px;
  background:linear-gradient(transparent,rgba(0,229,160,.07),transparent);
  pointer-events:none;z-index:999;animation:scanline 9s linear infinite;}

/* ───── HERO ───── */
.hero{
  min-height:100vh;
  display:flex;flex-direction:column;justify-content:center;align-items:flex-start;
  padding:6rem 7vw 5rem;
  position:relative;overflow:hidden;
  background:
    radial-gradient(ellipse 75% 55% at 72% 48%,rgba(0,229,160,.08) 0%,transparent 65%),
    radial-gradient(ellipse 38% 38% at 18% 78%,rgba(0,184,217,.06) 0%,transparent 55%),
    #050a0e;
}
.hero-svg{position:absolute;right:6vw;top:50%;transform:translateY(-50%);
  width:clamp(220px,28vw,380px);opacity:.12;
  animation:float 7s ease-in-out infinite;}
.status-badge{display:inline-flex;align-items:center;gap:.5rem;
  padding:.38rem 1rem;border-radius:20px;
  background:rgba(0,229,160,.08);border:1px solid rgba(0,229,160,.22);
  font-size:.71rem;color:#00e5a0;margin-bottom:1.4rem;
  animation:fadeIn .8s .1s ease both;}
.sdot{width:7px;height:7px;border-radius:50%;background:#00e5a0;
  display:inline-block;flex-shrink:0;animation:pulse 1.6s infinite;}
.eyebrow{font-size:.73rem;letter-spacing:.26em;text-transform:uppercase;color:#00e5a0;
  display:flex;align-items:center;gap:.7rem;margin-bottom:.55rem;
  animation:fadeUp .6s .25s ease both;}
.eyebrow::before{content:'';width:30px;height:1px;background:#00e5a0;flex-shrink:0;}
.hname{font-family:'Syne',sans-serif;
  font-size:clamp(2.8rem,8.5vw,7.5rem);font-weight:800;line-height:.93;
  color:#e8f4f0;margin-bottom:.5rem;
  animation:fadeUp .7s .4s ease both;}
.hname-g{background:linear-gradient(135deg,#00e5a0 0%,#00b8d9 50%,#00e5a0 100%);
  background-size:200% auto;
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  animation:shimmer 3s linear infinite;}
.htitle{font-family:'Instrument Serif',serif;font-style:italic;
  font-size:clamp(.9rem,2vw,1.35rem);color:rgba(232,244,240,.52);
  margin-bottom:1.6rem;animation:fadeUp .7s .55s ease both;}
.hdesc{max-width:50ch;font-size:.86rem;line-height:1.95;color:rgba(232,244,240,.58);
  border-left:2px solid rgba(0,229,160,.3);padding-left:1.2rem;
  margin-bottom:2.2rem;animation:fadeUp .7s .7s ease both;}
.hbtns{display:flex;gap:1rem;flex-wrap:wrap;animation:fadeUp .7s .85s ease both;}
.btnp{font-family:'DM Mono',monospace;font-size:.76rem;letter-spacing:.12em;
  text-transform:uppercase;padding:.82rem 1.9rem;background:#00e5a0;color:#050a0e;
  border:none;border-radius:2px;cursor:pointer;font-weight:600;
  transition:transform .2s,box-shadow .2s;animation:pulse 2.8s infinite;
  text-decoration:none;display:inline-block;}
.btnp:hover{transform:translateY(-3px);box-shadow:0 12px 28px rgba(0,229,160,.4);}
.btns{font-family:'DM Mono',monospace;font-size:.76rem;letter-spacing:.12em;
  text-transform:uppercase;padding:.82rem 1.9rem;background:transparent;color:#00e5a0;
  border:1px solid rgba(0,229,160,.38);border-radius:2px;cursor:pointer;
  transition:transform .2s,border-color .2s;text-decoration:none;display:inline-block;
  animation:borderA 3s ease infinite;}
.btns:hover{transform:translateY(-3px);border-color:#00e5a0;}
.term{font-family:'DM Mono',monospace;font-size:.75rem;line-height:1.9;
  background:rgba(0,0,0,.55);border:1px solid rgba(0,229,160,.16);border-radius:4px;
  padding:1.4rem 1.4rem 1.2rem;margin-top:2.4rem;max-width:460px;position:relative;
  animation:fadeUp .7s 1s ease both;}
.term::before{content:'● ● ●';position:absolute;top:.52rem;left:1rem;
  font-size:.58rem;color:rgba(232,244,240,.18);letter-spacing:.3rem;}
.tb{margin-top:.45rem;}
.tp{color:rgba(0,229,160,.75);}
.tc{color:#e8f4f0;}
.to{color:rgba(232,244,240,.42);}
.cur{display:inline-block;width:7px;height:12px;background:#00e5a0;
  vertical-align:text-bottom;animation:blink 1s step-end infinite;}

/* ───── STATS ───── */
.stats{display:grid;grid-template-columns:repeat(5,1fr);
  background:rgba(0,229,160,.09);
  border-top:1px solid rgba(0,229,160,.1);
  border-bottom:1px solid rgba(0,229,160,.1);}
@media(max-width:700px){.stats{grid-template-columns:repeat(2,1fr);}}
.sc{padding:2.2rem 1.2rem;background:#050a0e;text-align:center;
  border-right:1px solid rgba(0,229,160,.09);transition:background .3s;}
.sc:last-child{border-right:none;}
.sc:hover{background:rgba(0,229,160,.05);}
.sn{font-family:'Syne',sans-serif;font-size:2.6rem;font-weight:800;
  color:#00e5a0;display:block;animation:glow 3s ease infinite;}
.sl{font-size:.65rem;letter-spacing:.14em;text-transform:uppercase;
  color:rgba(232,244,240,.38);margin-top:.38rem;display:block;}

/* ───── SECTION ───── */
.sec{padding:5rem 7vw;position:relative;}
.sec-alt{background:rgba(0,229,160,.018);
  border-top:1px solid rgba(0,229,160,.07);
  border-bottom:1px solid rgba(0,229,160,.07);}
.lbl{font-size:.68rem;letter-spacing:.3em;text-transform:uppercase;color:#00e5a0;
  margin-bottom:.55rem;display:flex;align-items:center;gap:.7rem;}
.lbl::after{content:'';flex:1;height:1px;
  background:linear-gradient(to right,rgba(0,229,160,.3),transparent);max-width:180px;}
.stitle{font-family:'Syne',sans-serif;font-size:clamp(1.7rem,3.8vw,2.8rem);
  font-weight:700;color:#e8f4f0;margin-bottom:.38rem;line-height:1.1;}
.ssub{color:rgba(232,244,240,.4);font-size:.83rem;margin-bottom:2.8rem;max-width:50ch;}

/* ───── SKILL CARDS ───── */
.sg{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1.3rem;}
.skc{border:1px solid rgba(0,229,160,.13);padding:1.8rem;border-radius:4px;
  background:rgba(255,255,255,.013);
  transition:transform .3s,border-color .3s,box-shadow .3s;
  position:relative;overflow:hidden;animation:cardIn .6s ease both;}
.skc::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent,#00e5a0,transparent);
  transform:translateX(-100%);transition:transform .45s;}
.skc:hover{transform:translateY(-5px);border-color:rgba(0,229,160,.38);
  box-shadow:0 18px 45px rgba(0,229,160,.08);}
.skc:hover::before{transform:translateX(100%);}
.skc:nth-child(1){animation-delay:.04s}.skc:nth-child(2){animation-delay:.11s}
.skc:nth-child(3){animation-delay:.18s}.skc:nth-child(4){animation-delay:.25s}
.skc:nth-child(5){animation-delay:.32s}.skc:nth-child(6){animation-delay:.39s}
.skie{font-size:1.65rem;margin-bottom:.85rem;display:block;}
.skn{font-family:'Syne',sans-serif;font-size:.97rem;font-weight:700;color:#e8f4f0;margin-bottom:.4rem;}
.skd{font-size:.76rem;line-height:1.75;color:rgba(232,244,240,.43);margin-bottom:.95rem;}
.pr{margin:.65rem 0;}
.prl{display:flex;justify-content:space-between;font-size:.7rem;color:rgba(232,244,240,.48);margin-bottom:.3rem;}
.prt{height:3px;background:rgba(255,255,255,.07);border-radius:2px;overflow:hidden;}
.prf{height:100%;border-radius:2px;background:linear-gradient(90deg,#00e5a0,#00b8d9);
  animation:progFill 1.5s cubic-bezier(.22,1,.36,1) both;}

/* ───── TIMELINE ───── */
.tl{position:relative;padding-left:1.9rem;}
.tl::before{content:'';position:absolute;left:0;top:0;bottom:0;width:1px;
  background:linear-gradient(to bottom,#00e5a0,rgba(0,229,160,.06));}
.tli{position:relative;margin-bottom:2.6rem;animation:cardIn .6s ease both;}
.tli:nth-child(1){animation-delay:.04s}.tli:nth-child(2){animation-delay:.17s}.tli:nth-child(3){animation-delay:.3s}
.tld{position:absolute;left:-2.3rem;top:.28rem;width:9px;height:9px;
  border-radius:50%;background:#00e5a0;border:2px solid #050a0e;
  box-shadow:0 0 0 3px rgba(0,229,160,.2);}
.tlp{font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:#00e5a0;margin-bottom:.26rem;}
.tlr{font-family:'Syne',sans-serif;font-size:1.06rem;font-weight:700;color:#e8f4f0;margin-bottom:.16rem;}
.tlco{font-size:.75rem;color:rgba(232,244,240,.4);margin-bottom:.6rem;}
.tlde{font-size:.78rem;line-height:1.85;color:rgba(232,244,240,.5);}

/* ───── PROJECTS ───── */
.pg{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.3rem;}
.pc{border:1px solid rgba(0,229,160,.11);border-radius:4px;overflow:hidden;
  background:rgba(255,255,255,.01);transition:transform .3s,box-shadow .3s;
  animation:cardIn .6s ease both;}
.pc:hover{transform:translateY(-7px);box-shadow:0 26px 52px rgba(0,229,160,.1);}
.pc:nth-child(1){animation-delay:.04s}.pc:nth-child(2){animation-delay:.14s}
.pc:nth-child(3){animation-delay:.24s}.pc:nth-child(4){animation-delay:.34s}
.pc:nth-child(5){animation-delay:.44s}.pc:nth-child(6){animation-delay:.54s}
.ph{padding:1.55rem;border-bottom:1px solid rgba(0,229,160,.07);
  background:rgba(0,229,160,.03);display:flex;justify-content:space-between;
  align-items:flex-start;gap:.8rem;}
.pt{font-family:'Syne',sans-serif;font-size:1rem;font-weight:700;color:#e8f4f0;}
.pty{font-size:.6rem;letter-spacing:.11em;text-transform:uppercase;color:#00e5a0;
  padding:.24rem .58rem;border:1px solid rgba(0,229,160,.28);border-radius:2px;
  white-space:nowrap;flex-shrink:0;}
.pb{padding:1.45rem;}
.pd{font-size:.78rem;line-height:1.8;color:rgba(232,244,240,.46);margin-bottom:1rem;}
.ptags{display:flex;flex-wrap:wrap;gap:.4rem;}
.tag{font-size:.6rem;letter-spacing:.08em;text-transform:uppercase;padding:.2rem .52rem;
  background:rgba(0,229,160,.07);border:1px solid rgba(0,229,160,.15);
  border-radius:2px;color:rgba(0,229,160,.82);}

/* ───── TECH ───── */
.tg{display:flex;flex-wrap:wrap;gap:.85rem;}
.tpill{display:flex;align-items:center;gap:.42rem;padding:.5rem 1rem;
  border:1px solid rgba(0,229,160,.14);border-radius:2px;background:rgba(0,229,160,.03);
  font-size:.74rem;color:rgba(232,244,240,.66);
  transition:transform .2s,border-color .2s,color .2s;}
.tpill:hover{transform:translateY(-3px);border-color:rgba(0,229,160,.4);color:#00e5a0;}

/* ───── CONTACT ───── */
.cg{display:grid;grid-template-columns:1fr 1fr;gap:3rem;}
@media(max-width:680px){.cg{grid-template-columns:1fr;}}
.ci{display:flex;align-items:flex-start;gap:1rem;padding:1.25rem;
  border:1px solid rgba(0,229,160,.11);border-radius:4px;margin-bottom:.85rem;
  transition:border-color .3s;}
.ci:hover{border-color:rgba(0,229,160,.38);}
.cie{font-size:1.2rem;flex-shrink:0;margin-top:.08rem;}
.cil{font-size:.62rem;letter-spacing:.2em;text-transform:uppercase;color:#00e5a0;margin-bottom:.16rem;}
.civ{font-size:.79rem;color:rgba(232,244,240,.63);word-break:break-all;}

/* ───── FOOTER ───── */
.ft{padding:1.7rem 7vw;text-align:center;border-top:1px solid rgba(0,229,160,.07);
  font-size:.67rem;color:rgba(232,244,240,.2);letter-spacing:.1em;}
.ft span{color:rgba(0,229,160,.55);}
</style>
<div class="scanline"></div>
""", unsafe_allow_html=True)

# ─── HERO ────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="hero">
  <svg class="hero-svg" viewBox="0 0 380 380" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="190" cy="190" r="170" stroke="#00e5a0" stroke-width=".5" stroke-dasharray="4 8"/>
    <circle cx="190" cy="190" r="130" stroke="#00b8d9" stroke-width=".5" stroke-dasharray="2 6"/>
    <circle cx="190" cy="190" r="90"  stroke="#00e5a0" stroke-width=".5" stroke-dasharray="1 4"/>
    <circle cx="190" cy="190" r="50"  stroke="#00b8d9" stroke-width=".4" stroke-dasharray="2 4"/>
    <line x1="20" y1="190" x2="360" y2="190" stroke="#00e5a0" stroke-width=".3"/>
    <line x1="190" y1="20" x2="190" y2="360" stroke="#00e5a0" stroke-width=".3"/>
    <rect x="145" y="145" width="90" height="90" stroke="#00b8d9" stroke-width=".4" stroke-dasharray="3 5"/>
    <circle cx="190" cy="190" r="9" fill="#00e5a0" opacity=".7"/>
    <circle cx="190" cy="20"  r="4" fill="#00b8d9" opacity=".5"/>
    <circle cx="360" cy="190" r="4" fill="#00e5a0" opacity=".5"/>
    <circle cx="190" cy="360" r="4" fill="#00b8d9" opacity=".5"/>
    <circle cx="20"  cy="190" r="4" fill="#00e5a0" opacity=".5"/>
  </svg>
  <div class="status-badge"><span class="sdot"></span>&nbsp;Available for new opportunities</div>
  <p class="eyebrow">Senior Full-Stack Engineer</p>
  <h1 class="hname">Iftikhar<br><span class="hname-g">Hussain Shah</span></h1>
  <p class="htitle">5 Years &middot; Laravel PHP &middot; ERP &amp; CRM Systems &middot; AI-Augmented Development</p>
  <p class="hdesc">I build robust enterprise-grade web systems — from real-estate ERP platforms to AI-integrated CRM solutions. Specialising in Laravel ecosystems, RESTful architecture, and modern DevOps pipelines that scale.</p>
  <div class="hbtns">
    <a class="btnp" href="mailto:iftikhar.hshah@gmail.com">Get in Touch &nearr;</a>
    <a class="btns" href="#projects">View Projects &rarr;</a>
  </div>
  <div class="term">
    <div class="tb">
      <div><span class="tp">~/portfolio $</span> <span class="tc">whoami</span></div>
      <div class="to">Iftikhar Hussain Shah — Backend Architect &amp; API Specialist</div>
      <div style="margin-top:.38rem"><span class="tp">~/portfolio $</span> <span class="tc">skills --top 3</span></div>
      <div class="to">Laravel &nbsp;&bull;&nbsp; Vue.js &nbsp;&bull;&nbsp; AI/LLM Integration</div>
      <div style="margin-top:.38rem"><span class="tp">~/portfolio $</span> <span class="tc">status</span></div>
      <div class="to">&#9889; Open to senior / lead roles &nbsp;<span class="cur"></span></div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ─── STATS ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats">
  <div class="sc"><span class="sn">5+</span><span class="sl">Years Experience</span></div>
  <div class="sc"><span class="sn">30+</span><span class="sl">Projects Delivered</span></div>
  <div class="sc"><span class="sn">12+</span><span class="sl">ERP/CRM Modules</span></div>
  <div class="sc"><span class="sn">4</span><span class="sl">Industry Sectors</span></div>
  <div class="sc"><span class="sn">99%</span><span class="sl">Client Satisfaction</span></div>
</div>
""", unsafe_allow_html=True)

# ─── SKILLS ──────────────────────────────────────────────────────────────────
st.markdown("""
<section class="sec">
  <p class="lbl">Expertise</p>
  <h2 class="stitle">Core Competencies</h2>
  <p class="ssub">A full-stack practitioner with a back-end-first mindset, deeply versed in enterprise architecture patterns.</p>
  <div class="sg">

    <div class="skc">
      <span class="skie">&#128311;</span>
      <p class="skn">Laravel &amp; PHP Ecosystem</p>
      <p class="skd">Expert-level Laravel 10/11 — Eloquent ORM, Queues, Events, Sanctum/Passport auth, Livewire, Filament admin panels. PSR-12 clean code advocate.</p>
      <div class="pr"><div class="prl"><span>Laravel</span><span>97%</span></div><div class="prt"><div class="prf" style="--w:97%"></div></div></div>
      <div class="pr"><div class="prl"><span>PHP 8.x</span><span>93%</span></div><div class="prt"><div class="prf" style="--w:93%"></div></div></div>
      <div class="pr"><div class="prl"><span>Livewire / Filament</span><span>88%</span></div><div class="prt"><div class="prf" style="--w:88%"></div></div></div>
    </div>

    <div class="skc">
      <span class="skie">&#128451;</span>
      <p class="skn">Database Architecture</p>
      <p class="skd">High-performance relational schemas for ERP/CRM. MySQL, PostgreSQL, Redis caching, query optimisation, and full-text search at scale.</p>
      <div class="pr"><div class="prl"><span>MySQL / PostgreSQL</span><span>92%</span></div><div class="prt"><div class="prf" style="--w:92%"></div></div></div>
      <div class="pr"><div class="prl"><span>Redis</span><span>83%</span></div><div class="prt"><div class="prf" style="--w:83%"></div></div></div>
      <div class="pr"><div class="prl"><span>Query Optimisation</span><span>90%</span></div><div class="prt"><div class="prf" style="--w:90%"></div></div></div>
    </div>

    <div class="skc">
      <span class="skie">&#129302;</span>
      <p class="skn">AI &amp; LLM Integration</p>
      <p class="skd">Integrating OpenAI GPT-4o &amp; Claude API into ERP workflows — AI data entry, smart search, document summarisation, and embedded chatbots.</p>
      <div class="pr"><div class="prl"><span>OpenAI / Claude APIs</span><span>85%</span></div><div class="prt"><div class="prf" style="--w:85%"></div></div></div>
      <div class="pr"><div class="prl"><span>Prompt Engineering</span><span>80%</span></div><div class="prt"><div class="prf" style="--w:80%"></div></div></div>
      <div class="pr"><div class="prl"><span>RAG / Vector DBs</span><span>70%</span></div><div class="prt"><div class="prf" style="--w:70%"></div></div></div>
    </div>

    <div class="skc">
      <span class="skie">&#9881;</span>
      <p class="skn">API Design &amp; Microservices</p>
      <p class="skd">RESTful and GraphQL API design, microservice decomposition, inter-service messaging with RabbitMQ/Kafka, and OpenAPI 3.x docs.</p>
      <div class="pr"><div class="prl"><span>REST API</span><span>95%</span></div><div class="prt"><div class="prf" style="--w:95%"></div></div></div>
      <div class="pr"><div class="prl"><span>GraphQL</span><span>72%</span></div><div class="prt"><div class="prf" style="--w:72%"></div></div></div>
      <div class="pr"><div class="prl"><span>RabbitMQ / Kafka</span><span>68%</span></div><div class="prt"><div class="prf" style="--w:68%"></div></div></div>
    </div>

    <div class="skc">
      <span class="skie">&#128187;</span>
      <p class="skn">Frontend — Vue &amp; Inertia</p>
      <p class="skd">Vue 3 + Pinia + Vite for reactive SPA dashboards. Inertia.js for seamless Laravel-Vue workflows. Tailwind CSS, Chart.js visualisations.</p>
      <div class="pr"><div class="prl"><span>Vue 3</span><span>82%</span></div><div class="prt"><div class="prf" style="--w:82%"></div></div></div>
      <div class="pr"><div class="prl"><span>Inertia.js</span><span>85%</span></div><div class="prt"><div class="prf" style="--w:85%"></div></div></div>
      <div class="pr"><div class="prl"><span>Tailwind CSS</span><span>88%</span></div><div class="prt"><div class="prf" style="--w:88%"></div></div></div>
    </div>

    <div class="skc">
      <span class="skie">&#128640;</span>
      <p class="skn">DevOps &amp; Cloud</p>
      <p class="skd">CI/CD with GitHub Actions, Docker / Compose, AWS EC2/S3/RDS deployments, Laravel Forge, Envoyer, and Nginx server management.</p>
      <div class="pr"><div class="prl"><span>Docker</span><span>80%</span></div><div class="prt"><div class="prf" style="--w:80%"></div></div></div>
      <div class="pr"><div class="prl"><span>AWS</span><span>74%</span></div><div class="prt"><div class="prf" style="--w:74%"></div></div></div>
      <div class="pr"><div class="prl"><span>CI/CD</span><span>82%</span></div><div class="prt"><div class="prf" style="--w:82%"></div></div></div>
    </div>

  </div>
</section>
""", unsafe_allow_html=True)

# ─── EXPERIENCE ──────────────────────────────────────────────────────────────
st.markdown("""
<section class="sec sec-alt">
  <p class="lbl">Career</p>
  <h2 class="stitle">Experience</h2>
  <p class="ssub">Five years of shipping production software across real estate, finance, and enterprise SaaS.</p>
  <div class="tl">

    <div class="tli">
      <div class="tld"></div>
      <p class="tlp">2023 — Present</p>
      <p class="tlr">Senior Laravel Developer</p>
      <p class="tlco">Enterprise Software Studio — Remote</p>
      <p class="tlde">Leading backend architecture for a multi-tenant real-estate ERP platform serving 30+ agencies. Introduced AI-assisted property valuation module using GPT-4o API, cutting manual appraisal time by 60%. Mentored a team of 4 junior developers; enforced TDD with PHPUnit &amp; Pest. Migrated monolith to service-oriented architecture on AWS — 99.9% uptime achieved.</p>
    </div>

    <div class="tli">
      <div class="tld"></div>
      <p class="tlp">2021 — 2023</p>
      <p class="tlr">Full-Stack Laravel Developer</p>
      <p class="tlco">PropTech Solutions Pvt. Ltd — Rawalpindi</p>
      <p class="tlde">Built a CRM system for real-estate brokerages from scratch: lead pipeline management, automated follow-up sequences, commission tracking, and contract generation via PDF APIs. Integrated WhatsApp Business API and Twilio SMS. Reduced lead response time from 4 hours to under 8 minutes with Laravel Queues.</p>
    </div>

    <div class="tli">
      <div class="tld"></div>
      <p class="tlp">2019 — 2021</p>
      <p class="tlr">Junior PHP Developer</p>
      <p class="tlco">WebCraft Agency — Islamabad</p>
      <p class="tlde">Developed and maintained custom Laravel applications for SME clients across retail, e-commerce, and hospitality verticals. Built reusable Blade component libraries and payment gateway integrations (Stripe, JazzCash). Gained solid foundations in RESTful API design and MySQL optimisation.</p>
    </div>

  </div>
</section>
""", unsafe_allow_html=True)

# ─── PROJECTS ────────────────────────────────────────────────────────────────
st.markdown("""
<section class="sec" id="projects">
  <p class="lbl">Work</p>
  <h2 class="stitle">Featured Projects</h2>
  <p class="ssub">Handpicked deliverables demonstrating depth across ERP, CRM, and AI-augmented products.</p>
  <div class="pg">

    <div class="pc">
      <div class="ph"><p class="pt">RealEstate360 ERP</p><span class="pty">ERP &middot; SaaS</span></div>
      <div class="pb">
        <p class="pd">Multi-tenant ERP for real-estate agencies covering inventory, sales pipeline, agent commissions, document management, and a GPT-4o-powered AI assistant for property queries and automated reporting.</p>
        <div class="ptags"><span class="tag">Laravel 11</span><span class="tag">Vue 3</span><span class="tag">Inertia</span><span class="tag">PostgreSQL</span><span class="tag">OpenAI API</span><span class="tag">AWS S3</span></div>
      </div>
    </div>

    <div class="pc">
      <div class="ph"><p class="pt">LeadFlow CRM</p><span class="pty">CRM &middot; Automation</span></div>
      <div class="pb">
        <p class="pd">End-to-end CRM for real-estate brokers: lead capture from 10+ portals, automated WhatsApp &amp; SMS drip campaigns, deal tracking, and AI-assisted follow-up suggestions.</p>
        <div class="ptags"><span class="tag">Laravel</span><span class="tag">Livewire</span><span class="tag">Redis</span><span class="tag">Twilio</span><span class="tag">WhatsApp API</span><span class="tag">Claude AI</span></div>
      </div>
    </div>

    <div class="pc">
      <div class="ph"><p class="pt">FinOps Tracker</p><span class="pty">Finance &middot; ERP</span></div>
      <div class="pb">
        <p class="pd">Accounting module with accounts payable/receivable, multi-currency support, bank reconciliation, automated VAT reporting, and exportable audit trails in PDF/Excel.</p>
        <div class="ptags"><span class="tag">Laravel</span><span class="tag">MySQL</span><span class="tag">Filament</span><span class="tag">Spatie</span><span class="tag">Laravel Excel</span><span class="tag">DomPDF</span></div>
      </div>
    </div>

    <div class="pc">
      <div class="ph"><p class="pt">DocuScan AI</p><span class="pty">AI &middot; Document OCR</span></div>
      <div class="pb">
        <p class="pd">Automated document intake using OCR + LLM pipeline to extract fields from title deeds, NOC certificates, and mortgage papers — pushing structured data into ERP with 94% accuracy.</p>
        <div class="ptags"><span class="tag">Python</span><span class="tag">FastAPI</span><span class="tag">Laravel API</span><span class="tag">Tesseract</span><span class="tag">GPT-4o Vision</span><span class="tag">Pinecone</span></div>
      </div>
    </div>

    <div class="pc">
      <div class="ph"><p class="pt">PropPortal Mobile API</p><span class="pty">API &middot; Mobile</span></div>
      <div class="pb">
        <p class="pd">Headless REST API for a Flutter property listing app: JWT auth, geolocation search, FCM push notifications, and real-time buyer-agent chat via WebSockets.</p>
        <div class="ptags"><span class="tag">Laravel Sanctum</span><span class="tag">WebSockets</span><span class="tag">FCM</span><span class="tag">Elasticsearch</span><span class="tag">Redis</span><span class="tag">Docker</span></div>
      </div>
    </div>

    <div class="pc">
      <div class="ph"><p class="pt">HR &amp; Payroll Module</p><span class="pty">ERP &middot; HR</span></div>
      <div class="pb">
        <p class="pd">HR module for a 500-employee group: biometric attendance sync, leave management, payroll with tax slabs, loan deductions, and self-service employee portal with role-based access.</p>
        <div class="ptags"><span class="tag">Laravel</span><span class="tag">Vue 3</span><span class="tag">Filament</span><span class="tag">Spatie Roles</span><span class="tag">Chart.js</span><span class="tag">MySQL</span></div>
      </div>
    </div>

  </div>
</section>
""", unsafe_allow_html=True)

# ─── TECH STACK ───────────────────────────────────────────────────────────────
st.markdown("""
<section class="sec sec-alt">
  <p class="lbl">Toolbox</p>
  <h2 class="stitle">Full Tech Stack</h2>
  <p class="ssub">Technologies I use day-to-day to deliver production-ready systems.</p>
  <div class="tg">
    <div class="tpill">&#128311; Laravel 10/11</div>
    <div class="tpill">&#128024; PHP 8.2</div>
    <div class="tpill">&#128154; Vue 3 + Pinia</div>
    <div class="tpill">&#9889; Inertia.js</div>
    <div class="tpill">&#127788; Tailwind CSS</div>
    <div class="tpill">&#128293; Livewire 3</div>
    <div class="tpill">&#127919; Filament 3</div>
    <div class="tpill">&#128451; MySQL 8</div>
    <div class="tpill">&#128024; PostgreSQL 16</div>
    <div class="tpill">&#128308; Redis</div>
    <div class="tpill">&#128269; Elasticsearch</div>
    <div class="tpill">&#128051; Docker</div>
    <div class="tpill">&#9729; AWS EC2 / S3</div>
    <div class="tpill">&#9881; GitHub Actions</div>
    <div class="tpill">&#129302; OpenAI GPT-4o</div>
    <div class="tpill">&#129504; Claude API</div>
    <div class="tpill">&#128205; Pinecone</div>
    <div class="tpill">&#128013; Python / FastAPI</div>
    <div class="tpill">&#128230; RabbitMQ</div>
    <div class="tpill">&#128172; Twilio / WA API</div>
    <div class="tpill">&#129514; Pest / PHPUnit</div>
    <div class="tpill">&#128221; Swagger / OpenAPI</div>
    <div class="tpill">&#128274; Laravel Sanctum</div>
    <div class="tpill">&#127760; Nginx</div>
  </div>
</section>
""", unsafe_allow_html=True)

# ─── CONTACT ─────────────────────────────────────────────────────────────────
st.markdown("""
<section class="sec">
  <p class="lbl">Contact</p>
  <h2 class="stitle">Let's Build Something</h2>
  <p class="ssub">Open to senior engineering roles, technical leadership, and freelance ERP/CRM projects.</p>
  <div class="cg">
    <div>
      <div class="ci"><span class="cie">&#128231;</span><div><p class="cil">Email</p><p class="civ">iftikhar.hshah@gmail.com</p></div></div>
      <div class="ci"><span class="cie">&#128188;</span><div><p class="cil">LinkedIn</p><p class="civ">linkedin.com/in/iftikhar-hussain-shah</p></div></div>
      <div class="ci"><span class="cie">&#128025;</span><div><p class="cil">GitHub</p><p class="civ">github.com/iftikhar-hshah</p></div></div>
      <div class="ci"><span class="cie">&#128205;</span><div><p class="cil">Location</p><p class="civ">Rawalpindi, Pakistan &middot; Open to Remote</p></div></div>
    </div>
    <div>
      <div class="term" style="margin-top:0;animation:none;opacity:1;">
        <div class="tb">
          <div><span class="tp">$ </span><span class="tc">cat availability.txt</span></div>
          <div class="to" style="margin-top:.35rem;">
            Status &nbsp;&nbsp;&nbsp;: &#10003; Available<br>
            Notice &nbsp;&nbsp;&nbsp;: Immediate<br>
            Preferred : Remote / Hybrid<br>
            Timezone &nbsp;: PKT (UTC+5)<br>
            Rate &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: Negotiable
          </div>
          <div style="margin-top:.7rem;"><span class="tp">$ </span><span class="tc">cat specialisations.txt</span></div>
          <div class="to" style="margin-top:.35rem;">
            &#10004; ERP &amp; CRM Architecture<br>
            &#10004; Real Estate Tech Platforms<br>
            &#10004; AI/LLM Feature Integration<br>
            &#10004; API Design &amp; Microservices<br>
            &#10004; Team Lead &amp; Code Review
          </div>
          <div style="margin-top:.7rem;"><span class="tp">$ </span><span class="cur"></span></div>
        </div>
      </div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ─── FOOTER ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ft">
  Crafted with <span>&#9889;</span> by Iftikhar Hussain Shah &nbsp;&middot;&nbsp; 2025
  &nbsp;&middot;&nbsp; Built with <span>Streamlit + Laravel spirit</span>
</div>
""", unsafe_allow_html=True)