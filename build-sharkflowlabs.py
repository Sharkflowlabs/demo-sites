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
  <nav><a href="index.html#services">Services</a><a href="index.html#work">Work</a><a href="index.html#process">How it works</a><a href="text-updates.html">Get your demo</a><a href="index.html#contact">Contact</a></nav>
</div></header>
"""
FOOT = """<footer><div class="wrap row">
  <div>© 2026 Sharkflow Labs. Sharkflow Labs is a brand of {{REGISTERED_NAME}}, {{CITY}}, India.</div>
  <div><a href="privacy.html">Privacy Policy</a> · <a href="terms.html">Terms</a> · <a href="text-updates.html">Text updates</a> · <a href="mailto:{{EMAIL}}">{{EMAIL}}</a></div>
</div></footer>
</body>
</html>
"""
pages = {}
pages['index.html'] = ("Sharkflow Labs | Websites for local service businesses", "Sharkflow Labs designs fast, conversion-focused websites for roofers, plumbers, landscapers and other local service businesses in the US and UK.", """
<section class="hero"><div class="wrap">
  <h1>Websites that turn local searches into <em>booked jobs</em>.</h1>
  <p>Sharkflow Labs designs fast, mobile-first websites for roofers, plumbers, landscapers, painters and other local service businesses. We build you a free demo first, so you see your new site before you pay anything.</p>
  <a class="btn primary" href="text-updates.html">Get your free demo</a><a class="btn ghost" href="#process">How it works</a>
</div></section>

<section id="services"><div class="wrap">
  <h2>What we do</h2>
  <p class="lead">One small studio, one focus: websites that make your phone ring.</p>
  <div class="grid">
    <div class="card"><h3>Website design</h3><p>A clean, professional site built around your services, service area and reviews, with clear calls to action on every page.</p></div>
    <div class="card"><h3>Local SEO setup</h3><p>Page titles, service-area pages and Google Business Profile tips so nearby customers find you.</p></div>
    <div class="card"><h3>Quote forms that work</h3><p>Lead forms, click-to-call buttons and instant email alerts, so no enquiry slips through.</p></div>
    <div class="card"><h3>Hosting and care</h3><p>Fast hosting, SSL, backups and small updates handled for you, so the site stays live and current.</p></div>
  </div>
</div></section>

<section id="work"><div class="wrap">
  <h2>Concept work</h2>
  <p class="lead">Example designs for the kinds of businesses we work with. These are concept sites for fictional companies.</p>
  <div class="grid work">
    <figure class="card shot"><img src="concept-roofing.jpg" alt="Concept website for a roofing company on desktop and phone" loading="lazy"><figcaption>Roofing</figcaption></figure>
    <figure class="card shot"><img src="concept-hvac.jpg" alt="Concept website for a heating and cooling company on desktop and phone" loading="lazy"><figcaption>Heating &amp; cooling</figcaption></figure>
    <figure class="card shot"><img src="concept-plumbing.jpg" alt="Concept website for a plumbing company on desktop and phone" loading="lazy"><figcaption>Plumbing</figcaption></figure>
  </div>
</div></section>

<section id="process" class="alt"><div class="wrap">
  <h2>How it works</h2>
  <p class="lead">No long calls or sales pitch. You see the work first.</p>
  <div class="grid">
    <div class="card"><div class="num">1</div><h3>Free demo</h3><p>We build a demo homepage for your business using your photos, services and reviews.</p></div>
    <div class="card"><div class="num">2</div><h3>Quick review</h3><p>You look it over and tell us what to change. We can walk through it on a short video call if you like.</p></div>
    <div class="card"><div class="num">3</div><h3>Launch</h3><p>Once you approve the fixed price, we finish every page, connect your domain and go live.</p></div>
  </div>
</div></section>

<section id="contact"><div class="wrap contact">
  <div>
    <h2>Talk to us</h2>
    <p class="lead">Want a free demo of a new website for your business? Email us, or ask for the demo by text.</p>
    <dl>
      <dt>Email</dt><dd><a href="mailto:{{EMAIL}}">{{EMAIL}}</a></dd>
      <dt>Based in</dt><dd>{{CITY}}, India. Serving businesses in the US and UK.</dd>
      <dt>Business</dt><dd>Sharkflow Labs is a brand of {{REGISTERED_NAME}}.</dd>
    </dl>
  </div>
  <div>
    <h3 style="margin-top:0">Get your demo by text</h3>
    <p class="lead" style="margin-bottom:16px">Leave your number and we'll text you the link to your free website demo.</p>
    <p><a class="btn primary" href="text-updates.html">Request by text</a></p>
  </div>
