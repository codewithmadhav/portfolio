:root {
  --bg: #0b1020;
  --bg-soft: #121a2d;
  --surface: rgba(17, 25, 40, 0.8);
  --surface-strong: #121b2f;
  --card: rgba(18, 28, 48, 0.92);
  --text: #e7edf8;
  --muted: #a7b7d6;
  --line: rgba(165, 186, 222, 0.14);
  --primary: #7cc7ff;
  --primary-strong: #8b5cf6;
  --accent: #8ef3d7;
  --shadow: 0 18px 45px rgba(1, 4, 20, 0.45);
  --radius: 18px;
  --container: 1160px;
}

html[data-theme="light"] {
  --bg: #f3f7ff;
  --bg-soft: #edf3ff;
  --surface: rgba(255, 255, 255, 0.75);
  --surface-strong: #ffffff;
  --card: rgba(255, 255, 255, 0.96);
  --text: #101828;
  --muted: #53627d;
  --line: rgba(42, 52, 78, 0.12);
  --primary: #2957ff;
  --primary-strong: #6a4ef7;
  --accent: #0f9d8a;
  --shadow: 0 18px 45px rgba(12, 22, 48, 0.12);
}

* { box-sizing: border-box; }

html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: "Inter", sans-serif;
  background:
    radial-gradient(circle at top left, rgba(124, 199, 255, 0.14), transparent 25%),
    radial-gradient(circle at bottom right, rgba(139, 92, 246, 0.12), transparent 28%),
    var(--bg);
  color: var(--text);
  transition: background 0.3s ease, color 0.3s ease;
}

img { max-width: 100%; display: block; }
a { color: inherit; text-decoration: none; }
button, input, textarea, select { font: inherit; }

.container { width: min(var(--container), calc(100% - 2rem)); margin-inline: auto; }
.section-spacing { padding: 5rem 0; }
.eyebrow {
  display: inline-block;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.72rem;
  color: var(--primary);
  margin-bottom: 0.75rem;
}

h1, h2, h3, h4 { margin: 0 0 1rem; line-height: 1.08; }
h1 { font-size: clamp(2.8rem, 4vw, 5rem); }
h2 { font-size: clamp(2rem, 2.5vw, 3rem); }
h3 { font-size: 1.4rem; }
p { margin: 0 0 1rem; color: var(--muted); line-height: 1.7; }

.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  backdrop-filter: blur(16px);
  background: rgba(11, 16, 32, 0.72);
  border-bottom: 1px solid var(--line);
}
html[data-theme="light"] .site-header { background: rgba(255,255,255,0.7); }

.nav {
  min-height: 78px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
.brand {
  display: inline-flex;
  align-items: center;
  gap: 0.7rem;
  font-weight: 700;
  letter-spacing: -0.04em;
}
.brand-mark {
  width: 2rem;
  height: 2rem;
  display: grid;
  place-items: center;
  border-radius: 8px;
  background: linear-gradient(135deg, var(--primary), var(--primary-strong));
  color: #fff;
  box-shadow: var(--shadow);
}
.nav-links { display: flex; align-items: center; gap: 1.2rem; }
.nav-links a { color: var(--muted); font-size: 0.95rem; transition: color 0.2s ease; }
.nav-links a:hover, .nav-links a.active { color: var(--text); }
.nav-actions { display: flex; align-items: center; }
.theme-toggle {
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--text);
  border-radius: 999px;
  width: 42px;
  height: 42px;
  cursor: pointer;
}
.nav-toggle { display: none; }

