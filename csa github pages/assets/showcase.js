/* Car Service Archiver native screenshot galleries: no external resources */
(()=>{
  const section=document.querySelector('[data-showcase]');
  if(section){
    const thumbnails=[...section.querySelectorAll('[data-shot]')];
    const image=section.querySelector('[data-main-image]');
    const link=section.querySelector('[data-main-link]');
    const title=section.querySelector('[data-current-name]');
    const number=section.querySelector('[data-current-num]');
    const prev=section.querySelector('[data-prev]');
    const next=section.querySelector('[data-next]');
    let current=0;
    function select(i){
      current=(i+thumbnails.length)%thumbnails.length;
      const target=thumbnails[current], thumb=target.querySelector('img');
      image.src=target.href;
      image.alt=target.getAttribute('aria-label');
      link.href=target.href;
      title.textContent=target.querySelector('span').textContent;
      number.textContent=String(current+1).padStart(2,'0');
      thumbnails.forEach((t,j)=>{t.classList.toggle('is-selected',j===current);if(j===current)t.setAttribute('aria-current','true');else t.removeAttribute('aria-current');});
    }
    thumbnails.forEach((t,i)=>t.addEventListener('click',e=>{e.preventDefault();select(i)}));
    prev.hidden=false;next.hidden=false;
    prev.addEventListener('click',()=>select(current-1));
    next.addEventListener('click',()=>select(current+1));
  }
  const gallery=document.querySelector('[data-gallery]');
  const modal=document.querySelector('[data-gallery-dialog]');
  if(!gallery||!modal||typeof modal.showModal!=='function')return;
  const entries=[...gallery.querySelectorAll('[data-gallery-item]')];
  const viewer=modal.querySelector('[data-dialog-image]');
  const caption=modal.querySelector('[data-dialog-caption]');
  const count=modal.querySelector('[data-dialog-count]');
  let index=0;
  function show(i){
    index=(i+entries.length)%entries.length;
    const entry=entries[index],img=entry.querySelector('img');
    viewer.src=entry.href;viewer.alt=img.alt;
    caption.textContent=entry.querySelector('.gallery-card-name').textContent.trim().replace('↗','').trim();
    count.textContent=String(index+1).padStart(2,'0')+' / '+String(entries.length).padStart(2,'0');
  }
  entries.forEach((entry,i)=>entry.addEventListener('click',e=>{e.preventDefault();show(i);modal.showModal();}));
  modal.querySelector('[data-dialog-close]').addEventListener('click',()=>modal.close());
  modal.querySelector('[data-dialog-prev]').addEventListener('click',()=>show(index-1));
  modal.querySelector('[data-dialog-next]').addEventListener('click',()=>show(index+1));
  modal.addEventListener('click',e=>{if(e.target===modal)modal.close()});
  document.addEventListener('keydown',e=>{if(!modal.open)return;if(e.key==='ArrowRight'){e.preventDefault();show(index+1)}else if(e.key==='ArrowLeft'){e.preventDefault();show(index-1)}});
  modal.addEventListener('close',()=>{viewer.removeAttribute('src')});
})();
