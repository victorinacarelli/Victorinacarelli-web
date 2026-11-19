/* Analítica: Google Tag Manager + modo de consentimiento + banner de cookies + eventos de conversión.
   Para cambiar herramientas (GA4, Meta Pixel, etc.) se usa Tag Manager, no este archivo.
   Solo hay que tocar acá el ID del contenedor. */
(function(){
  var GTM_ID = "GTM-WSXQKMH6"; // ej. "GTM-ABC1234". Vacío = no carga Tag Manager (solo el banner, para pruebas).
  var KEY = "victo-consent";

  var w = window, d = document;
  w.dataLayer = w.dataLayer || [];
  function gtag(){ w.dataLayer.push(arguments); }
  w.gtag = w.gtag || gtag;

  /* 1) Todo arranca denegado hasta que la persona acepte. */
  gtag("consent", "default", {
    analytics_storage: "denied", ad_storage: "denied",
    ad_user_data: "denied", ad_personalization: "denied",
    functionality_storage: "granted", security_storage: "granted",
    wait_for_update: 500
  });

  var saved = null;
  try { saved = JSON.parse(localStorage.getItem(KEY) || "null"); } catch(e){}
  function apply(state, fromClick){
    var g = state === "granted" ? "granted" : "denied";
    gtag("consent", "update", { analytics_storage: g, ad_storage: g, ad_user_data: g, ad_personalization: g });
    w.dataLayer.push({ event: "consent_update", consent_state: g, consent_from_click: !!fromClick });
  }
  if (saved && saved.s) apply(saved.s, false);

  /* 2) Tag Manager */
  if (GTM_ID) {
    w.dataLayer.push({ "gtm.start": new Date().getTime(), event: "gtm.js" });
    var s = d.createElement("script"); s.async = true;
    s.src = "https://www.googletagmanager.com/gtm.js?id=" + GTM_ID;
    d.head.appendChild(s);
  }

  /* 3) Eventos de conversión (se mandan a GA4 / Pixel desde Tag Manager) */
  function track(name, params){
    var o = { event: name }; for (var k in params) o[k] = params[k];
    w.dataLayer.push(o);
  }
  w.victoTrack = track;
  function where(el){
    if (el.closest(".top")) return "header";
    if (el.closest(".ctx")) return "bio_menu";
    var sec = el.closest("section[id]"); if (sec) return sec.id;
    var art = el.closest("[id]"); if (art) return art.id;
    return "page";
  }
  function label(el){ return (el.textContent || "").replace(/\s+/g, " ").replace(/[→↗]/g, "").trim().slice(0, 60); }
  d.addEventListener("click", function(e){
    var el = e.target.closest && e.target.closest("a,button"); if (!el) return;
    if (el.closest("#cookie-banner")) return;
    var href = el.getAttribute("href") || "", loc = where(el), path = location.pathname;
    if (el.hasAttribute("data-copy")) return track("copy_email", { link_location: loc, page_path: path });
    if (/wa\.me|whatsapp/.test(href)) return track("contact_whatsapp", { link_location: loc, page_path: path });
    if (/^mailto:/.test(href)) return track("contact_email", { link_location: loc, page_path: path });
    var net = /instagram\.com/.test(href) ? "instagram" : /linkedin\.com/.test(href) ? "linkedin" : /behance\.net/.test(href) ? "behance" : "";
    if (net) return track("social_click", { social_network: net, link_url: href, link_location: loc, page_path: path });
    if (/#contacto$/.test(href)) return track("cta_click", { cta_text: label(el), cta_location: loc, service: el.getAttribute("data-need") || "", page_path: path });
  }, true);

  /* 4) Banner de cookies */
  var TXT = {
    es: { title: "cookies.txt", body: "Uso cookies para medir visitas.", ok: "Aceptar", no: "No", pref: "Cookies" },
    en: { title: "cookies.txt", body: "I use cookies to measure visits.", ok: "Accept", no: "No", pref: "Cookies" }
  };
  function lang(){ return (d.documentElement.lang || "es").slice(0,2) === "en" ? "en" : "es"; }
  var CSS =
    /* Barra fina abajo: una línea de texto + Aceptar / No */
    "#cookie-banner{position:fixed;z-index:60;left:max(12px,env(safe-area-inset-left,0px));right:max(12px,env(safe-area-inset-right,0px));bottom:max(12px,env(safe-area-inset-bottom,0px));" +
      "max-width:460px;display:flex;align-items:center;gap:10px;padding:8px 8px 8px 16px;background:var(--surface,#fff);color:var(--ink,#3A1C14);" +
      "border:1.5px solid var(--ink,#3A1C14);border-radius:999px;font:400 13.5px/1.3 var(--font-body,system-ui,sans-serif);" +
      "animation:cb-in .35s cubic-bezier(.2,.9,.3,1.2) both}" +
    "@keyframes cb-in{from{opacity:0;transform:translateY(16px)}}" +
    "@media (prefers-reduced-motion:reduce){#cookie-banner{animation:none}}" +
    "#cookie-banner p{margin:0;flex:1;min-width:0}" +
    "@media (min-width:600px){#cookie-banner{right:auto;gap:16px}}" +
    "#cookie-banner .cb-btns{display:flex;gap:6px;flex:none}" +
    "#cookie-banner button{font:600 13.5px/1 var(--font-body,system-ui,sans-serif);border-radius:999px;padding:9px 14px;border:1.5px solid var(--ink,#3A1C14);cursor:pointer;white-space:nowrap;transition:transform .15s,box-shadow .15s}" +
    "#cookie-banner .cb-ok{background:var(--ink,#3A1C14);color:var(--bg,#FDF8F1)}" +
    "#cookie-banner .cb-no{background:transparent;color:var(--ink,#3A1C14)}" +
    "@media (hover:hover){#cookie-banner button:hover{transform:translate(-2px,-2px);box-shadow:3px 3px 0 var(--naranja,#FF6B2C)}}" +
    ".cb-pref{font:inherit;color:inherit;background:none;border:0;padding:0;text-decoration:underline;text-underline-offset:3px;cursor:pointer;opacity:.9}";

  function closeBanner(){ var b = d.getElementById("cookie-banner"); if (b) b.remove(); }
  function choose(state){
    try { localStorage.setItem(KEY, JSON.stringify({ s: state, t: Date.now() })); } catch(e){}
    apply(state, true); closeBanner();
  }
  function openBanner(){
    if (d.getElementById("cookie-banner")) return;
    var t = TXT[lang()];
    var b = d.createElement("div");
    b.id = "cookie-banner"; b.setAttribute("role", "dialog"); b.setAttribute("aria-live", "polite"); b.setAttribute("aria-label", "Cookies");
    b.innerHTML = '<p>' + t.body + '</p>' +
      '<div class="cb-btns"><button type="button" class="cb-ok">' + t.ok + '</button><button type="button" class="cb-no">' + t.no + '</button></div>';
    b.querySelector(".cb-ok").addEventListener("click", function(){ choose("granted"); });
    b.querySelector(".cb-no").addEventListener("click", function(){ choose("denied"); });
    d.body.appendChild(b);
  }
  function init(){
    var st = d.createElement("style"); st.textContent = CSS; d.head.appendChild(st);
    /* Sin ID de Tag Manager no hay nada que consentir: no se muestra el banner (salvo ?cookies=1 para probarlo). */
    if (!GTM_ID && !/[?&]cookies=1/.test(location.search)) return;
    var foot = d.querySelector("main footer, .mini-foot, footer");
    if (foot) {
      var p = d.createElement("button"); p.type = "button"; p.className = "cb-pref"; p.textContent = TXT[lang()].pref;
      p.addEventListener("click", openBanner); foot.appendChild(p);
    }
    if (!saved || !saved.s) {
      openBanner();
    }
    /* Si cambia el idioma con el banner abierto, lo re-dibujo. */
    new MutationObserver(function(){
      var b = d.getElementById("cookie-banner"); if (b) { b.remove(); openBanner(); }
    }).observe(d.documentElement, { attributes: true, attributeFilter: ["lang"] });
  }
  if (d.readyState === "loading") d.addEventListener("DOMContentLoaded", init); else init();
})();
