import sys, os
out = sys.argv[1]
HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="top"><div class="wrap nav">
  <a class="logo" href="index.html"><img src="mark.png" alt="">sharkflow<span>labs</span></a>
  <nav><a href="index.html#services">Services</a><a href="index.html#work">Work</a><a href="index.html#process">How it works</a><a href="index.html#faq">FAQ</a><a class="nav-cta" href="index.html#contact">Free demo</a></nav>
</div></header>
"""
FOOT = """<footer><div class="wrap row">
  <div>© 2026 Sharkflow Labs. Sharkflow Labs is a brand of {{REGISTERED_NAME}}.</div>
  <div><a href="privacy.html">Privacy Policy</a> · <a href="terms.html">Terms &amp; Conditions</a> · <a href="text-updates.html">Text updates</a> · <a href="mailto:{{EMAIL}}">{{EMAIL}}</a></div>
</div></footer>
</body>
</html>
"""
pages = {}
pages['index.html'] = ("Sharkflow Labs | Websites for local service businesses", "Sharkflow Labs designs fast, conversion-focused websites for roofers, plumbers, landscapers and other local service businesses. See a free demo of your new site before you pay.", """
<section class="hero"><div class="wrap hero-grid">
  <div>
    <p class="eyebrow">Websites for contractors &amp; home services</p>
    <h1>Websites that turn local searches into <em>booked jobs</em>.</h1>
    <p>We design fast, mobile-first websites for roofers, plumbers, HVAC, landscapers, painters and other local service businesses. You see a free demo of your new site before you pay a cent.</p>
    <div class="cta-row"><a class="btn primary" href="#contact">Get my free demo</a><a class="btn ghost" href="#work">See our work</a></div>
    <ul class="checks">
      <li>Free demo, no obligation</li>
      <li>Fixed price, no surprises</li>
      <li>Live in about 2 weeks</li>
    </ul>
  </div>
  <div class="hero-stack" aria-hidden="true">
    <div class="hs hs1"><div class="browser-bar"><i></i><i></i><i></i></div><img src="demo-jpgroofing.jpg" alt=""></div>
    <div class="hs hs2"><div class="browser-bar"><i></i><i></i><i></i></div><img src="demo-everpalmlandscapes.jpg" alt=""></div>
    <div class="hs hs3"><div class="browser-bar"><i></i><i></i><i></i></div><img src="work-orozco-desktop.jpg" alt=""></div>
    <div class="hero-badge"><b>25+</b><span>demo sites built for local businesses</span></div>
  </div>
</div></section>

<div class="strip"><div class="wrap strip-row">
  <span>Built for</span><b>Roofing</b><b>Plumbing</b><b>HVAC</b><b>Landscaping</b><b>Painting</b><b>Electrical</b><b>Cleaning</b>
</div></div>

<section id="problem"><div class="wrap split">
  <div>
    <h2>Your work is great. Does your website show it?</h2>
    <p class="lead">Most homeowners check you out on their phone before they call. If your site is slow, outdated or missing, they call the next company on Google.</p>
  </div>
  <ul class="pain">
    <li><b>No site, or just a Facebook page</b><span>Customers can't find your services, area or reviews in one place.</span></li>
    <li><b>Looks dated on a phone</b><span>Tiny text and hidden phone numbers send visitors back to Google.</span></li>
    <li><b>Visitors, but no calls</b><span>No clear "call now" or quote form means lost jobs every week.</span></li>
  </ul>
</div></section>

<section id="services" class="alt"><div class="wrap">
  <h2>Everything you need to get found and get calls</h2>
  <p class="lead">One focus: websites that make your phone ring.</p>
  <div class="grid">
    <div class="card"><div class="ico">&#9998;</div><h3>Custom website design</h3><p>A clean, professional site built around your services, service area, photos and reviews.</p></div>
    <div class="card"><div class="ico">&#9742;</div><h3>Built to get calls</h3><p>Tap-to-call buttons, quote forms and instant alerts on every page, so no lead slips through.</p></div>
    <div class="card"><div class="ico">&#9873;</div><h3>Local SEO basics</h3><p>Service and area pages, fast load times and Google Business Profile setup so nearby customers find you.</p></div>
    <div class="card"><div class="ico">&#10003;</div><h3>Hosting and care</h3><p>Hosting, SSL, backups and small text or photo updates handled for you.</p></div>
  </div>
</div></section>

