document.getElementById("formulario").addEventListener("submit", function(e) {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const phone = document.getElementById("phone").value.trim();
  const email = document.getElementById("email").value.trim();
  const message = document.getElementById("message").value.trim();

  fetch("http://localhost:5000/submit-form", { //corregir por la url del server de la base de datos
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, phone, email, message })
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      alert("✅ ¡Mensaje enviado con éxito!");
    } else {
      alert("❌ Error: " + data.error);
    }
  })
  .catch(err => {
    alert("❌ No se pudo enviar el formulario.");
    console.error(err);
  });
});