.hero {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  align-items: center;
  gap: 2rem;
  min-height: 78vh;
}
.hero-copy { position: relative; z-index: 1; }
.hero-subtitle { font-size: clamp(1.05rem, 1.2vw, 1.4rem); max-width: 620px; }
.hero-actions, .social-row, .card-actions, .field-row, .check-row, .tag-row, .chip-row, .footer-links, .admin-links { display: flex; flex-wrap: wrap; gap: 0.8rem; align-items: center; }
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  padding: 0.9rem 1.4rem;
  border: 1px solid transparent;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  font-weight: 600;
}
.btn:hover { transform: translateY(-1px); }
.btn-primary {
  background: linear-gradient(135deg, var(--primary), var(--primary-strong));
  box-shadow: 0 10px 30px rgba(124, 199, 255, 0.25);
  color: #fff;
}
.btn-secondary {
  background: transparent;
  border-color: var(--line);
  color: var(--text);
}
.btn.small { padding: 0.6rem 0.9rem; font-size: 0.9rem; }
.social-row { margin-top: 1.25rem; }
.social-row a { color: var(--muted); font-weight: 500; }
.social-row a:hover { color: var(--text); }

.profile-card {
  position: relative;
  border: 1px solid var(--line);
  background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
  border-radius: 28px;
  padding: 1rem;
  box-shadow: var(--shadow);
}
.profile-image-wrap {
  overflow: hidden;
  border-radius: 22px;
  border: 1px solid var(--line);
}
.profile-image-wrap img {
  width: 100%;
  object-fit: cover;
  min-height: 520px;
}
.profile-badges { display: flex; gap: 0.6rem; flex-wrap: wrap; margin-top: 1rem; }
.profile-badges span, .chip-row span, .mini-tag, .tag-pill {
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 0.45rem 0.8rem;
  font-size: 0.8rem;
  color: var(--muted);
  background: rgba(255,255,255,0.02);
}

.section-heading { margin-bottom: 2rem; }
.project-heading { display: flex; justify-content: space-between; align-items: end; gap: 1rem; }
.text-link { color: var(--primary); font-weight: 600; }

.about-grid { display: grid; grid-template-columns: 1.3fr 0.7fr; gap: 1.4rem; }
.mini-panel, .contact-card, .achievement-card, .activity-panel, .project-card, .blog-card, .gallery-item, .admin-panel, .stat-card, .message-card, .auth-card, .not-found-card, .project-detail, .featured-post {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}
.mini-panel { padding: 1.4rem 1.5rem; }
.mini-panel ul { margin: 0; padding-left: 1.2rem; color: var(--muted); }
.mini-panel li + li { margin-top: 0.7rem; }

.skills-grid, .project-grid, .blog-preview-grid, .achievement-grid, .stats-grid, .admin-panels { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1rem; }
.skill-group, .achievement-card, .stat-card, .admin-panel, .message-card { padding: 1.4rem; }
.skill-group h3 { margin-bottom: 0.8rem; }
.skill-group ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 0.6rem; }
.skill-group li { border: 1px solid var(--line); border-radius: 999px; padding: 0.5rem 0.8rem; color: var(--muted); }

.project-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.project-card, .blog-card, .featured-post { overflow: hidden; }
.project-image-wrap img, .blog-card img, .featured-post img, .gallery-item img { width: 100%; height: 220px; object-fit: cover; transition: transform 0.35s ease; }
.project-card:hover .project-image-wrap img, .gallery-item:hover img, .blog-card:hover img, .featured-post:hover img { transform: scale(1.04); }
.project-body, .blog-card-body { padding: 1.2rem; }
.project-body p, .blog-card-body p { margin-bottom: 1rem; }

.timeline { display: grid; gap: 1rem; }
.timeline-item {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  display: grid;
  grid-template-columns: 120px 1fr;
  gap: 1rem;
  padding: 1.2rem 1.5rem;
}
.timeline-item .year { color: var(--primary); font-weight: 700; }

.blog-preview-grid { grid-template-columns: repeat(3, minmax(0,1fr)); }
.post-meta { display: inline-block; color: var(--primary); margin-bottom: 0.7rem; font-size: 0.8rem; }

.photo-grid-compact { display: grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap: 1rem; }
.photo-card { margin: 0; overflow: hidden; border-radius: 16px; border: 1px solid var(--line); background: var(--card); }
.photo-card img { width: 100%; height: 260px; object-fit: cover; }

.achievement-grid { grid-template-columns: repeat(3, minmax(0,1fr)); }
.achievement-tag { display: inline-block; margin-bottom: 0.75rem; color: var(--accent); font-size: 0.72rem; letter-spacing: 0.1em; text-transform: uppercase; }

