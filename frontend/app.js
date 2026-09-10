const serviceIcons = ["☁", "⚙", "♢", "▥", "↗", "◌", "◈", "✦"];

async function loadServices() {
  const grid = document.getElementById("service-grid");

  try {
    const response = await fetch("/api/services");

    if (!response.ok) {
      throw new Error(`API returned ${response.status}`);
    }

    const services = await response.json();

    grid.innerHTML = services.map((service, index) => `
      <article class="service-card">
        <div class="service-icon">${serviceIcons[index % serviceIcons.length]}</div>
        <div>
          <h3>${escapeHtml(service.name)}</h3>
          <p>${escapeHtml(service.description)}</p>
        </div>
      </article>
    `).join("");
  } catch (error) {
    console.error("Unable to load services:", error);

    grid.innerHTML = `
      <div class="loading">
        Services are temporarily unavailable. Please try again shortly.
      </div>
    `;
  }
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

const form = document.getElementById("contact-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const status = document.getElementById("form-status");
  const data = Object.fromEntries(new FormData(form));

  status.textContent = "Sending your enquiry…";

  try {
    const response = await fetch("/api/enquiries", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();

    if (!response.ok) {
      throw new Error(result.error || "Unable to send enquiry.");
    }

    form.reset();
    status.textContent = "Thank you. Your enquiry has been received.";
  } catch (error) {
    console.error(error);
    status.textContent = error.message;
  }
});

loadServices();
