import os

ROOT = "/home/claude/portfolio"

SKELETON = """<!doctype html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta_desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family={font_display_url}&family={font_body_url}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{assets_prefix}assets/site.css">
<style>
  :root{{
    --bg:{bg}; --surface:{surface}; --text:{text}; --muted:{muted};
    --line:{line}; --line-strong:{line_strong};
    --accent:{accent}; --accent-contrast:{accent_contrast};
    --font-display:'{font_display}', serif;
    --font-body:'{font_body}', sans-serif;
    --radius:{radius};
  }}
  {extra_css}
</style>
</head>
<body>

<header class="nav">
  <div class="nav-inner">
    <a href="#accueil" class="brand">{brand_name} <span>{brand_suffix}</span></a>
    <nav class="links">
      <a href="#accueil">Accueil</a>
      <a href="#apropos">À propos</a>
      <a href="#services">{services_label}</a>
      <a href="#contact">Contact</a>
    </nav>
    <a href="#contact" class="nav-cta">{nav_cta}</a>
    <button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
  <div class="mobile-menu">
    <a href="#accueil">Accueil</a>
    <a href="#apropos">À propos</a>
    <a href="#services">{services_label}</a>
    <a href="#contact">Contact</a>
  </div>
</header>

{hero}

{apropos}

{services}

{extra_section}

{contact}

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="brand" style="margin-bottom:12px;">{brand_name} <span>{brand_suffix}</span></div>
        <p class="lede" style="font-size:14px;">{footer_tagline}</p>
      </div>
      <div>
        <h4>Navigation</h4>
        <a href="#accueil">Accueil</a>
        <a href="#apropos">À propos</a>
        <a href="#services">{services_label}</a>
        <a href="#contact">Contact</a>
      </div>
      <div>
        <h4>Contact</h4>
        <a href="tel:{phone}">{phone}</a>
        <a href="mailto:{email}">{email}</a>
        <a href="#">{address}</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 {brand_name}. Site de démonstration — portfolio.</span>
      <span><a href="../index.html">← Retour au portfolio</a></span>
    </div>
  </div>
</footer>

<script src="{assets_prefix}assets/site.js"></script>
</body>
</html>
"""

def _write(path, html):
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(html)
    print("written:", path)


def page(path, **kw):
    kw.setdefault("assets_prefix", "../")
    html = SKELETON.format(**kw)
    _write(path, html)


def hero(eyebrow, title, lede, cta_primary, cta_ghost, img_seed, img_ratio="4/5", stats=None, badge=None):
    stats_html = ""
    if stats:
        items = "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v, l in stats)
        stats_html = f'<div class="stats reveal">{items}</div>'
    badge_html = f'<div class="badge reveal"><span class="dot"></span>{badge}</div>' if badge else ""
    return f"""
<section class="hero" id="accueil">
  <div class="container hero-grid">
    <div>
      {badge_html}
      <div class="eyebrow reveal">{eyebrow}</div>
      <h1 class="reveal">{title}</h1>
      <p class="lede reveal">{lede}</p>
      <div class="hero-actions reveal">
        <a href="#contact" class="btn btn-primary">{cta_primary}</a>
        <a href="#services" class="btn btn-ghost">{cta_ghost}</a>
      </div>
      {stats_html}
    </div>
    <div class="hero-media reveal">
      <img src="https://picsum.photos/seed/{img_seed}/900/1100" alt="{title}" style="aspect-ratio:{img_ratio};">
    </div>
  </div>
</section>
"""


def apropos(eyebrow, title, paragraphs, img_seed, reverse=False):
    p_html = "".join(f"<p>{p}</p>" for p in paragraphs)
    text_block = f"""
    <div>
      <div class="eyebrow reveal">{eyebrow}</div>
      <h2 class="section-title reveal">{title}</h2>
      <div class="reveal">{p_html}</div>
    </div>"""
    img_block = f"""
    <div class="reveal"><img src="https://picsum.photos/seed/{img_seed}/900/700" alt="{title}"></div>"""
    order = [img_block, text_block] if reverse else [text_block, img_block]
    return f"""
<section class="section" id="apropos">
  <div class="container split">
    {order[0]}
    {order[1]}
  </div>
</section>
"""


