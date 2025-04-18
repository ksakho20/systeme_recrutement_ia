document.getElementById('formInscription').addEventListener('submit', function(event) {
  event.preventDefault();
  const data = {
    nom: this.nom.value,
    email: this.email.value,
    societe: this.societe.value,
    motdepasse: this.motdepasse.value
  };
  console.log("Recruteur inscrit :", data);
  document.getElementById('message').innerText = "Inscription réussie ! (Simulation)";
  this.reset();
});