<section id="work" class="work-sec"><div class="wrap">
  <p class="eyebrow-dark">Our work</p>
  <h2>Websites built to make the phone ring</h2>
  <p class="lead">A live client site and real demo homepages we've built for local service businesses across the US. Every one puts a quote form and a call button where customers can't miss them.</p>

  <article class="feature">
    <div class="feature-media">
      <div class="browser"><div class="browser-bar"><i></i><i></i><i></i><span>orozcopainterssolutions.com</span></div><img src="work-orozco-desktop.jpg" alt="Orozco Painters Solutions homepage on desktop" loading="lazy"></div>
      <div class="phone-frame"><img src="work-orozco-phone.jpg" alt="Orozco Painters Solutions homepage on a phone" loading="lazy"></div>
    </div>
    <div class="feature-copy">
      <span class="live-tag"><b></b>Live client site</span>
      <h3>Orozco Painters Solutions</h3>
      <p class="meta">House painting · San Marcos, CA</p>
      <p>A licensed painting contractor serving San Marcos and North County San Diego needed a site that turns visitors into estimate requests.</p>
      <ul class="built">
        <li>Free estimate form right in the hero, with interior, exterior or both</li>
        <li>Tap-to-call button and a sticky call bar on phones</li>
        <li>License number and 5.0 Yelp rating shown up top</li>
        <li>Clear service area: San Marcos and North County San Diego</li>
      </ul>
      <div class="cta-row"><a class="btn primary" href="https://orozcopainterssolutions.com/" target="_blank" rel="noopener">Visit live site ↗</a><a class="btn outline" href="#contact">Get a site like this</a></div>
    </div>
  </article>

  <div class="concepts-head"><div><h3>Demo homepages we've designed</h3><p>Free demos we built for local businesses to show what their new site could look like. Click any one to see it live.</p></div>
    <div class="filters" role="tablist"><button class="chip-f on" data-f="all">All</button><button class="chip-f" data-f="plumbing">Plumbing &amp; HVAC</button><button class="chip-f" data-f="roofing">Roofing</button><button class="chip-f" data-f="outdoor">Outdoor</button><button class="chip-f" data-f="remodel">Remodeling</button><button class="chip-f" data-f="cleaning">Cleaning</button></div></div>
  <div class="demos">
    <a class="demo-card" data-cat="plumbing" href="https://hohmannoilandplumbing.pages.dev/" target="_blank" rel="noopener"><div class="browser sm"><div class="browser-bar"><i></i><i></i><i></i></div><img src="demo-hohmannoilandplumbing.jpg" alt="Demo homepage for A. Hohmann &amp; Co." loading="lazy"></div><div class="demo-cap"><span class="pill-c">Plumbing &amp; HVAC</span><b>A. Hohmann &amp; Co.</b><span>Heating, plumbing &amp; fuel oil · Dorchester, MA</span><em>View demo ↗</em></div></a>
    <a class="demo-card" data-cat="roofing" href="https://jpgroofing.pages.dev/" target="_blank" rel="noopener"><div class="browser sm"><div class="browser-bar"><i></i><i></i><i></i></div><img src="demo-jpgroofing.jpg" alt="Demo homepage for JP&amp;G Roofing" loading="lazy"></div><div class="demo-cap"><span class="pill-c">Roofing</span><b>JP&amp;G Roofing</b><span>Roof repair · Phoenix, AZ</span><em>View demo ↗</em></div></a>
    <a class="demo-card" data-cat="outdoor" href="https://everpalmlandscapes.pages.dev/" target="_blank" rel="noopener"><div class="browser sm"><div class="browser-bar"><i></i><i></i><i></i></div><img src="demo-everpalmlandscapes.jpg" alt="Demo homepage for Everpalm Landscapes" loading="lazy"></div><div class="demo-cap"><span class="pill-c">Outdoor</span><b>Everpalm Landscapes</b><span>Landscape design · South Florida</span><em>View demo ↗</em></div></a>
    <a class="demo-card" data-cat="outdoor" href="https://reyeshardscaping.pages.dev/" target="_blank" rel="noopener"><div class="browser sm"><div class="browser-bar"><i></i><i></i><i></i></div><img src="demo-reyeshardscaping.jpg" alt="Demo homepage for Reyes Hardscaping Plus" loading="lazy"></div><div class="demo-cap"><span class="pill-c">Outdoor</span><b>Reyes Hardscaping Plus</b><span>Patios, pool decks &amp; walls · New Jersey</span><em>View demo ↗</em></div></a>
    <a class="demo-card" data-cat="outdoor" href="https://avenidaconcrete.pages.dev/" target="_blank" rel="noopener"><div class="browser sm"><div class="browser-bar"><i></i><i></i><i></i></div><img src="demo-avenidaconcrete.jpg" alt="Demo homepage for Avenida Concrete" loading="lazy"></div><div class="demo-cap"><span class="pill-c">Outdoor</span><b>Avenida Concrete</b><span>Stamped concrete &amp; pools · Riverside County, CA</span><em>View demo ↗</em></div></a>
    <a class="demo-card" data-cat="remodel" href="https://upgraderemodeling.pages.dev/" target="_blank" rel="noopener"><div class="browser sm"><div class="browser-bar"><i></i><i></i><i></i></div><img src="demo-upgraderemodeling.jpg" alt="Demo homepage for Upgrade Remodeling" loading="lazy"></div><div class="demo-cap"><span class="pill-c">Remodeling</span><b>Upgrade Remodeling</b><span>Kitchens, baths &amp; remodels · Southern California</span><em>View demo ↗</em></div></a>
    <a class="demo-card" data-cat="remodel" href="https://bnoconstruction.pages.dev/" target="_blank" rel="noopener"><div class="browser sm"><div class="browser-bar"><i></i><i></i><i></i></div><img src="demo-bnoconstruction.jpg" alt="Demo homepage for BNO Construction" loading="lazy"></div><div class="demo-cap"><span class="pill-c">Remodeling</span><b>BNO Construction</b><span>Wood ceilings &amp; finish carpentry · Cape Coral, FL</span><em>View demo ↗</em></div></a>
    <a class="demo-card" data-cat="remodel" href="https://jatile.pages.dev/" target="_blank" rel="noopener"><div class="browser sm"><div class="browser-bar"><i></i><i></i><i></i></div><img src="demo-jatile.jpg" alt="Demo homepage for JA Tile" loading="lazy"></div><div class="demo-cap"><span class="pill-c">Remodeling</span><b>JA Tile</b><span>Tile, bathrooms &amp; floors · Massachusetts</span><em>View demo ↗</em></div></a>
    <a class="demo-card" data-cat="cleaning" href="https://4sisterscleaning.pages.dev/" target="_blank" rel="noopener"><div class="browser sm"><div class="browser-bar"><i></i><i></i><i></i></div><img src="demo-4sisterscleaning.jpg" alt="Demo homepage for 4 Sisters Cleaning" loading="lazy"></div><div class="demo-cap"><span class="pill-c">Cleaning</span><b>4 Sisters Cleaning</b><span>House cleaning · New Jersey</span><em>View demo ↗</em></div></a>
  </div>
  <p class="more-note">Plus more demos for painters, framers, insulation, siding, concrete and carpentry companies.</p>
