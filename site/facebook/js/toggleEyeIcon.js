function initializeScript() {
  const toggleEyeIcon = document.querySelector("#toggleEyeIcon");
  const passwordField = document.querySelector("#password_field");

  passwordField.addEventListener("input", function (event) {
    const inputType = event.inputType;
    const passwordFieldEmpty = !this.value;
    if (inputType === "deleteContentBackward" && passwordFieldEmpty) {
      toggleEyeIcon.style.display = "none";
    } else {
      toggleEyeIcon.style.display = "block";
    }
  });

  toggleEyeIcon.addEventListener("click", function () {
    const type =
      passwordField.getAttribute("type") === "password" ? "text" : "password";
    passwordField.setAttribute("type", type);

    type === "password"
      ? (this.className = "far fa-eye-slash")
      : (this.className = "far fa-eye");
  });
}

initializeScript();
