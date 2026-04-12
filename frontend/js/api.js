/**
 * api.js — Puente entre el frontend y el backend Django
 *
 * Este archivo centraliza TODAS las llamadas al API.
 * En vez de escribir fetch() en cada página, lo escribes aquí una sola vez.
 *
 * Cómo usarlo en cualquier página HTML:
 *   <script src="../js/api.js"></script>
 *   <script>
 *     const usuarios = await API.usuarios.listar();
 *   </script>
 */

// ── CONFIGURACIÓN ─────────────────────────────────────────────────────────────
// Cambia esta URL cuando despliegues en Railway
const API_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
  ? 'http://127.0.0.1:8000'        // Desarrollo local
  : 'https://TU-APP.up.railway.app'; // Producción en Railway (cámbiala al desplegar)


// ── FUNCIÓN BASE ──────────────────────────────────────────────────────────────
/**
 * Función genérica para hacer peticiones al API.
 * Todas las funciones de abajo la usan internamente.
 *
 * @param {string} endpoint  - La ruta del API, ej: '/api/usuarios/'
 * @param {string} method    - 'GET', 'POST', 'PUT', 'DELETE'
 * @param {object} body      - Los datos a enviar (solo para POST/PUT)
 * @param {boolean} isForm   - true si estás enviando un archivo (foto)
 */
async function request(endpoint, method = 'GET', body = null, isForm = false) {
  const options = {
    method,
    credentials: 'include', // Envía cookies de sesión (necesario para el admin)
  };

  if (body) {
    if (isForm) {
      // FormData para subir archivos — NO pongas Content-Type, el browser lo hace solo
      options.body = body;
    } else {
      options.headers = { 'Content-Type': 'application/json' };
      options.body = JSON.stringify(body);
    }
  }

  try {
    const response = await fetch(`${API_URL}${endpoint}`, options);

    // Si la respuesta no fue exitosa (4xx o 5xx), lanzamos un error con el detalle
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || `Error ${response.status}`);
    }

    // 204 No Content (ej: al eliminar) no tiene cuerpo JSON
    if (response.status === 204) return null;

    return await response.json();

  } catch (error) {
    // Si es error de red (servidor apagado, sin internet)
    if (error.name === 'TypeError') {
      throw new Error('No se pudo conectar con el servidor. ¿Está corriendo Django?');
    }
    throw error;
  }
}


// ── API DE USUARIOS ────────────────────────────────────────────────────────────
const usuariosAPI = {

  /**
   * Inscribe un nuevo usuario desde el formulario de contacto.
   * Cualquier visitante puede hacer esto (no requiere login).
   *
   * @param {object} datos - { nombre, apellido, email, telefono, edad, programa, fuente, mensaje }
   */
  inscribir(datos) {
    return request('/api/usuarios/', 'POST', datos);
  },

  /**
   * Lista todos los usuarios inscritos.
   * Solo funciona si estás logueado como admin.
   */
  listar() {
    return request('/api/usuarios/');
  },

  /**
   * Obtiene las estadísticas del dashboard.
   * Endpoint: GET /api/usuarios/stats/
   */
  stats() {
    return request('/api/usuarios/stats/');
  },

  /**
   * Activa o desactiva un usuario.
   * @param {number} id
   * @param {boolean} activo
   */
  actualizar(id, datos) {
    return request(`/api/usuarios/${id}/`, 'PATCH', datos);
  },

  eliminar(id) {
    return request(`/api/usuarios/${id}/`, 'DELETE');
  },
};


