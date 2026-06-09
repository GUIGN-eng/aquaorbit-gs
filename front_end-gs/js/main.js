document.addEventListener("DOMContentLoaded", () => {
    // 1. Menu Hambúrguer Funcional
    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.getElementById("navLinks");

    if (menuToggle && navLinks) {
        menuToggle.addEventListener("click", () => {
            navLinks.classList.toggle("active");
        });
    }

    // 2. Acordeon Dinâmico (FAQ)
    const accordionHeaders = document.querySelectorAll(".accordion-header");
    accordionHeaders.forEach(header => {
        header.addEventListener("click", () => {
            const body = header.nextElementSibling;
            body.classList.toggle("active");
        });
    });

    // 3. Validação e Motor de Regras (Simulação do Backend Java)
    const contactForm = document.getElementById("contactForm");
    const feedbackBox = document.getElementById("formFeedback");

    if (contactForm && feedbackBox) {
        contactForm.addEventListener("submit", (e) => {
            e.preventDefault();

            const ph = parseFloat(document.getElementById("phValue").value);
            const turbidez = parseFloat(document.getElementById("turbidezValue").value);
            const cloro = parseFloat(document.getElementById("cloroValue").value);

            // Método 1 do Domínio: avaliarQualidadeAgua()
            const isAprovada = (ph >= 6.0 && ph <= 9.5) && (turbidez <= 5.0) && (cloro >= 0.2 && cloro <= 2.0);

            feedbackBox.classList.remove("hidden", "success-laudo", "danger-laudo");

            // Método 2 & 4: obterResultadoFormatado() & emitirAlertaSeguranca()
            if (isAprovada) {
                feedbackBox.textContent = "Laudo Técnico: APROVADA para consumo. Operação Estável.";
                feedbackBox.classList.add("success-laudo");
            } else {
                feedbackBox.textContent = "ALERTA URGENTE: REPROVADA - Risco à saúde pública. Triagem técnica emergencial necessária!";
                feedbackBox.classList.add("danger-laudo");
            }
        });
    }
});