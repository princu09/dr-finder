$(document).ready(function() {

    username = document.querySelector("#usrname");
    usernameAlert = document.querySelector(".username-alert");
    usernameAlert.classList.remove("show")

    username.addEventListener("keyup", (e) => {
        const usrnameVal = e.target.value;

        usernameAlert.classList.remove("show")
        username.classList.remove("is-invalid");
        if (usrnameVal.length > 3) {
            fetch("authenticate-username", {
                body: JSON.stringify({ username: usrnameVal }),
                method: "POST",
            }).then(res => res.json()).then(data => {
                if (data.username_error) {
                    username.classList.add("is-invalid");
                    usernameAlert.classList.add("show")
                }
            });
        }
    });
});