<script>
document.querySelectorAll('.chip-f').forEach(b => b.addEventListener('click', () => {
  document.querySelectorAll('.chip-f').forEach(x => x.classList.toggle('on', x === b));
  document.querySelectorAll('.demo-card').forEach(c => { c.hidden = b.dataset.f !== 'all' && c.dataset.cat !== b.dataset.f; });
}));
</script>
</div></section>

<section id="process" class="alt"><div class="wrap">
  <h2>How it works</h2>
  <p class="lead">No long sales calls. You see the work first.</p>
  <div class="grid steps">
    <div class="card"><div class="num">1</div><h3>Free demo</h3><p>We build a demo homepage for your business using your services, photos and reviews.</p></div>
    <div class="card"><div class="num">2</div><h3>Your feedback</h3><p>Tell us what to change. We can walk through it on a quick video call if you like.</p></div>
    <div class="card"><div class="num">3</div><h3>Launch</h3><p>Approve the fixed price and we finish every page, connect your domain and go live.</p></div>
    <div class="card"><div class="num">4</div><h3>We look after it</h3><p>Hosting, security and small updates are handled, so you can get back to the jobs.</p></div>
  </div>
</div></section>

<section id="faq"><div class="wrap narrow">
  <h2>Questions owners ask</h2>
  <details><summary>Is the demo really free?</summary><p>Yes. We build a demo of your homepage first. If you don't like it, you owe nothing.</p></details>
  <details><summary>How long does it take?</summary><p>Most sites go live in about 2 weeks after you approve the demo, depending on how quickly we get your photos and details.</p></details>
  <details><summary>How much does it cost?</summary><p>A fixed price agreed before any work starts, based on the pages you need. No hourly billing and no surprise invoices.</p></details>
  <details><summary>Do I need to write the content?</summary><p>No. We write it for you from your services, service area and reviews. You just check it's right.</p></details>
  <details><summary>Will I own my website?</summary><p>Yes. Once it's paid for, the site and your domain are yours.</p></details>
  <details><summary>Can you update it later?</summary><p>Yes. Small text and photo changes are included with hosting and care.</p></details>
