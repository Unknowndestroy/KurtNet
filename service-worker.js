self.addEventListener('install', event => {
    event.waitUntil(
        caches.open('tarayici-cache').then(cache => {
            return cache.addAll([
                '/index.html',
                '/styles.css',
                '/main.js',
                '/manifest.webmanifest'
            ]);
        })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});
