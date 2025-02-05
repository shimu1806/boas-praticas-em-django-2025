class MobileNavbar {
    constructor(mobileMenu, navList, navLinks) {
      this.mobileMenu = document.querySelector(mobileMenu);
      this.navList = document.querySelector(navList);
      this.navLinks = document.querySelectorAll(navLinks);
      this.activeClass = "active";
  
      this.handleClick = this.handleClick.bind(this);
    }
  
    animateLinks() {
      this.navLinks.forEach((link, index) => {
        link.style.animation
          ? (link.style.animation = "")
          : (link.style.animation = `navLinkFade 0.5s ease forwards ${
              index / 7 + 0.3
            }s`);
      });
    }
  
    handleClick() {
      this.navList.classList.toggle(this.activeClass);
      this.mobileMenu.classList.toggle(this.activeClass);
      this.animateLinks();
    }
  
    addClickEvent() {
      this.mobileMenu.addEventListener("click", this.handleClick);
    }
  
    init() {
      if (this.mobileMenu) {
        this.addClickEvent();
      }
      return this;
    }
    

}
function onSubmit(token) {
document.getElementById("demo-form").submit();
}


document.getElementById("id_sendEmail").addEventListener("click", function() {
	sendEmail();
});


function sendEmail() {
const casa = "Garibaldi"
  let parms = {
    name: document.getElementById("name").value.trim(),
    phone: document.getElementById("phone").value.trim(),
    email: document.getElementById("email").value.trim(),
    message: document.getElementById("message").value.trim(),
    casa : casa
  };

  let recaptchaResponse = grecaptcha.getResponse();
  if (!recaptchaResponse) {
    alert("Conferma di non essere un robot.");
    return;
  }

  // Verifica se algum campo está vazio
  if (!parms.name || !parms.email || !parms.message) {
    alert("Compila tutti i campi obbligatori!");
    return;
  }

  // Verifica se já houve um envio recente
  const lastSent = localStorage.getItem("lastSent");
  const now = new Date().getTime();
  if (lastSent && now - lastSent < 60000) { // 60 segundos
    alert("Attendere un minuto prima di inviare nuovamente.");
    return;
  }

  // Validação do e-mail
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(parms.email)) {
    alert("Indirizzo email non valido!");
    return;
  }

const serviceID = "service_li3mkbm";
const templateID = "template_f3df0v1";

try {
  console.log("Invio in corso...", parms);
  alert("Stiamo ricevendo il tuo messaggio!");

  emailjs.send(serviceID, templateID, parms, {
  headers: {
    "Content-Type": "application/json"
  }
      
  }).then(
  (response) => {
    try {
      console.log("SUCCESSO! Stato:", response.status, "Messaggio:", response.text);
      localStorage.setItem("lastSent", now); // Salva o tempo do último envio
      alert("Email inviata con successo!");
      grecaptcha.reset(); // Reseta o reCAPTCHA após o envio
    } catch (err) {
      console.error("Errore imprevisto nella gestione della risposta:", err);
      alert("Si è verificato un errore durante l'elaborazione della risposta.");
    }
      },
      (error) => {
        console.log("ERRORE durante l'invio:", error);
        alert("Errore durante l'invio dell'email.");
      }
    );
  } catch (err) {
    console.error("Errore imprevisto:", err);
    alert("Si è verificato un errore inaspettato.");
  }
}

  