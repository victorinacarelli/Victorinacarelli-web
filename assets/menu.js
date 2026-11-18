/* Menú hamburguesa (mobile) */
(function(){
  const b=document.getElementById("burger"), m=document.getElementById("mmenu");
  if(!b||!m) return;
  function set(open){
    m.hidden=!open; b.setAttribute("aria-expanded",open);
    b.setAttribute("aria-label",open?"Cerrar menú":"Abrir menú");
    document.documentElement.classList.toggle("menu-open",open);
  }
  b.addEventListener("click",()=>set(m.hidden));
  m.addEventListener("click",e=>{ if(e.target.closest("a")) set(false); });
  document.addEventListener("keydown",e=>{ if(e.key==="Escape"&&!m.hidden){ set(false); b.focus(); } });
  window.matchMedia("(min-width:960px)").addEventListener("change",e=>{ if(e.matches) set(false); });
})();
