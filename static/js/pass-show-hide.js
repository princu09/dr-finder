var toogleBtn = document.querySelector(".field i");
var passField = document.querySelector(".field input[type='password']");

toogleBtn.onclick = () => {
    if (passField.type == "password") {
        passField.type = "text";
        toogleBtn.classList.add("active");
    } else {
        passField.type = "password";
        toogleBtn.classList.remove("active");
    }
}