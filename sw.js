// Orbe: guarda la app en el teléfono para abrir sin internet.
// La página se pide primero a la red (así siempre ves la última versión);
// si la red no responde rápido o no hay señal, se abre la copia guardada.
var CACHE = "orbe-v2";
var CORE = ["./", "./index.html", "./manifest.webmanifest", "./icons/icon-192.png", "./icons/icon-512.png"];
var NET_WAIT = 3000;

self.addEventListener("install", function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(CORE); }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

function fromNetwork(req, key) {
  return fetch(req).then(function (res) {
    if (res && res.ok) { var copy = res.clone(); caches.open(CACHE).then(function (c) { c.put(key || req, copy); }); }
    return res;
  });
}

self.addEventListener("fetch", function (e) {
  var req = e.request;
  if (req.method !== "GET") return;
  var url = new URL(req.url);

  // La app: red primero, con espera corta; si no, la copia guardada
  if (req.mode === "navigate" || (url.origin === location.origin && /\/(index\.html)?$/.test(url.pathname))) {
    e.respondWith(new Promise(function (resolve) {
      var done = false, net = fromNetwork(req, "./index.html");
      var fallback = function () {
        caches.match("./index.html").then(function (hit) {
          if (done) return;
          if (hit) { done = true; resolve(hit); }
        });
      };
      var timer = setTimeout(fallback, NET_WAIT);
      net.then(function (res) { clearTimeout(timer); if (!done) { done = true; resolve(res); } })
        .catch(function () {
          clearTimeout(timer);
          caches.match("./index.html").then(function (hit) { if (!done) { done = true; resolve(hit || Response.error()); } });
        });
    }));
    return;
  }

  // Íconos y archivos propios: copia guardada y se actualiza por detrás
  if (url.origin === location.origin && !/tasa\.json/.test(url.pathname)) {
    e.respondWith(caches.match(req).then(function (hit) {
      var net = fromNetwork(req).catch(function () { return hit; });
      return hit || net;
    }));
    return;
  }

  // Tipografía de Google: se guarda la primera vez y luego sale del teléfono
  if (url.host === "fonts.googleapis.com" || url.host === "fonts.gstatic.com") {
    e.respondWith(caches.match(req).then(function (hit) {
      return hit || fetch(req).then(function (res) {
        if (res && res.ok) { var copy = res.clone(); caches.open(CACHE).then(function (c) { c.put(req, copy); }); }
        return res;
      });
    }));
  }
  // Tasas y demás servicios externos: siempre a la red (la app ya guarda la última tasa)
});
