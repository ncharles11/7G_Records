document.addEventListener("DOMContentLoaded", function() {
    const cards = document.querySelectorAll(".artist-card");
    console.log("Cartes détectées :", cards.length);

    cards.forEach(card => {
        card.addEventListener("click", () => {
            console.log("Flip déclenché pour :", card);
            card.classList.toggle("flipped");
        });

        // Empêche le flip quand on clique sur les liens
        card.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', e => e.stopPropagation());
        });
    });
});