.activity-panel { padding: 1.25rem; }
.activity-row {
  display: grid;
  grid-template-columns: 120px 1fr;
  gap: 1rem;
  padding: 0.8rem 0;
  border-bottom: 1px solid var(--line);
}
.activity-row:last-child { border-bottom: none; }
.activity-row span { color: var(--muted); }

.contact-grid { display: grid; grid-template-columns: 0.8fr 1.2fr; gap: 1rem; }
.contact-form, .admin-form { display: grid; gap: 1rem; }
.contact-card, .auth-card, .admin-form { padding: 1.5rem; }
label { display: grid; gap: 0.5rem; color: var(--text); font-weight: 500; }
input, textarea, select {
  width: 100%;
  border: 1px solid var(--line);
  background: rgba(255,255,255,0.01);
  color: var(--text);
  border-radius: 12px;
  padding: 0.8rem 0.9rem;
}
textarea { resize: vertical; }

.page-shell, .gallery-shell, .blog-shell, .blog-detail-shell, .admin-shell, .auth-shell { min-height: 70vh; }

.blog-grid, .gallery-grid { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 1.2rem; }
.search-bar { display: flex; gap: 0.7rem; margin-bottom: 1.2rem; }
.search-bar input { flex: 1; }
.category-row { display: flex; flex-wrap: wrap; gap: 0.7rem; margin-bottom: 1.5rem; }
.tag-pill { cursor: pointer; }
.tag-pill.active { background: rgba(124,199,255,0.08); color: var(--text); border-color: rgba(124,199,255,0.25); }
.featured-posts { display: grid; gap: 1rem; margin-bottom: 2rem; }
.featured-post { display: grid; grid-template-columns: 260px 1fr; }
.featured-post img { height: 100%; min-height: 220px; }
.featured-post > div { padding: 1.2rem; }

.article-hero { width: 100%; height: 440px; object-fit: cover; border-radius: 20px; border: 1px solid var(--line); }
.blog-detail-shell { display: grid; grid-template-columns: minmax(0,1fr) 290px; gap: 1.5rem; }
.article { padding: 0; }
.article-header { margin-top: 2rem; }
.article-meta { display: flex; gap: 0.7rem; color: var(--muted); font-size: 0.9rem; }
.article-body { margin-top: 2rem; }
.article-body pre, .article-body code {
  background: rgba(12, 19, 34, 0.8);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 1rem;
  overflow-x: auto;
}
.article-body h2, .article-body h3 { margin-top: 1.8rem; }
.article-body blockquote {
  margin: 1.5rem 0;
  padding-left: 1rem;
  border-left: 3px solid var(--primary);
  color: var(--text);
}
.sidebar { display: grid; gap: 1rem; }
.sidebar-panel { padding: 1.2rem; background: var(--card); border: 1px solid var(--line); border-radius: var(--radius); }
.sidebar-list, .related-list { list-style: none; padding: 0; margin: 0; display: grid; gap: 0.8rem; }
.share-row { display: flex; flex-wrap: wrap; gap: 0.8rem; margin-top: 2rem; }

.gallery-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.gallery-item { overflow: hidden; border-radius: 18px; }
.gallery-item figcaption {
  display: grid;
  gap: 0.25rem;
  padding: 0.9rem 1rem 1rem;
}
.gallery-item figcaption span { color: var(--muted); font-size: 0.9rem; }

.admin-shell, .auth-shell { padding-top: 2rem; }
.stats-grid { grid-template-columns: repeat(4, minmax(0,1fr)); }
.stat-card { text-align: center; }
.stat-card span { color: var(--muted); display: block; margin-bottom: 0.7rem; }
.stat-card strong { font-size: 2rem; }
.admin-panels { grid-template-columns: repeat(2, minmax(0,1fr)); margin-top: 1.25rem; }
.admin-panel ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 0.8rem; }
.admin-panel li { display: flex; justify-content: space-between; gap: 0.5rem; padding-bottom: 0.7rem; border-bottom: 1px solid var(--line); }
.admin-panel li:last-child { border-bottom: none; padding-bottom: 0; }

