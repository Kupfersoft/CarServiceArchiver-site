/* Official Microsoft Store badge graceful fallback (no analytics, no external calls). */
(() => {
  if (!('customElements' in window)) return;
  window.customElements.whenDefined('ms-store-badge').then(() => {
    document.documentElement.classList.add('ms-store-badge-ready');
  });
})();