</div></section>
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
  <p>Your website demo link, Google Meet links for calls you agreed to, reminders before those calls, and follow-ups about your demo and pricing. Every message is sent by a person, one at a time. Message frequency varies.</p>
  <h2>How to stop</h2>
  <div class="box">Reply <b>STOP</b> to any message to stop all texts. Reply <b>START</b> to resubscribe. Reply <b>HELP</b> for help, or email <a href="mailto:{{EMAIL}}">{{EMAIL}}</a>. Message and data rates may apply.</div>
  <h2>Your privacy</h2>
  <p>We do not sell or share your phone number or text messaging opt-in data with third parties or affiliates for marketing purposes. Read the full <a href="privacy.html">Privacy Policy</a>.</p>
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
  <p>Sharkflow Labs is a brand of {{REGISTERED_NAME}}, {{CITY}}, India ("we", "us"). This policy explains what we collect when you contact us or use this website, and how we use it.</p>
  <h2>What we collect</h2>
  <p>Business contact details you give us or that are publicly listed for your business: your name, business name, phone number, email address, website and social media profile. We also keep records of our messages and calls with you, including call recordings where we tell you a call may be recorded.</p>
  <h2>How we use it</h2>
  <p>To prepare your website demo, contact you about it, schedule and remind you of calls, provide our services and keep business records. We do not use your information for any unrelated purpose.</p>
  <h2>Text messaging</h2>
  <div class="box">If you agree to receive text messages from Sharkflow Labs, we use your phone number only to send you messages about your website demo, meetings and our services. Message frequency varies. Message and data rates may apply. Reply STOP to opt out or HELP for help. We do not sell or share your phone number or text messaging opt-in data with third parties or affiliates for marketing purposes.</div>
  <h2>Who we share it with</h2>
  <p>Only service providers that help us run the business, such as our phone and messaging provider (Twilio), hosting (Cloudflare) and email. They may only use it to provide their service to us. We do not sell personal information.</p>
  <h2>How long we keep it</h2>
  <p>As long as we are in contact with you, and for up to 2 years after, unless you ask us to delete it sooner or the law requires us to keep it longer.</p>
  <h2>Your choices</h2>
  <p>You can ask us to see, correct or delete your information, or to stop contacting you, at any time by emailing <a href="mailto:{{EMAIL}}">{{EMAIL}}</a>. Reply STOP to any text to stop texts.</p>
  <h2>Contact</h2>
  <p>{{REGISTERED_NAME}} (Sharkflow Labs), {{CITY}}, India. Email <a href="mailto:{{EMAIL}}">{{EMAIL}}</a>.</p>
</div></main>
""")

pages['terms.html'] = ("Terms | Sharkflow Labs", "Terms of service and messaging terms for Sharkflow Labs.", """
<main class="doc"><div class="wrap">
  <h1>Terms</h1>
  <p class="updated">Last updated 22 November 2026</p>
  <p>These terms apply to this website and to services from Sharkflow Labs, a brand of {{REGISTERED_NAME}}, {{CITY}}, India.</p>
  <h2>Demos and projects</h2>
  <p>Website demos are free and come with no obligation. Paid work starts only after you approve a written price and scope. Ownership of the finished website passes to you once it is paid for.</p>
  <h2>Text messaging terms</h2>
  <div class="box">
    <p style="margin-top:0"><b>Program:</b> Sharkflow Labs texts about website demos, meeting links and reminders, and follow-ups about our services, sent only to people who agreed to receive them.</p>
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
        t = t.replace('Sharkflow Labs is a brand of {{REGISTERED_NAME}}, {{CITY}}, India.', 'Based in India, serving the US and UK.')
        t = t.replace('<dt>Business</dt><dd>Sharkflow Labs is a brand of {{REGISTERED_NAME}}.</dd>', '')
        t = t.replace('Sharkflow Labs is a brand of {{REGISTERED_NAME}}, {{CITY}}, India ("we", "us")', 'Sharkflow Labs ("we", "us")')
        t = t.replace('Sharkflow Labs, a brand of {{REGISTERED_NAME}}, {{CITY}}, India', 'Sharkflow Labs')
        t = t.replace('{{REGISTERED_NAME}} (Sharkflow Labs), {{CITY}}, India.', 'Sharkflow Labs, India.')
    t = t.replace('{{REGISTERED_NAME}}', reg or 'Sharkflow Labs').replace('{{EMAIL}}', email)
    t = t.replace('{{CITY}}, India. Serving', (city + ', India. Serving') if city else 'India. Serving').replace('{{CITY}}', city or '')
    assert '{{' not in t, t[t.index('{{')-80:t.index('{{')+80]
    return t
for name, (title, desc, body) in pages.items():
    with open(os.path.join(out, name), 'w') as fh:
        fh.write(fill(HEAD.format(title=title, desc=desc) + body + FOOT))
print('ok')
