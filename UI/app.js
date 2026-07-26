fetch ("navbar.html")
.then(response => response.text())
.then((html) =>{
     document.getElementById("navbar").innerHTML = html;
checklogin();
})
function onClear(){
    document.getElementById("book-name").value = "";
    document.getElementById("author").value = "";
    document.getElementById("category").value = "";
    document.getElementById("available").value ="";
    showErrorMessage("Form Cleared Successfully");
}
function onAdd(){
    let bookName = document.getElementById("book-name").value;
    let authorName = document.getElementById("author").value;
    let category = document.getElementById("category").value;
    showSuccessMessage("Book Added Successfully");

}
function showSuccessMessage(message) {
    let alrtMessage = document.getElementById("alrt-message");
    alrtMessage.innerText = message;
    alrtMessage.style.backgroundColor = "#4CAF50";
    alrtMessage.style.color = "white";
    alrtMessage.classList.add("show")
    setTimeout(function(){
       alrtMessage.classList.remove("show"); }
      , 3000 );
}
function showErrorMessage(message) {
    let alrtMessage = document.getElementById("alrt-message");
    alrtMessage.innerText = message;
    alrtMessage.style.backgroundColor = "#FF9800";
    alrtMessage.style.color = "white";
    alrtMessage.classList.add("show")
    setTimeout(function(){
         alrtMessage.classList.remove("show"); }
        , 3000 );
}

function showUpdate(message) {
    let toast = document.getElementById("edit_toast");

    toast.innerText = message;
    toast.style.color = "white";
    toast.style.backgroundColor = "green";

    toast.classList.add("show");

    setTimeout(function () {
        toast.classList.remove("show");
    }, 3000);
}
function login() {
    let email = document.getElementById("login-email").value;
    let password = document.getElementById("password").value;

    if (email === "" || password === "") {
        showErrorMessage("Please enter Email and Password");
    }
    else {
        localStorage.setItem("login", "true")
        showSuccessMessage("Login Successful!");

        setTimeout(function () {
            document.getElementById("alrt-message").classList.remove("show");
        }, 2000);
    }
}


function checklogin() {
    let loginstatus = localStorage.getItem("login");
    if (loginstatus == "true"){
        document.getElementById("login-menu").style.display ="none";
        document.getElementById("user-menu").style.display = "block"
    }
    else{
        document.getElementById("login-menu").style.display = "block";
        document.getElementById("user-menu").style.display = "none"
    }
}
function logout(){
    localStorage.removeItem("login");
    window.location.href = "login.html";
}





