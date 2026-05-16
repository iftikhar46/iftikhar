import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Iftikhar Hussain Shah | Senior Laravel Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome only
st.markdown("""
<style>
[data-testid="stHeader"], [data-testid="stToolbar"],
[data-testid="stSidebarCollapsedControl"],
footer, #MainMenu { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
body, [data-testid="stAppViewContainer"],
[data-testid="stMain"] { background: #050a0e !important; }
</style>
""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:ital,wght@0,400;0,500;1,400&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{background:#050a0e;color:#e8f4f0;font-family:'DM Mono',monospace;overflow-x:hidden;}
::-webkit-scrollbar{width:4px;}
::-webkit-scrollbar-track{background:#050a0e;}
::-webkit-scrollbar-thumb{background:#00e5a0;border-radius:2px;}

@keyframes fadeUp  {from{opacity:0;transform:translateY(40px);}to{opacity:1;transform:translateY(0);}}
@keyframes fadeIn  {from{opacity:0;}to{opacity:1;}}
@keyframes pulse   {0%,100%{box-shadow:0 0 0 0 rgba(0,229,160,.4);}70%{box-shadow:0 0 0 14px rgba(0,229,160,0);}}
@keyframes scanline{0%{transform:translateY(-200%);}100%{transform:translateY(200vh);}}
@keyframes blink   {0%,100%{opacity:1;}50%{opacity:0;}}
@keyframes float   {0%,100%{transform:translateY(0);}50%{transform:translateY(-14px);}}
@keyframes shimmer {0%{background-position:-200% center;}100%{background-position:200% center;}}
@keyframes glow    {0%,100%{text-shadow:0 0 20px rgba(0,229,160,.3);}50%{text-shadow:0 0 40px rgba(0,229,160,.8),0 0 80px rgba(0,229,160,.4);}}
@keyframes progFill{from{width:0;}to{width:var(--w);}}
@keyframes cardIn  {from{opacity:0;transform:translateY(28px);}to{opacity:1;transform:translateY(0);}}
@keyframes borderA {0%,100%{border-color:rgba(0,229,160,.4);}50%{border-color:rgba(0,184,217,.5);}}

body::before{content:'';position:fixed;inset:0;pointer-events:none;z-index:0;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
  background-size:200px;opacity:.4;}
body::after{content:'';position:fixed;left:0;top:-100%;width:100%;height:2px;
  background:linear-gradient(transparent,rgba(0,229,160,.06),transparent);
  pointer-events:none;z-index:1;animation:scanline 10s linear infinite;}

/* HERO */
.hero{min-height:100vh;display:flex;flex-direction:column;justify-content:center;
  align-items:flex-start;padding:6rem 6vw 4rem;position:relative;overflow:hidden;
  background:radial-gradient(ellipse 80% 60% at 70% 50%,rgba(0,229,160,.07) 0%,transparent 60%),
             radial-gradient(ellipse 40% 40% at 20% 80%,rgba(0,184,217,.05) 0%,transparent 50%),#050a0e;}
.hero-grid{position:absolute;right:5vw;top:50%;transform:translateY(-50%);
  width:clamp(240px,32vw,400px);height:clamp(240px,32vw,400px);
  opacity:.13;animation:float 7s ease-in-out infinite,fadeIn 1.2s .8s ease both;}
.status-badge{display:inline-flex;align-items:center;gap:.5rem;padding:.4rem 1rem;
  border-radius:20px;background:rgba(0,229,160,.08);border:1px solid rgba(0,229,160,.22);
  font-size:.72rem;color:#00e5a0;margin-bottom:1.5rem;
  animation:fadeIn 1s .2s ease both;opacity:0;animation-fill-mode:forwards;}
.status-dot{width:8px;height:8px;border-radius:50%;background:#00e5a0;
  display:inline-block;animation:pulse 1.5s infinite;flex-shrink:0;}
.hero-eyebrow{font-size:.75rem;letter-spacing:.25em;text-transform:uppercase;color:#00e5a0;
  animation:fadeUp .6s .3s ease both;opacity:0;animation-fill-mode:forwards;
  display:flex;align-items:center;gap:.75rem;margin-bottom:.6rem;}
.hero-eyebrow::before{content:'';display:inline-block;width:32px;height:1px;background:#00e5a0;}
.hero-name{font-family:'Syne',sans-serif;font-size:clamp(2.8rem,9vw,7.5rem);
  font-weight:800;line-height:.95;color:#e8f4f0;
  animation:fadeUp .7s .45s ease both;opacity:0;animation-fill-mode:forwards;margin-bottom:.5rem;}
.hero-name span{background:linear-gradient(135deg,#00e5a0 0%,#00b8d9 50%,#00e5a0 100%);
  background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;animation:shimmer 3s linear infinite;}
.hero-title{font-family:'Instrument Serif',serif;font-style:italic;
  font-size:clamp(.95rem,2.2vw,1.45rem);color:rgba(232,244,240,.55);margin-bottom:1.75rem;
  animation:fadeUp .7s .6s ease both;opacity:0;animation-fill-mode:forwards;}
.hero-desc{max-width:52ch;font-size:.87rem;line-height:1.9;color:rgba(232,244,240,.58);
  border-left:2px solid rgba(0,229,160,.3);padding-left:1.25rem;margin-bottom:2.25rem;
  animation:fadeUp .7s .75s ease both;opacity:0;animation-fill-mode:forwards;}
.hero-cta{display:flex;gap:1rem;flex-wrap:wrap;
  animation:fadeUp .7s .9s ease both;opacity:0;animation-fill-mode:forwards;}
.btn-p{font-family:'DM Mono',monospace;font-size:.77rem;letter-spacing:.12em;
  text-transform:uppercase;padding:.85rem 2rem;background:#00e5a0;color:#050a0e;
  border:none;border-radius:2px;cursor:pointer;font-weight:600;
  transition:transform .2s,box-shadow .2s;animation:pulse 2.5s infinite;
  text-decoration:none;display:inline-block;}
.btn-p:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(0,229,160,.4);}
.btn-s{font-family:'DM Mono',monospace;font-size:.77rem;letter-spacing:.12em;
  text-transform:uppercase;padding:.85rem 2rem;background:transparent;color:#00e5a0;
  border:1px solid rgba(0,229,160,.4);border-radius:2px;cursor:pointer;
  transition:transform .2s,border-color .2s,box-shadow .2s;
  text-decoration:none;display:inline-block;animation:borderA 3s ease infinite;}
.btn-s:hover{transform:translateY(-3px);border-color:#00e5a0;box-shadow:0 12px 30px rgba(0,229,160,.15);}

/* Terminal */
.terminal{font-family:'DM Mono',monospace;font-size:.77rem;line-height:1.9;
  background:rgba(0,0,0,.55);border:1px solid rgba(0,229,160,.15);border-radius:4px;
  padding:1.5rem;margin-top:2.5rem;position:relative;
  animation:fadeUp .7s 1.1s ease both;opacity:0;animation-fill-mode:forwards;}
.terminal::before{content:'● ● ●';position:absolute;top:.55rem;left:1rem;
  font-size:.6rem;color:rgba(232,244,240,.2);letter-spacing:.3rem;}
.terminal-body{margin-top:.5rem;}
.tp{color:rgba(0,229,160,.7);}
.tc{color:#e8f4f0;}
.to{color:rgba(232,244,240,.42);}
.cursor{display:inline-block;width:8px;height:13px;background:#00e5a0;
  vertical-align:text-bottom;animation:blink 1s step-end infinite;}

/* STATS */
.stats-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));
  gap:1px;background:rgba(0,229,160,.1);
  border-top:1px solid rgba(0,229,160,.1);border-bottom:1px solid rgba(0,229,160,.1);}
.stat-cell{padding:2.4rem 1.5rem;background:#050a0e;text-align:center;transition:background .3s;}
.stat-cell:hover{background:rgba(0,229,160,.05);}
.sn{font-family:'Syne',sans-serif;font-size:2.7rem;font-weight:800;color:#00e5a0;
  display:block;animation:glow 3s ease infinite;}
.sl{font-size:.67rem;letter-spacing:.15em;text-transform:uppercase;
  color:rgba(232,244,240,.4);margin-top:.4rem;display:block;}

/* SECTION */
.section{padding:5.5rem 6vw;position:relative;}
.section-alt{background:rgba(0,229,160,.018);
  border-top:1px solid rgba(0,229,160,.07);border-bottom:1px solid rgba(0,229,160,.07);}
.sec-label{font-size:.7rem;letter-spacing:.3em;text-transform:uppercase;color:#00e5a0;
  margin-bottom:.6rem;display:flex;align-items:center;gap:.75rem;}
.sec-label::after{content:'';flex:1;height:1px;
  background:linear-gradient(to right,rgba(0,229,160,.3),transparent);max-width:200px;}
.sec-title{font-family:'Syne',sans-serif;font-size:clamp(1.7rem,4vw,2.9rem);
  font-weight:700;color:#e8f4f0;margin-bottom:.4rem;line-height:1.1;}
.sec-sub{color:rgba(232,244,240,.42);font-size:.84rem;margin-bottom:2.8rem;max-width:52ch;}

/* SKILLS */
.skills-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.4rem;}
.skill-card{border:1px solid rgba(0,229,160,.12);padding:1.9rem;border-radius:4px;
  background:rgba(255,255,255,.012);transition:transform .3s,border-color .3s,box-shadow .3s;
  position:relative;overflow:hidden;animation:cardIn .6s ease both;}
.skill-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent,#00e5a0,transparent);
  transform:translateX(-100%);transition:transform .45s;}
.skill-card:hover{transform:translateY(-6px);border-color:rgba(0,229,160,.35);
  box-shadow:0 20px 50px rgba(0,229,160,.08);}
.skill-card:hover::before{transform:translateX(100%);}
.skill-card:nth-child(1){animation-delay:.05s;}
.skill-card:nth-child(2){animation-delay:.12s;}
.skill-card:nth-child(3){animation-delay:.19s;}
.skill-card:nth-child(4){animation-delay:.26s;}
.skill-card:nth-child(5){animation-delay:.33s;}
.skill-card:nth-child(6){animation-delay:.40s;}
.sk-icon{font-size:1.7rem;margin-bottom:.9rem;display:block;}
.sk-name{font-family:'Syne',sans-serif;font-size:1rem;font-weight:700;color:#e8f4f0;margin-bottom:.4rem;}
.sk-desc{font-size:.77rem;line-height:1.75;color:rgba(232,244,240,.44);margin-bottom:1rem;}
.pr-row{margin:.7rem 0;}
.pr-label{display:flex;justify-content:space-between;font-size:.71rem;color:rgba(232,244,240,.5);margin-bottom:.32rem;}
.pr-track{height:3px;background:rgba(255,255,255,.07);border-radius:2px;overflow:hidden;}
.pr-fill{height:100%;border-radius:2px;background:linear-gradient(90deg,#00e5a0,#00b8d9);
  animation:progFill 1.4s cubic-bezier(.22,1,.36,1) both;}

/* TIMELINE */
.timeline{position:relative;padding-left:2rem;}
.timeline::before{content:'';position:absolute;left:0;top:0;bottom:0;width:1px;
  background:linear-gradient(to bottom,#00e5a0,rgba(0,229,160,.08));}
.tl-item{position:relative;margin-bottom:2.8rem;animation:cardIn .6s ease both;}
.tl-item:nth-child(1){animation-delay:.05s;}
.tl-item:nth-child(2){animation-delay:.18s;}
.tl-item:nth-child(3){animation-delay:.31s;}
.tl-dot{position:absolute;left:-2.38rem;top:.3rem;width:10px;height:10px;
  border-radius:50%;background:#00e5a0;border:2px solid #050a0e;
  box-shadow:0 0 0 3px rgba(0,229,160,.22);}
.tl-period{font-size:.67rem;letter-spacing:.15em;text-transform:uppercase;color:#00e5a0;margin-bottom:.28rem;}
.tl-role{font-family:'Syne',sans-serif;font-size:1.08rem;font-weight:700;color:#e8f4f0;margin-bottom:.18rem;}
.tl-co{font-size:.77rem;color:rgba(232,244,240,.42);margin-bottom:.65rem;}
.tl-desc{font-size:.79rem;line-height:1.85;color:rgba(232,244,240,.52);}

/* PROJECTS */
.projects-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.4rem;}
.proj-card{border:1px solid rgba(0,229,160,.1);border-radius:4px;overflow:hidden;
  background:rgba(255,255,255,.01);transition:transform .3s,box-shadow .3s;
  animation:cardIn .6s ease both;}
.proj-card:hover{transform:translateY(-8px);box-shadow:0 28px 56px rgba(0,229,160,.1);}
.proj-card:nth-child(1){animation-delay:.05s;}
.proj-card:nth-child(2){animation-delay:.15s;}
.proj-card:nth-child(3){animation-delay:.25s;}
.proj-card:nth-child(4){animation-delay:.35s;}
.proj-card:nth-child(5){animation-delay:.45s;}
.proj-card:nth-child(6){animation-delay:.55s;}
.proj-head{padding:1.65rem;border-bottom:1px solid rgba(0,229,160,.07);
  background:rgba(0,229,160,.03);display:flex;justify-content:space-between;
  align-items:flex-start;gap:1rem;}
.proj-title{font-family:'Syne',sans-serif;font-size:1.02rem;font-weight:700;color:#e8f4f0;}
.proj-type{font-size:.61rem;letter-spacing:.12em;text-transform:uppercase;color:#00e5a0;
  padding:.26rem .6rem;border:1px solid rgba(0,229,160,.3);border-radius:2px;
  white-space:nowrap;flex-shrink:0;}
.proj-body{padding:1.5rem;}
.proj-desc{font-size:.79rem;line-height:1.8;color:rgba(232,244,240,.48);margin-bottom:1.05rem;}
.proj-tags{display:flex;flex-wrap:wrap;gap:.42rem;}
.tag{font-size:.61rem;letter-spacing:.08em;text-transform:uppercase;padding:.2rem .55rem;
  background:rgba(0,229,160,.07);border:1px solid rgba(0,229,160,.15);
  border-radius:2px;color:rgba(0,229,160,.8);}

/* TECH */
.tech-grid{display:flex;flex-wrap:wrap;gap:.9rem;}
.tech-pill{display:flex;align-items:center;gap:.45rem;padding:.5rem 1rem;
  border:1px solid rgba(0,229,160,.14);border-radius:2px;background:rgba(0,229,160,.033);
  font-size:.75rem;color:rgba(232,244,240,.68);
  transition:transform .2s,border-color .2s,color .2s;}
.tech-pill:hover{transform:translateY(-3px);border-color:rgba(0,229,160,.4);color:#00e5a0;}

/* CONTACT */
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:3rem;}
@media(max-width:680px){.contact-grid{grid-template-columns:1fr;}}
.c-item{display:flex;align-items:flex-start;gap:1.1rem;padding:1.3rem;
  border:1px solid rgba(0,229,160,.1);border-radius:4px;margin-bottom:.9rem;
  transition:border-color .3s;}
.c-item:hover{border-color:rgba(0,229,160,.35);}
.c-icon{font-size:1.25rem;flex-shrink:0;margin-top:.1rem;}
.c-label{font-size:.64rem;letter-spacing:.2em;text-transform:uppercase;color:#00e5a0;margin-bottom:.18rem;}
.c-value{font-size:.8rem;color:rgba(232,244,240,.65);word-break:break-all;}

/* FOOTER */
.footer{padding:1.8rem 6vw;text-align:center;border-top:1px solid rgba(0,229,160,.07);
  font-size:.68rem;color:rgba(232,244,240,.22);letter-spacing:.1em;}
.footer span{color:rgba(0,229,160,.55);}

@media(max-width:600px){.hero{padding:5rem 5vw 3rem;}.section{padding:4rem 5vw;}.hero-grid{display:none;}}
</style>
</head>
<body>

<!-- HERO -->
<section class="hero">
  <svg class="hero-grid" viewBox="0 0 400 400" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="200" cy="200" r="180" stroke="#00e5a0" stroke-width=".5" stroke-dasharray="4 8"/>
    <circle cx="200" cy="200" r="140" stroke="#00b8d9" stroke-width=".5" stroke-dasharray="2 6"/>
    <circle cx="200" cy="200" r="100" stroke="#00e5a0" stroke-width=".5" stroke-dasharray="1 4"/>
    <circle cx="200" cy="200" r="60"  stroke="#00b8d9" stroke-width=".4" stroke-dasharray="2 5"/>
    <line x1="20" y1="200" x2="380" y2="200" stroke="#00e5a0" stroke-width=".3"/>
    <line x1="200" y1="20" x2="200" y2="380" stroke="#00e5a0" stroke-width=".3"/>
    <rect x="150" y="150" width="100" height="100" stroke="#00b8d9" stroke-width=".4" stroke-dasharray="3 5"/>
    <circle cx="200" cy="200" r="10" fill="#00e5a0" opacity=".7"/>
    <circle cx="200" cy="60"  r="4" fill="#00b8d9" opacity=".5"/>
    <circle cx="340" cy="200" r="4" fill="#00e5a0" opacity=".5"/>
    <circle cx="200" cy="340" r="4" fill="#00b8d9" opacity=".5"/>
    <circle cx="60"  cy="200" r="4" fill="#00e5a0" opacity=".5"/>
  </svg>

  <div class="status-badge">
    <span class="status-dot"></span>&nbsp;Available for new opportunities
  </div>
  <p class="hero-eyebrow">Senior Full-Stack Engineer</p>
  <h1 class="hero-name">Iftikhar<br><span>Hussain Shah</span></h1>
  <p class="hero-title">5 Years &middot; Laravel PHP &middot; ERP &amp; CRM Systems &middot; AI-Augmented Development</p>
  <p class="hero-desc">I build robust enterprise-grade web systems &mdash; from real-estate ERP platforms to AI-integrated CRM solutions. Specialising in Laravel ecosystems, RESTful architecture, and modern DevOps pipelines that scale.</p>
  <div class="hero-cta">
    <a class="btn-p" href="mailto:iftikhar.hshah@gmail.com">Get in Touch &nearr;</a>
    <a class="btn-s" href="#projects">View Projects &rarr;</a>
  </div>
  <div class="terminal" style="max-width:480px;">
    <div class="terminal-body">
      <div><span class="tp">~/portfolio $</span> <span class="tc">whoami</span></div>
      <div class="to">Iftikhar Hussain Shah &mdash; Backend Architect &amp; API Specialist</div>
      <div style="margin-top:.4rem"><span class="tp">~/portfolio $</span> <span class="tc">skills --top 3</span></div>
      <div class="to">Laravel &nbsp;&bull;&nbsp; Vue.js &nbsp;&bull;&nbsp; AI/LLM Integration</div>
      <div style="margin-top:.4rem"><span class="tp">~/portfolio $</span> <span class="tc">status</span></div>
      <div class="to">&#9889; Open to senior / lead roles &nbsp;<span class="cursor"></span></div>
    </div>
  </div>
</section>

<!-- STATS -->
<div class="stats-row">
  <div class="stat-cell"><span class="sn">5+</span><span class="sl">Years Experience</span></div>
  <div class="stat-cell"><span class="sn">30+</span><span class="sl">Projects Delivered</span></div>
  <div class="stat-cell"><span class="sn">12+</span><span class="sl">ERP/CRM Modules</span></div>
  <div class="stat-cell"><span class="sn">4</span><span class="sl">Industry Sectors</span></div>
  <div class="stat-cell"><span class="sn">99%</span><span class="sl">Client Satisfaction</span></div>
</div>

<!-- SKILLS -->
<section class="section">
  <p class="sec-label">Expertise</p>
  <h2 class="sec-title">Core Competencies</h2>
  <p class="sec-sub">A full-stack practitioner with a back-end-first mindset, deeply versed in enterprise architecture patterns.</p>
  <div class="skills-grid">

    <div class="skill-card">
      <span class="sk-icon">&#128311;</span>
      <p class="sk-name">Laravel &amp; PHP Ecosystem</p>
      <p class="sk-desc">Expert-level Laravel 10/11 &mdash; Eloquent ORM, Queues, Events, Sanctum/Passport auth, Livewire, Filament admin panels. PSR-12 clean code advocate.</p>
      <div class="pr-row"><div class="pr-label"><span>Laravel</span><span>97%</span></div><div class="pr-track"><div class="pr-fill" style="--w:97%"></div></div></div>
      <div class="pr-row"><div class="pr-label"><span>PHP 8.x</span><span>93%</span></div><div class="pr-track"><div class="pr-fill" style="--w:93%"></div></div></div>
      <div class="pr-row"><div class="pr-label"><span>Livewire / Filament</span><span>88%</span></div><div class="pr-track"><div class="pr-fill" style="--w:88%"></div></div></div>
    </div>

    <div class="skill-card">
      <span class="sk-icon">&#128451;</span>
      <p class="sk-name">Database Architecture</p>
      <p class="sk-desc">High-performance relational schemas for ERP/CRM. MySQL, PostgreSQL, Redis caching, query optimisation, and full-text search at scale.</p>
      <div class="pr-row"><div class="pr-label"><span>MySQL / PostgreSQL</span><span>92%</span></div><div class="pr-track"><div class="pr-fill" style="--w:92%"></div></div></div>
      <div class="pr-row"><div class="pr-label"><span>Redis</span><span>83%</span></div><div class="pr-track"><div class="pr-fill" style="--w:83%"></div></div></div>
      <div class="pr-row"><div class="pr-label"><span>Query Optimisation</span><span>90%</span></div><div class="pr-track"><div class="pr-fill" style="--w:90%"></div></div></div>
    </div>

    <div class="skill-card">
      <span class="sk-icon">&#129302;</span>
      <p class="sk-name">AI &amp; LLM Integration</p>
      <p class="sk-desc">Integrating OpenAI GPT-4o &amp; Claude API into ERP workflows &mdash; AI-assisted data entry, smart search, document summarisation, and chatbots.</p>
      <div class="pr-row"><div class="pr-label"><span>OpenAI / Claude APIs</span><span>85%</span></div><div class="pr-track"><div class="pr-fill" style="--w:85%"></div></div></div>
      <div class="pr-row"><div class="pr-label"><span>Prompt Engineering</span><span>80%</span></div><div class="pr-track"><div class="pr-fill" style="--w:80%"></div></div></div>
      <div class="pr-row"><div class="pr-label"><span>RAG / Vector DBs</span><span>70%</span></div><div class="pr-track"><div class="pr-fill" style="--w:70%"></div></div></div>
    </div>

    <div class="skill-card">
      <span class="sk-icon">&#9881;&#65039;</span>
      <p class="sk-name">API Design &amp; Microservices</p>
      <p class="sk-desc">RESTful and GraphQL API design. Microservice decomposition, inter-service messaging with RabbitMQ/Kafka, and OpenAPI 3.x documentation.</p>
      <div class="pr-row"><div class="pr-label"><span>REST API</span><span>95%</span></div><div class="pr-track"><div class="pr-fill" style="--w:95%"></div></div></div>
      <div class="pr-row"><div class="pr-label"><span>GraphQL</span><span>72%</span></div><div class="pr-track"><div class="pr-fill" style="--w:72%"></div></div></div>
      <div class="pr-row"><div class="pr-label"><span>RabbitMQ / Kafka</span><span>68%</span></div><div class="pr-track"><div class="pr-fill" style="--w:68%"></div></div></div>
    </div>

    <div class="skill-card">
      <span class="sk-icon">&#128187;</span>
      <p class="sk-name">Frontend &mdash; Vue &amp; Inertia</p>
      <p class="sk-desc">Vue 3 + Pinia + Vite for reactive SPA dashboards. Inertia.js for seamless Laravel-Vue workflows. Tailwind CSS, Chart.js visualisations.</p>
      <div class="pr-row"><div class="pr-label"><span>Vue 3</span><span>82%</span></div><div class="pr-track"><div class="pr-fill" style="--w:82%"></div></div></div>
      <div class="pr-row"><div class="pr-label"><span>Inertia.js</span><span>85%</span></div><div class="pr-track"><div class="pr-fill" style="--w:85%"></div></div></div>
      <div class="pr-row"><div class="pr-label"><span>Tailwind CSS</span><span>88%</span></div><div class="pr-track"><div class="pr-fill" style="--w:88%"></div></div></div>
    </div>

    <div class="skill-card">
      <span class="sk-icon">&#128640;</span>
      <p class="sk-name">DevOps &amp; Cloud</p>
      <p class="sk-desc">CI/CD with GitHub Actions. Docker / Docker Compose. AWS EC2, S3, RDS deployments. Forge, Envoyer, and Nginx server management.</p>
      <div class="pr-row"><div class="pr-label"><span>Docker</span><span>80%</span></div><div class="pr-track"><div class="pr-fill" style="--w:80%"></div></div></div>
      <div class="pr-row"><div class="pr-label"><span>AWS</span><span>74%</span></div><div class="pr-track"><div class="pr-fill" style="--w:74%"></div></div></div>
      <div class="pr-row"><div class="pr-label"><span>CI/CD</span><span>82%</span></div><div class="pr-track"><div class="pr-fill" style="--w:82%"></div></div></div>
    </div>

  </div>
</section>

<!-- EXPERIENCE -->
<section class="section section-alt">
  <p class="sec-label">Career</p>
  <h2 class="sec-title">Experience</h2>
  <p class="sec-sub">Five years of shipping production software across real estate, finance, and enterprise SaaS.</p>
  <div class="timeline">

    <div class="tl-item">
      <div class="tl-dot"></div>
      <p class="tl-period">2023 &mdash; Present</p>
      <p class="tl-role">Senior Laravel Developer</p>
      <p class="tl-co">Enterprise Software Studio &mdash; Remote</p>
      <p class="tl-desc">Leading backend architecture for a multi-tenant real-estate ERP platform serving 30+ agencies. Introduced AI-assisted property valuation module using GPT-4o API, cutting manual appraisal time by 60%. Mentored a team of 4 junior developers; enforced TDD with PHPUnit &amp; Pest. Migrated monolith to service-oriented architecture on AWS &mdash; 99.9% uptime achieved.</p>
    </div>

    <div class="tl-item">
      <div class="tl-dot"></div>
      <p class="tl-period">2021 &mdash; 2023</p>
      <p class="tl-role">Full-Stack Laravel Developer</p>
      <p class="tl-co">PropTech Solutions Pvt. Ltd &mdash; Rawalpindi</p>
      <p class="tl-desc">Built a CRM system for real-estate brokerages from scratch: lead pipeline management, automated follow-up sequences, commission tracking, and contract generation via PDF APIs. Integrated WhatsApp Business API and Twilio SMS for automated client communication. Reduced lead response time from 4 hours to under 8 minutes with Laravel Queues.</p>
    </div>

    <div class="tl-item">
      <div class="tl-dot"></div>
      <p class="tl-period">2019 &mdash; 2021</p>
      <p class="tl-role">Junior PHP Developer</p>
      <p class="tl-co">WebCraft Agency &mdash; Islamabad</p>
      <p class="tl-desc">Developed and maintained custom Laravel applications for SME clients across retail, e-commerce, and hospitality verticals. Built reusable Blade component libraries and payment gateway integrations (Stripe, JazzCash). Gained solid foundations in RESTful API design and MySQL optimisation.</p>
    </div>

  </div>
</section>

<!-- PROJECTS -->
<section class="section" id="projects">
  <p class="sec-label">Work</p>
  <h2 class="sec-title">Featured Projects</h2>
  <p class="sec-sub">Handpicked deliverables demonstrating depth across ERP, CRM, and AI-augmented products.</p>
  <div class="projects-grid">

    <div class="proj-card">
      <div class="proj-head"><p class="proj-title">RealEstate360 ERP</p><span class="proj-type">ERP &middot; SaaS</span></div>
      <div class="proj-body">
        <p class="proj-desc">Multi-tenant ERP for real-estate agencies covering inventory, sales pipeline, agent commissions, document management, and a GPT-4o-powered AI assistant for property queries and report generation.</p>
        <div class="proj-tags"><span class="tag">Laravel 11</span><span class="tag">Vue 3</span><span class="tag">Inertia</span><span class="tag">PostgreSQL</span><span class="tag">OpenAI API</span><span class="tag">AWS S3</span></div>
      </div>
    </div>

    <div class="proj-card">
      <div class="proj-head"><p class="proj-title">LeadFlow CRM</p><span class="proj-type">CRM &middot; Automation</span></div>
      <div class="proj-body">
        <p class="proj-desc">End-to-end CRM for real-estate brokers: lead capture from 10+ portals, automated WhatsApp &amp; SMS drip campaigns, deal tracking, and AI-assisted follow-up suggestion engine.</p>
        <div class="proj-tags"><span class="tag">Laravel</span><span class="tag">Livewire</span><span class="tag">Redis</span><span class="tag">Twilio</span><span class="tag">WhatsApp API</span><span class="tag">Claude AI</span></div>
      </div>
    </div>

    <div class="proj-card">
      <div class="proj-head"><p class="proj-title">FinOps Tracker</p><span class="proj-type">Finance &middot; ERP</span></div>
      <div class="proj-body">
        <p class="proj-desc">Accounting module with accounts payable/receivable, multi-currency support, bank reconciliation, automated VAT reporting, and exportable audit trails in PDF/Excel.</p>
        <div class="proj-tags"><span class="tag">Laravel</span><span class="tag">MySQL</span><span class="tag">Filament</span><span class="tag">Spatie</span><span class="tag">Laravel Excel</span><span class="tag">DomPDF</span></div>
      </div>
    </div>

    <div class="proj-card">
      <div class="proj-head"><p class="proj-title">DocuScan AI</p><span class="proj-type">AI &middot; Document OCR</span></div>
      <div class="proj-body">
        <p class="proj-desc">Automated document intake using OCR + LLM pipeline to extract fields from title deeds, NOC certificates, and mortgage papers &mdash; pushing structured data into ERP with 94% accuracy.</p>
        <div class="proj-tags"><span class="tag">Python</span><span class="tag">FastAPI</span><span class="tag">Laravel API</span><span class="tag">Tesseract</span><span class="tag">GPT-4o Vision</span><span class="tag">Pinecone</span></div>
      </div>
    </div>

    <div class="proj-card">
      <div class="proj-head"><p class="proj-title">PropPortal Mobile API</p><span class="proj-type">API &middot; Mobile Backend</span></div>
      <div class="proj-body">
        <p class="proj-desc">Headless REST API for a cross-platform property listing app: JWT auth, geolocation search, FCM push notifications, and real-time buyer-agent chat via WebSockets.</p>
        <div class="proj-tags"><span class="tag">Laravel Sanctum</span><span class="tag">WebSockets</span><span class="tag">FCM</span><span class="tag">Elasticsearch</span><span class="tag">Redis</span><span class="tag">Docker</span></div>
      </div>
    </div>

    <div class="proj-card">
      <div class="proj-head"><p class="proj-title">HR &amp; Payroll Module</p><span class="proj-type">ERP &middot; HR</span></div>
      <div class="proj-body">
        <p class="proj-desc">HR module for a 500-employee group: biometric attendance sync, leave management, payroll with tax slabs, loan deductions, and a self-service employee portal with role-based access.</p>
        <div class="proj-tags"><span class="tag">Laravel</span><span class="tag">Vue 3</span><span class="tag">Filament</span><span class="tag">Spatie Roles</span><span class="tag">Chart.js</span><span class="tag">MySQL</span></div>
      </div>
    </div>

  </div>
</section>

<!-- TECH STACK -->
<section class="section section-alt">
  <p class="sec-label">Toolbox</p>
  <h2 class="sec-title">Full Tech Stack</h2>
  <p class="sec-sub">Technologies I use day-to-day to deliver production-ready systems.</p>
  <div class="tech-grid">
    <div class="tech-pill"><span>&#128311;</span> Laravel 10/11</div>
    <div class="tech-pill"><span>&#128024;</span> PHP 8.2</div>
    <div class="tech-pill"><span>&#128154;</span> Vue 3 + Pinia</div>
    <div class="tech-pill"><span>&#9889;</span> Inertia.js</div>
    <div class="tech-pill"><span>&#127788;&#65039;</span> Tailwind CSS</div>
    <div class="tech-pill"><span>&#128293;</span> Livewire 3</div>
    <div class="tech-pill"><span>&#127919;</span> Filament 3</div>
    <div class="tech-pill"><span>&#128451;&#65039;</span> MySQL 8</div>
    <div class="tech-pill"><span>&#128024;</span> PostgreSQL 16</div>
    <div class="tech-pill"><span>&#128308;</span> Redis</div>
    <div class="tech-pill"><span>&#128269;</span> Elasticsearch</div>
    <div class="tech-pill"><span>&#128051;</span> Docker</div>
    <div class="tech-pill"><span>&#9729;&#65039;</span> AWS EC2 / S3</div>
    <div class="tech-pill"><span>&#9881;&#65039;</span> GitHub Actions</div>
    <div class="tech-pill"><span>&#129302;</span> OpenAI GPT-4o</div>
    <div class="tech-pill"><span>&#129504;</span> Claude API</div>
    <div class="tech-pill"><span>&#128205;</span> Pinecone</div>
    <div class="tech-pill"><span>&#128013;</span> Python / FastAPI</div>
    <div class="tech-pill"><span>&#128230;</span> RabbitMQ</div>
    <div class="tech-pill"><span>&#128172;</span> Twilio / WA API</div>
    <div class="tech-pill"><span>&#129514;</span> Pest / PHPUnit</div>
    <div class="tech-pill"><span>&#128221;</span> Swagger / OpenAPI</div>
    <div class="tech-pill"><span>&#128274;</span> Laravel Sanctum</div>
    <div class="tech-pill"><span>&#127760;</span> Nginx</div>
  </div>
</section>

<!-- CONTACT -->
<section class="section">
  <p class="sec-label">Contact</p>
  <h2 class="sec-title">Let's Build Something</h2>
  <p class="sec-sub">Open to senior engineering roles, technical leadership, and freelance ERP/CRM projects.</p>
  <div class="contact-grid">
    <div>
      <div class="c-item">
        <span class="c-icon">&#128231;</span>
        <div><p class="c-label">Email</p><p class="c-value">iftikhar.hshah@gmail.com</p></div>
      </div>
      <div class="c-item">
        <span class="c-icon">&#128188;</span>
        <div><p class="c-label">LinkedIn</p><p class="c-value">linkedin.com/in/iftikhar-hussain-shah</p></div>
      </div>
      <div class="c-item">
        <span class="c-icon">&#128025;</span>
        <div><p class="c-label">GitHub</p><p class="c-value">github.com/iftikhar-hshah</p></div>
      </div>
      <div class="c-item">
        <span class="c-icon">&#128205;</span>
        <div><p class="c-label">Location</p><p class="c-value">Rawalpindi, Pakistan &middot; Open to Remote</p></div>
      </div>
    </div>
    <div>
      <div class="terminal" style="margin-top:0;animation:none;opacity:1;">
        <div class="terminal-body">
          <div><span class="tp">$ </span><span class="tc">cat availability.txt</span></div>
          <div class="to" style="margin-top:.4rem;">
            Status &nbsp;&nbsp;&nbsp;: &#10003; Available<br>
            Notice &nbsp;&nbsp;&nbsp;: Immediate<br>
            Preferred : Remote / Hybrid<br>
            Timezone &nbsp;: PKT (UTC+5)<br>
            Rate &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: Negotiable
          </div>
          <div style="margin-top:.8rem;"><span class="tp">$ </span><span class="tc">cat specialisations.txt</span></div>
          <div class="to" style="margin-top:.4rem;">
            &#10004; ERP &amp; CRM Architecture<br>
            &#10004; Real Estate Tech Platforms<br>
            &#10004; AI/LLM Feature Integration<br>
            &#10004; API Design &amp; Microservices<br>
            &#10004; Team Lead &amp; Code Review
          </div>
          <div style="margin-top:.8rem;"><span class="tp">$ </span><span class="cursor"></span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<div class="footer">
  Crafted with <span>&#9889;</span> by Iftikhar Hussain Shah &nbsp;&middot;&nbsp; 2025
  &nbsp;&middot;&nbsp; Built with <span>Streamlit + Laravel spirit</span>
</div>

</body>
</html>"""

components.html(HTML, height=10000, scrolling=False)