</div></section>

<section id="contact" class="cta-band quote"><div class="wrap quote-grid">
  <div>
    <h2>Get your free website demo</h2>
    <p>Tell us about your business and we'll build a demo of your new homepage, usually within 2 business days. No calls needed, no obligation.</p>
    <ul class="checks"><li>Free demo first</li><li>Fixed price</li><li>Live in about 2 weeks</li></ul>
    <p style="margin-top:20px">Prefer email? Write to <a href="mailto:{{EMAIL}}">{{EMAIL}}</a>.</p>
  </div>
  <form class="quote-form" id="quote" novalidate>
    <div class="two">
      <label>Your name *<input type="text" name="name" required autocomplete="name"></label>
      <label>Business name *<input type="text" name="business" required autocomplete="organization"></label>
    </div>
    <div class="two">
      <label>Phone *<input type="tel" name="phone" required autocomplete="tel" placeholder="(555) 123-4567"></label>
      <label>Email *<input type="email" name="email" required autocomplete="email"></label>
    </div>
    <div class="two">
      <label>Your trade<select name="trade"><option value="">Choose one</option><option>Roofing</option><option>Plumbing</option><option>HVAC</option><option>Electrical</option><option>Landscaping</option><option>Cleaning</option><option>Painting</option><option>Pest control</option><option>Other</option></select></label>
      <label>Current website (if any)<input type="text" name="website" inputmode="url" placeholder="yourbusiness.com"></label>
    </div>
    <label>Anything we should know?<textarea name="message" rows="3" placeholder="Services, service area, what you'd like the site to do"></textarea></label>
    <label class="hp" aria-hidden="true">Leave this empty<input type="text" name="company_website_hp" tabindex="-1" autocomplete="off"></label>
    <label class="consent"><input type="checkbox" name="agree_terms" required>
      <span>I agree to the <a href="privacy.html" target="_blank">Privacy Policy</a> and <a href="terms.html" target="_blank">Terms</a>. *</span></label>
    <label class="consent"><input type="checkbox" name="consent_contact">
      <span id="consentText">I agree to receive calls and text messages from Sharkflow Labs at the number above about my website demo, meeting links and reminders, and our services. Message frequency varies. Message and data rates may apply. Reply STOP to opt out or HELP for help. Consent is not a condition of purchase.</span></label>
    <button type="submit">Get my free demo</button>
    <p class="msg" id="quoteMsg" role="status"></p>
  </form>