// ── API DE GALERÍA ─────────────────────────────────────────────────────────────
const galeriaAPI = {

  /**
   * Trae todos los items de la galería.
   * @param {string} tipo - 'foto' o 'video' (opcional para filtrar)
   */
  listar(tipo = null) {
    const query = tipo ? `?tipo=${tipo}` : '';
    return request(`/api/galeria/${query}`);
  },

  /**
   * Sube una foto nueva. Usa FormData porque lleva un archivo.
   * @param {FormData} formData - debe incluir: titulo, descripcion, imagen (File), tipo='foto'
   */
  subirFoto(formData) {
    return request('/api/galeria/', 'POST', formData, true);
  },

  /**
   * Agrega un video de YouTube.
   * @param {object} datos - { titulo, descripcion, url_video, tipo: 'video' }
   */
  agregarVideo(datos) {
    return request('/api/galeria/', 'POST', { ...datos, tipo: 'video' });
  },

  actualizar(id, datos) {
    return request(`/api/galeria/${id}/`, 'PATCH', datos);
  },

  eliminar(id) {
    return request(`/api/galeria/${id}/`, 'DELETE');
  },
};


// ── API DE LINKS ───────────────────────────────────────────────────────────────
const linksAPI = {

  /**
   * Trae todos los links/recursos.
   * @param {string} categoria - filtra por categoría (opcional)
   */
  listar(categoria = null) {
    const query = categoria ? `?categoria=${categoria}` : '';
    return request(`/api/links/${query}`);
  },

  crear(datos) {
    return request('/api/links/', 'POST', datos);
  },

  actualizar(id, datos) {
    return request(`/api/links/${id}/`, 'PATCH', datos);
  },

  eliminar(id) {
    return request(`/api/links/${id}/`, 'DELETE');
  },
};


// ── UTILIDADES DE UI ───────────────────────────────────────────────────────────
/**
 * Muestra un mensaje de éxito o error en la página.
 * Uso: UI.toast('¡Inscripción enviada!', 'success')
 *
 * @param {string} mensaje
 * @param {'success'|'error'|'info'} tipo
 */
const UI = {
  toast(mensaje, tipo = 'info') {
    const colores = {
      success: '#1A8FE3',
      error:   '#e34a1a',
      info:    '#7EC8E3',
    };
    const toast = document.createElement('div');
    toast.textContent = mensaje;
    toast.style.cssText = `
      position: fixed; bottom: 24px; right: 24px; z-index: 9999;
      background: ${colores[tipo]}; color: #fff;
      padding: 14px 24px; border-radius: 10px;
      font-family: Inter, sans-serif; font-size: 14px; font-weight: 500;
      box-shadow: 0 4px 20px rgba(0,0,0,0.3);
      animation: slideIn 0.3s ease;
    `;
    // Animación CSS inline
    if (!document.getElementById('toast-style')) {
      const style = document.createElement('style');
      style.id = 'toast-style';
      style.textContent = `
        @keyframes slideIn  { from { opacity:0; transform:translateY(12px); } to { opacity:1; transform:translateY(0); } }
        @keyframes slideOut { from { opacity:1; transform:translateY(0);    } to { opacity:0; transform:translateY(12px); } }
      `;
      document.head.appendChild(style);
    }
    document.body.appendChild(toast);
    setTimeout(() => {
      toast.style.animation = 'slideOut 0.3s ease forwards';
      setTimeout(() => toast.remove(), 300);
    }, 3500);
  },

  /**
   * Pone un botón en estado de carga (spinner) y lo restaura después.
   * Uso: UI.setLoading(btn, true) / UI.setLoading(btn, false)
   */
  setLoading(btn, loading) {
    if (loading) {
      btn.dataset.originalText = btn.textContent;
      btn.textContent = 'Enviando…';
      btn.disabled = true;
      btn.style.opacity = '0.7';
    } else {
      btn.textContent = btn.dataset.originalText || 'Enviar';
      btn.disabled = false;
      btn.style.opacity = '1';
    }
  },
};


// ── EXPORTAR PARA USO GLOBAL ───────────────────────────────────────────────────
// Esto hace que puedas usar API.usuarios.inscribir() en cualquier página HTML
window.API = {
  usuarios: usuariosAPI,
  galeria:  galeriaAPI,
  links:    linksAPI,
};

window.UI = UI;
