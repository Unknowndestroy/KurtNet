// Güvenlik için varsayılan ayarlar
(function secureDefaults() {
    // WebRTC sızıntılarını engelle
    if (typeof RTCDataChannel !== "undefined") {
        const origOpen = RTCDataChannel.prototype.open;
        RTCDataChannel.prototype.open = function () {
            console.warn('WebRTC sızıntısı engellendi');
            return null;
        };
    }

    // Üçüncü taraf çerezleri engelle
    document.cookie = "SameSite=Strict; Secure";
})();

// Hata raporlama işlevi
function sendErrorReport() {
    // Hata verilerini toplama
    const errorData = {
        timestamp: new Date().toISOString(),
        browserVersion: navigator.userAgent,
        errors: "Örnek hata mesajı"
    };

    // Verileri KurtNet'e gönderme
    fetch('https://kurtnet.com/api/error-report', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(errorData)
    })
    .then(response => alert("Hata verileri başarıyla gönderildi."))
    .catch(error => console.error("Hata raporu gönderilemedi:", error));
}

// PWA için servis çalışanı kaydı
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/service-worker.js')
            .then(reg => console.log('Servis çalışanı başarıyla kayıt edildi:', reg))
            .catch(err => console.log('Servis çalışanı kaydı başarısız:', err));
    });
}
