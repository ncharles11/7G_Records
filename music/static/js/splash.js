document.addEventListener("DOMContentLoaded", function () {
    const splash = document.getElementById("splash-screen");
    const mainContent = document.getElementById("main-content");

    if (!sessionStorage.getItem("splashDisplayed")) {
        splash.style.display = "flex";
        mainContent.style.display = "block";

        setTimeout(() => {
            
            splash.classList.add("hidden");

            setTimeout(() => {
                splash.style.display = "none";
                mainContent.classList.add("visible");
                sessionStorage.setItem("splashDisplayed", "true");
            }, 1000);
        }, 2500); 
    } else {
        splash.style.display = "none";
        mainContent.style.display = "block";
        mainContent.classList.add("visible");
    }
});