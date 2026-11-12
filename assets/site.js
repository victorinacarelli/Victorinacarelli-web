/* Shared script for the service detail pages: language toggle and "Quiero esta" preselection. */
(function(){
  const COMMON = {
    es:{nav_portfolio:"Portfolio",nav_services:"Servicios",nav_bio:"Sobre mí",nav_contact:"Contacto",cta_short:"Presupuesto",
        crumb_home:"Inicio",crumb_services:"Servicios",foot:"Diseñado con amor (y muchos post-its)",sample:"Textos de ejemplo"},
    en:{nav_portfolio:"Work",nav_services:"Services",nav_bio:"About",nav_contact:"Contact",cta_short:"Get a quote",
        crumb_home:"Home",crumb_services:"Services",foot:"Designed with love (and lots of sticky notes)",sample:"Sample copy"}
  };
  const PAGE = window.PAGE_T || {es:{},en:{}};
  function t(l,k){ return (PAGE[l] && PAGE[l][k]!==undefined) ? PAGE[l][k] : COMMON[l][k]; }
  function setLang(l){
    document.documentElement.lang = l;
    document.querySelectorAll("[data-i18n]").forEach(el=>{const v=t(l,el.dataset.i18n); if(typeof v==="string") el.textContent=v;});
    document.querySelectorAll("[data-i18n-html]").forEach(el=>{const v=t(l,el.dataset.i18nHtml); if(typeof v==="string") el.innerHTML=v;});
    document.querySelectorAll(".lang button").forEach(b=>b.setAttribute("aria-pressed", String(b.dataset.lang===l)));
    const title = t(l,"page_title"); if(title) document.title = title;
    try{localStorage.setItem("victo-lang", l)}catch(e){}
  }
  document.querySelectorAll(".lang button").forEach(b=>b.addEventListener("click",()=>setLang(b.dataset.lang)));
  document.querySelectorAll("[data-need]").forEach(a=>a.addEventListener("click",()=>{ try{localStorage.setItem("victo-need", a.dataset.need)}catch(e){} }));
  let saved=null; try{saved=localStorage.getItem("victo-lang")}catch(e){}
  setLang(saved==="en"?"en":"es");
})();