</div></section>
<script>
document.getElementById('quote').addEventListener('submit', async (e) => {
  e.preventDefault();
  const f = e.target, msg = document.getElementById('quoteMsg'), btn = f.querySelector('button');
  for (const el of f.querySelectorAll('[required]')) {
    if (!el.checkValidity()) { el.focus(); msg.textContent = el.type === 'checkbox' ? 'Please agree to the Privacy Policy and Terms.' : 'Please fill in ' + el.closest('label').firstChild.textContent.replace('*','').trim().toLowerCase() + '.'; return; }
  }
  const data = Object.fromEntries(new FormData(f));
  data.agree_terms = f.agree_terms.checked;
  data.consent_contact = f.consent_contact.checked;
  data.consent_text = data.consent_contact ? document.getElementById('consentText').textContent.trim() : '';
  btn.disabled = true; msg.textContent = 'Sending…';
  try {
    const r = await fetch('https://sharkflow-phone.preethamsaixp.workers.dev/public/lead', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(data) });
    const j = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(j.error || 'Something went wrong');
    f.reset(); msg.textContent = 'Thanks! We got your details and will be in touch soon with your demo.';
  } catch (err) { msg.textContent = err.message + '. You can also email {{EMAIL}}.'; }
  finally { btn.disabled = false; }
});
</script>
""")

pages['text-updates.html'] = ("Text updates | Sharkflow Labs", "How Sharkflow Labs asks permission before sending text messages, and how to opt in or out.", """
<main class="doc"><div class="wrap">
  <h1>Text updates from Sharkflow Labs</h1>
  <p class="updated">How we ask before we text you, and how to stop.</p>

  <div class="contact">
    <div>
      <h2 style="margin-top:0">Request your free demo by text</h2>
      <form class="optin" id="optin">
        <label>Your name<input type="text" name="name" required autocomplete="name"></label>
        <label>Business name<input type="text" name="business" required autocomplete="organization"></label>
        <label>Mobile number<input type="tel" name="phone" required autocomplete="tel" placeholder="(555) 123-4567"></label>
        <label class="consent"><input type="checkbox" name="consent" required>
          <span>I agree to receive text messages from Sharkflow Labs about my website demo, meeting links and reminders, and follow-ups about our services. Message frequency varies. Message and data rates may apply. Reply STOP to opt out or HELP for help. Consent is not a condition of purchase. See our <a href="privacy.html">Privacy Policy</a> and <a href="terms.html">Terms</a>.</span></label>
        <button type="submit">Text me my demo</button>
        <p class="msg" id="optinMsg" role="status"></p>
      </form>
    </div>
    <div>
      <h2 style="margin-top:0">How we get your permission</h2>
      <p>We only text people who have agreed to it. Business owners agree in one of these ways:</p>
      <ul>
        <li>Submitting the form on this page with the box ticked.</li>
        <li>Saying yes when we ask, by Instagram message, email or phone: <em>"Can I text you the demo link and a link for our call? It will come from our business number, message and data rates may apply, and you can reply STOP anytime."</em></li>
        <li>Texting our number first.</li>
      </ul>
      <p>We record when and how each person agreed before we send any text.</p>
      <div class="chat" aria-label="Example of how we ask for permission">
        <div class="bubble me">I made a free demo of a new website for your business. Can I text you the link? It'll come from our business number, msg &amp; data rates may apply, and you can reply STOP anytime.</div>
        <div class="bubble them">Sure, send it over</div>
      </div>
    </div>
  </div>

  <h2>What we send</h2>
  <p>Your website demo link, Google Meet links for calls you agreed to, reminders before those calls, and follow-ups about your demo and pricing. Every message is sent by a person, one at a time, from our business number +1 (470) 706-1294. Message frequency varies.</p>
  <h2>How to stop</h2>
  <div class="box">Reply <b>STOP</b> to any message to stop all texts. Reply <b>START</b> to resubscribe. Reply <b>HELP</b> for help, or email <a href="mailto:{{EMAIL}}">{{EMAIL}}</a>. Message and data rates may apply.</div>
  <h2>Your privacy</h2>
  <p>We do not sell or share your SMS opt-in data or personal information with third parties for marketing purposes. We also do not share your phone number or text messaging opt-in data with affiliates for marketing purposes. Read the full <a href="privacy.html">Privacy Policy</a>.</p>