def services(eyebrow, title, lede, items, alt=True):
    cards = "".join(
        f'<div class="card reveal"><div class="icon">{icon}</div><h3>{name}</h3><p>{desc}</p></div>'
        for icon, name, desc in items
    )
    cls = "section alt" if alt else "section"
    return f"""
<section class="{cls}" id="services">
  <div class="container">
    <div class="eyebrow reveal">{eyebrow}</div>
    <h2 class="section-title reveal">{title}</h2>
    <p class="lede reveal" style="margin-bottom:44px;">{lede}</p>
    <div class="grid-3">{cards}</div>
  </div>
</section>
"""


def gallery_section(eyebrow, title, seeds):
    imgs = "".join(
        f'<a href="https://picsum.photos/seed/{s}/900/900" target="_blank" rel="noopener"><img src="https://picsum.photos/seed/{s}/500/500" alt="Photo {i+1}" loading="lazy"></a>'
        for i, s in enumerate(seeds)
    )
    return f"""
<section class="section" id="galerie">
  <div class="container">
    <div class="eyebrow reveal">{eyebrow}</div>
    <h2 class="section-title reveal" style="margin-bottom:36px;">{title}</h2>
    <div class="gallery reveal">{imgs}</div>
  </div>
</section>
"""


def testimonials_section(eyebrow, title, quotes, alt=True):
    cards = "".join(
        f"""<div class="quote reveal"><div class="stars">*****</div><p>{q}</p><div class="who">{who}<span>{sub}</span></div></div>"""
        for q, who, sub in quotes
    )
    cls = "section alt" if alt else "section"
    return f"""
<section class="{cls}">
  <div class="container">
    <div class="eyebrow reveal">{eyebrow}</div>
    <h2 class="section-title reveal" style="margin-bottom:36px;">{title}</h2>
    <div class="grid-3">{cards}</div>
  </div>
</section>
"""


def banner_section(title, text, cta):
    return f"""
<section class="section">
  <div class="container">
    <div class="banner reveal">
      <h2>{title}</h2>
      <p>{text}</p>
      <a href="#contact" class="btn" style="background:var(--accent-contrast); color:var(--accent); margin-top:14px;">{cta}</a>
    </div>
  </div>
</section>
"""


def contact_section(eyebrow, title, lede, phone, email, address, hours, map_query, submit_label="Envoyer le message"):
    return f"""
<section class="section alt" id="contact">
  <div class="container">
    <div class="eyebrow reveal">{eyebrow}</div>
    <h2 class="section-title reveal">{title}</h2>
    <p class="lede reveal" style="margin-bottom:40px;">{lede}</p>
    <div class="contact-grid">
      <div class="reveal">
        <form class="contact-form">
          <div class="field"><label>Nom complet</label><input type="text" required placeholder="Votre nom"></div>
          <div class="field"><label>E-mail</label><input type="email" required placeholder="vous@exemple.com"></div>
          <div class="field"><label>Message</label><textarea required placeholder="Votre message..."></textarea></div>
          <button type="submit" class="btn btn-primary" style="width:100%;">{submit_label}</button>
        </form>
        <p class="form-note">Formulaire de demonstration : aucun message n'est reellement envoye (aucun serveur, aucune cle API). Voir le README pour brancher un vrai service d'envoi.</p>
        <div class="contact-info">
          <div><b>Telephone</b>{phone}</div>
          <div><b>E-mail</b>{email}</div>
          <div><b>Adresse</b>{address}</div>
          <div><b>Horaires</b>{hours}</div>
        </div>
      </div>
      <div class="map reveal">
        <iframe loading="lazy" src="https://www.google.com/maps?q={map_query}&output=embed"></iframe>
      </div>
    </div>
  </div>
</section>
"""
