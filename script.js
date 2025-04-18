window.addEventListener('DOMContentLoaded', () => {
    const heure = new Date().getHours();
    const titre = document.querySelector('.accueil h2');
  
    if (heure < 12) {
      titre.textContent = "Bonjour ! Bienvenue sur notre plateforme de recrutement intelligente";
    } else if (heure < 18) {
      titre.textContent = "Bon après-midi ! Bienvenue sur notre plateforme de recrutement intelligente";
    } else {
      titre.textContent = "Bonsoir ! Bienvenue sur notre plateforme de recrutement intelligente";
    }
  
    // Animation visuelle des boutons
    document.querySelectorAll('.btn').forEach(btn => {
      btn.addEventListener('mousedown', () => btn.style.transform = 'scale(0.96)');
      btn.addEventListener('mouseup', () => btn.style.transform = 'scale(1)');
      btn.addEventListener('mouseleave', () => btn.style.transform = 'scale(1)');
    });
  });
  