</div></main>
<script>
document.getElementById('optin').addEventListener('submit', async (e) => {
  e.preventDefault();
  const f = e.target, msg = document.getElementById('optinMsg'), btn = f.querySelector('button');
  const data = Object.fromEntries(new FormData(f));
  data.consent = f.consent.checked;
  data.consent_text = f.querySelector('.consent span').textContent.trim();
  btn.disabled = true; msg.textContent = 'Sending…';
  try {
    const r = await fetch('https://sharkflow-phone.preethamsaixp.workers.dev/public/optin', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(data) });
    const j = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(j.error || 'Something went wrong');
    f.reset(); msg.textContent = 'Thanks! We\\'ll text you your demo link soon.';
  } catch (err) { msg.textContent = err.message + '. You can also email {{EMAIL}}.'; }
  finally { btn.disabled = false; }
});
</script>
""")

pages['privacy.html'] = ("Privacy Policy | Sharkflow Labs", "Privacy Policy for Sharkflow Labs, including text messaging.", """
<main class="doc"><div class="wrap">
  <h1>Privacy Policy</h1>
  <p class="updated">Last updated 22 November 2026</p>
  <p>Sharkflow Labs is a brand of {{REGISTERED_NAME}} ("we", "us"). This policy explains what we collect when you contact us or use this website, and how we use it.</p>
  <h2>What we collect</h2>
  <p>Business contact details you give us or that are publicly listed for your business: your name, business name, phone number, email address, website and social media profile. We also keep records of our messages and calls with you, including call recordings where we tell you a call may be recorded.</p>
  <h2>How we use it</h2>
  <p>To prepare your website demo, contact you about it, schedule and remind you of calls, provide our services and keep business records. We do not use your information for any unrelated purpose.</p>
  <h2>Text messaging</h2>
  <div class="box">If you agree to receive text messages from Sharkflow Labs, we use your phone number only to send you messages about your website demo, meetings and our services. Message frequency varies. Message and data rates may apply. Reply STOP to opt out or HELP for help. We do not sell or share your SMS opt-in data or personal information with third parties for marketing purposes. We also do not share your phone number or text messaging opt-in data with affiliates for marketing purposes.</div>
  <h2>Who we share it with</h2>
  <p>Only service providers that help us run the business, such as our phone and messaging provider (Twilio), hosting (Cloudflare) and email. They may only use it to provide their service to us. We do not sell personal information.</p>
  <p>No mobile information will be shared with third parties or affiliates for marketing or promotional purposes. Text messaging originator opt-in data and consent are excluded from all of the sharing described above and will not be shared with any third parties.</p>
  <h2>How long we keep it</h2>
  <p>As long as we are in contact with you, and for up to 2 years after, unless you ask us to delete it sooner or the law requires us to keep it longer.</p>
  <h2>Your choices</h2>
  <p>You can ask us to see, correct or delete your information, or to stop contacting you, at any time by emailing <a href="mailto:{{EMAIL}}">{{EMAIL}}</a>. Reply STOP to any text to stop texts.</p>
  <h2>Contact</h2>
  <p>{{REGISTERED_NAME}} (Sharkflow Labs). Email <a href="mailto:{{EMAIL}}">{{EMAIL}}</a>.</p>
</div></main>
""")

pages['terms.html'] = ("Terms & Conditions | Sharkflow Labs", "Terms of service and messaging terms for Sharkflow Labs.", """
<main class="doc"><div class="wrap">
  <h1>Terms &amp; Conditions</h1>
  <p class="updated">Last updated 22 November 2026</p>
  <p>These terms apply to this website and to services from Sharkflow Labs, a brand of {{REGISTERED_NAME}}.</p>
  <h2>Demos and projects</h2>
  <p>Website demos are free and come with no obligation. Paid work starts only after you approve a written price and scope. Ownership of the finished website passes to you once it is paid for.</p>
  <h2>SMS Terms</h2>
  <div class="box">
    <p style="margin-top:0"><b>Program:</b> Sharkflow Labs texts about website demos, meeting links and reminders, and follow-ups about our services, sent only to people who agreed to receive them. Texts come from our business number, +1 (470) 706-1294.</p>
    <p><b>Frequency:</b> Message frequency varies.</p>
    <p><b>Cost:</b> Message and data rates may apply.</p>
    <p><b>Opt out:</b> Reply STOP to any message to stop. Reply START to resubscribe.</p>
    <p><b>Help:</b> Reply HELP or email <a href="mailto:{{EMAIL}}">{{EMAIL}}</a>.</p>
    <p style="margin-bottom:0">Carriers are not liable for delayed or undelivered messages. See our <a href="privacy.html">Privacy Policy</a>.</p>
  </div>
  <h2>Contact</h2>
  <p>Email <a href="mailto:{{EMAIL}}">{{EMAIL}}</a>.</p>
</div></main>
""")

import json
vals = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
def fill(t):
    reg, city, email = vals.get('REGISTERED_NAME'), vals.get('CITY'), vals.get('EMAIL', 'hello@sharkflowlabs.com')
    if not reg:
        t = t.replace(' Sharkflow Labs is a brand of {{REGISTERED_NAME}}.', '')
        t = t.replace('Sharkflow Labs is a brand of {{REGISTERED_NAME}} ("we", "us")', 'Sharkflow Labs ("we", "us")')
        t = t.replace(', a brand of {{REGISTERED_NAME}}.', '.')
        t = t.replace('<p>{{REGISTERED_NAME}} (Sharkflow Labs). Email', '<p>Sharkflow Labs. Email')
    t = t.replace('{{REGISTERED_NAME}}', reg or 'Sharkflow Labs').replace('{{EMAIL}}', email)
    assert '{{' not in t, t[t.index('{{')-80:t.index('{{')+80]
    return t
for name, (title, desc, body) in pages.items():
    with open(os.path.join(out, name), 'w') as fh:
        fh.write(fill(HEAD.format(title=title, desc=desc) + body + FOOT))
print('ok')