.auth-card { width: min(500px, 100%); margin: 2rem auto 0; }
.auth-card h1 { margin-top: 0.5rem; }

.message-card { margin-bottom: 1rem; }
.check-row { display: flex; justify-content: space-between; }
.tag-select-grid { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 0.6rem; }
.tag-select-grid label { display: flex; align-items: center; gap: 0.5rem; }

.site-footer {
  border-top: 1px solid var(--line);
  padding: 2rem 0 3rem;
  margin-top: 3rem;
}
.footer-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}
.footer-brand { font-weight: 700; font-size: 1.1rem; color: var(--text); }

.back-to-top {
  position: fixed; right: 1.5rem; bottom: 1.5rem;
  border: none; width: 48px; height: 48px; border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), var(--primary-strong));
  color: white; box-shadow: var(--shadow); cursor: pointer; opacity: 0; pointer-events: none; transition: 0.2s ease;
}
.back-to-top.visible { opacity: 1; pointer-events: auto; }

.flash-stack { padding-top: 1rem; }
.flash {
  padding: 0.9rem 1rem; border: 1px solid var(--line); border-radius: 12px; margin-bottom: 0.7rem;
}
.flash-success { background: rgba(82, 183, 140, 0.12); border-color: rgba(82, 183, 140, 0.3); }
.flash-error { background: rgba(223, 87, 87, 0.12); border-color: rgba(223, 87, 87, 0.3); }

.scroll-progress {
  position: fixed;
  inset: 0 0 auto 0;
  height: 3px;
  background: linear-gradient(90deg, var(--primary), var(--primary-strong));
  transform-origin: left center;
  transform: scaleX(0);
  z-index: 40;
}

.page-loader {
  position: fixed;
  inset: 0;
  background: rgba(11, 16, 32, 0.8);
  display: grid;
  place-items: center;
  z-index: 50;
  transition: opacity 0.25s ease, visibility 0.25s ease;
}
.page-loader.hidden { opacity: 0; visibility: hidden; }
.loader-ring {
  width: 54px; height: 54px;
  border-radius: 50%;
  border: 2px solid rgba(255,255,255,0.12);
  border-top-color: var(--primary);
  animation: spin 1s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

.not-found-shell { display: grid; place-items: center; }
.not-found-card { width: min(560px, 100%); padding: 2.5rem; text-align: center; }

@media (max-width: 960px) {
  .hero, .about-grid, .contact-grid, .blog-detail-shell { grid-template-columns: 1fr; }
  .skills-grid { grid-template-columns: repeat(2, minmax(0,1fr)); }
  .project-grid, .blog-preview-grid, .achievement-grid, .blog-grid, .gallery-grid { grid-template-columns: repeat(2, minmax(0,1fr)); }
  .photo-grid-compact { grid-template-columns: repeat(2, minmax(0,1fr)); }
}

@media (max-width: 720px) {
  .nav-toggle { display: inline-flex; flex-direction: column; gap: 4px; background: transparent; border: none; cursor: pointer; }
  .nav-toggle span { width: 24px; height: 2px; background: var(--text); border-radius: 2px; }
  .nav-links { position: absolute; top: 100%; left: 1rem; right: 1rem; display: none; flex-direction: column; align-items: flex-start; background: var(--surface-strong); border: 1px solid var(--line); border-radius: 16px; padding: 1rem; }
  .nav-links.open { display: flex; }
  .hero { padding-top: 2rem; }
  .skills-grid, .stats-grid, .project-grid, .blog-preview-grid, .achievement-grid, .blog-grid, .gallery-grid, .photo-grid-compact, .admin-panels { grid-template-columns: 1fr; }
  .project-heading, .footer-inner { flex-direction: column; align-items: flex-start; }
  .timeline-item { grid-template-columns: 1fr; }
  .featured-post { grid-template-columns: 1fr; }
  .search-bar { flex-direction: column; }
  .check-row { justify-content: flex-start; flex-direction: column; }
}

.reveal {
  opacity: 0;
  transform: translateY(18px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
