// Marca el link activo según la página actual
(function () {
  const path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('nav ul li a').forEach(a => {
    const href = a.getAttribute('href').split('/').pop();
    if (href === path) a.classList.add('active');
  });
})();

// Animación de entrada para elementos con data-animate
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('[data-animate]').forEach(el => observer.observe(el));

function switchTab(tab, btn) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  ['photos','videos','links'].forEach(t => {
    document.getElementById('tab-'+t).classList.toggle('hidden', t !== tab);
  });
}

async function cargarFotos() {
  const grid = document.getElementById('photos-grid');
  if (!grid) return;
  try {
    const data = await API.galeria.listar('foto');
    const items = data.results || data;
    if (!items || items.length === 0) return;
    grid.innerHTML = items.map((item, i) => `
      <div class="photo-item ${i === 0 ? 'wide' : ''}">
        ${item.imagen_url
          ? `<img src="${item.imagen_url}" alt="${item.titulo}" loading="lazy">`
          : `<div class="photo-placeholder">🖼️</div>`}
        <div class="photo-overlay"><span class="photo-label">${item.titulo}</span></div>
      </div>
    `).join('');
  } catch (e) {
    console.log('Error cargando fotos:', e.message);
  }
}

async function cargarVideos() {
  const grid = document.getElementById('videos-grid');
  if (!grid) return;
  try {
    const data = await API.galeria.listar('video');
    const items = data.results || data;
    if (!items || items.length === 0) return;
    grid.innerHTML = items.map(item => {
      const ytId = item.url_video?.match(/(?:v=|youtu\.be\/)([^&\n?#]+)/)?.[1];
      return `
        <div class="video-card">
          <div class="video-thumb">
            ${ytId
              ? `<img src="https://img.youtube.com/vi/${ytId}/hqdefault.jpg" alt="${item.titulo}" style="width:100%;height:100%;object-fit:cover;">`
              : `<div class="video-placeholder">🎬</div>`}
            <div class="play-btn" onclick="reproducirVideo('${ytId}', this)">▶</div>
          </div>
          <div class="video-info">
            <h4>${item.titulo}</h4>
            <p>${item.descripcion || ''}</p>
          </div>
        </div>
      `;
    }).join('');
  } catch (e) {
    console.log('Error cargando videos:', e.message);
  }
}

async function cargarLinks() {
  const grid = document.getElementById('links-grid');
  if (!grid) return;
  try {
    const data = await API.links.listar();
    const items = data.results || data;
    if (!items || items.length === 0) return;
    grid.innerHTML = items.map(item => `
      <a href="${item.url}" target="_blank" rel="noopener" class="link-card">
        <div class="link-icon">${item.icono || '🔗'}</div>
        <div>
          <div class="link-title">${item.titulo}</div>
          <div class="link-url">${item.url}</div>
        </div>
        <span class="link-arrow">↗</span>
      </a>
    `).join('');
  } catch (e) {
    console.log('Error cargando links:', e.message);
  }
}

function reproducirVideo(ytId, btn) {
  if (!ytId) return;
  const thumb = btn.parentElement;
  thumb.innerHTML = `<iframe src="https://www.youtube.com/embed/${ytId}?autoplay=1" allowfullscreen allow="autoplay" style="width:100%;height:100%;border:none;"></iframe>`;
}

document.addEventListener('DOMContentLoaded', () => {
  cargarFotos();
  cargarVideos();
  cargarLinks();
});

