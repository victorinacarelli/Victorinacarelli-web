#!/usr/bin/env python3
"""Genera el archivo para importar en Google Tag Manager (Admin → Importar contenedor).

Uso:  python3 tools/gtm_container.py GTM-XXXX G-XXXX 1234567890 > gtm-victorinacarelli.json
(el ID del Pixel es opcional; sin él, el contenedor solo trae GA4)

Qué arma:
- Google tag (GA4) en todas las páginas. Respeta el modo de consentimiento que define assets/tracking.js.
- Evento GA4 por cada conversión que manda el sitio al dataLayer (ver assets/tracking.js).
- Meta Pixel: PageView, Lead (formulario) y Contact (WhatsApp / mail), solo si la persona aceptó cookies.
"""
import json, sys, datetime

EVENTS = ["generate_lead", "contact_whatsapp", "copy_email", "contact_email", "cta_click", "social_click"]
PARAMS = ["link_location", "social_network", "link_url", "cta_text", "cta_location", "service", "form_id", "page_path"]


def t(key, value, typ="TEMPLATE"):
    return {"type": typ, "key": key, "value": value}


def main(gtm_id, ga_id, pixel_id=None):
    ids = iter(range(1, 1000))
    nid = lambda: str(next(ids))
    variables, triggers, tags = [], [], []

    for p in PARAMS + ["consent_state"]:
        variables.append({"variableId": nid(), "name": "dlv - " + p, "type": "v", "parameter": [
            t("dataLayerVersion", "2", "INTEGER"), t("setDefaultValue", "false", "BOOLEAN"), t("name", p)]})

    def custom_event(name, regex, consent=False):
        tr = {"triggerId": nid(), "name": name, "type": "CUSTOM_EVENT", "customEventFilter": [
            {"type": "MATCH_REGEX", "parameter": [t("arg0", "{{_event}}"), t("arg1", regex)]}]}
        if consent:
            tr["filter"] = [{"type": "EQUALS", "parameter": [t("arg0", "{{dlv - consent_state}}"), t("arg1", "granted")]}]
        triggers.append(tr)
        return tr["triggerId"]

    tr_conv = custom_event("Conversiones del sitio", "^(" + "|".join(EVENTS) + ")$")

    tags.append({"tagId": nid(), "name": "GA4 - Google tag", "type": "googtag",
                 "parameter": [t("tagId", ga_id)],
                 "firingTriggerId": ["2147479573"],  # Initialization - All Pages
                 "tagFiringOption": "ONCE_PER_EVENT"})
    tags.append({"tagId": nid(), "name": "GA4 - Conversiones", "type": "gaawe",
                 "parameter": [
                     t("sendEcommerceData", "false", "BOOLEAN"),
                     t("eventName", "{{Event}}"),
                     t("measurementIdOverride", ga_id),
                     {"type": "LIST", "key": "eventSettingsTable", "list": [
                         {"type": "MAP", "map": [t("parameter", p), t("parameterValue", "{{dlv - %s}}" % p)]}
                         for p in PARAMS]},
                 ],
                 "firingTriggerId": [tr_conv], "tagFiringOption": "ONCE_PER_EVENT"})

    if pixel_id:
        tr_ok = custom_event("Cookies aceptadas", "^consent_update$", consent=True)
        tr_lead = custom_event("Formulario enviado (con cookies)", "^generate_lead$", consent=True)
        tr_contact = custom_event("WhatsApp o mail (con cookies)", "^(contact_whatsapp|copy_email|contact_email)$", consent=True)
        base = ("<script>!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?"
                "n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;"
                "n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];"
                "s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');"
                "fbq('init','%s');fbq('track','PageView');</script>" % pixel_id)
        for name, html, trig in [
            ("Meta Pixel - Base", base, tr_ok),
            ("Meta Pixel - Lead", "<script>if(window.fbq)fbq('track','Lead');</script>", tr_lead),
            ("Meta Pixel - Contact", "<script>if(window.fbq)fbq('track','Contact');</script>", tr_contact),
        ]:
            tags.append({"tagId": nid(), "name": name, "type": "html",
                         "parameter": [t("html", html), t("supportDocumentWrite", "false", "BOOLEAN")],
                         "firingTriggerId": [trig], "tagFiringOption": "ONCE_PER_LOAD" if "Base" in name else "ONCE_PER_EVENT"})

    out = {
        "exportFormatVersion": 2,
        "exportTime": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "containerVersion": {
            "path": "accounts/0/containers/0/versions/0", "accountId": "0", "containerId": "0", "containerVersionId": "0",
            "container": {"path": "accounts/0/containers/0", "accountId": "0", "containerId": "0",
                          "name": "victorinacarelli.com.ar", "publicId": gtm_id, "usageContext": ["WEB"]},
            "tag": tags, "trigger": triggers, "variable": variables,
            "builtInVariable": [{"type": "EVENT", "name": "Event"}, {"type": "PAGE_URL", "name": "Page URL"},
                                {"type": "PAGE_PATH", "name": "Page Path"}, {"type": "REFERRER", "name": "Referrer"}],
        },
    }
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(*sys.argv[1:4])
