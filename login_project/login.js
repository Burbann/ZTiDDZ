const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");
//Ustawienie zaciągania loginu i hasła na przycisku       <input type="submit" value="Login" id="login-form-submit">
loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;
//Weryfikacja loginu \/
    if (username === "burban" && password === "123") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
        alert("Bad login credentials.");
        loginErrorMsg.style.opacity = 1;
    }
})