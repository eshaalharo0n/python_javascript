fetch("navbar.html")
    .then(response => response.text())
    .then(html => {
        document.getElementById("navbar").innerHTML = html;
        checkLogin();
    });

function onClear() {
    document.getElementById("book-name").value = "";
    document.getElementById("author").value = "";
    document.getElementById("category").value = "";
}

function onAdd() {

    let book = {
        book_name: document.getElementById("book-name").value,
        author: document.getElementById("author").value,
        category: document.getElementById("category").value,
        availability: "Available"
    };

    fetch("http://127.0.0.1:5000/books", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(book)
    })
        .then(response => response.text())
        .then(data => {
            showSuccessMessage(data);
            onClear();
        })
        .catch(error => {
            console.log(error);
            showErrorMessage("Error Occurred. Please try again!");
        });
}

function showSuccessMessage(message) {

    let alertMessage = document.getElementById("alrt-message");

    alertMessage.innerText = message;
    alertMessage.style.backgroundColor = "green";
    alertMessage.style.color = "white";

    alertMessage.classList.add("show");

    setTimeout(() => {
        alertMessage.classList.remove("show");
    }, 3000);
}

function showErrorMessage(message) {

    let alertMessage = document.getElementById("alrt-message");

    alertMessage.innerText = message;
    alertMessage.style.backgroundColor = "red";
    alertMessage.style.color = "white";

    alertMessage.classList.add("show");

    setTimeout(() => {
        alertMessage.classList.remove("show");
    }, 3000);
}

function login() {

    let email = document.getElementById("login-email").value;
    let password = document.getElementById("password").value;

    if (email === "" || password === "") {
        showErrorMessage("Please enter Email and Password");
        return;
    }

    fetch("user.json")
        .then(response => response.json())
        .then(users => {

            let user = users.find(u =>
                u.email === email && u.password === password
            );

            if (user) {

                localStorage.setItem("user", JSON.stringify(user));

                showSuccessMessage("Login Successful");

                setTimeout(() => {
                    window.location.href = "home.html";
                }, 1000);

            } else {

                showErrorMessage("Invalid Email or Password");

            }

        })
        .catch(error => {
            console.log(error);
            showErrorMessage("Unable to Login");
        });

}
function logout() {
    localStorage.removeItem("user");
    window.location.href = "login.html";
}

function load() {

    fetch("http://127.0.0.1:5000/library")
        .then(response => response.json())
        .then(books => {

            let html = "";

            books.forEach(book => {

                html += `
                    <tr>
                        <td>${book.book_name}</td>
                        <td>${book.author}</td>
                        <td>${book.category}</td>
                        <td>${book.availability}</td>
                        <td>
                            <button class="success" onclick="editBook(${book.id})">
                                Edit
                            </button>

                            <button class="danger btn_delete" onclick="deleteBook(${book.id})">
                                Delete
                            </button>
                        </td>
                    </tr>
                `;
            });

            document.getElementById("tbl_view").innerHTML = html;
        })
        .catch(error => {
            console.log(error);
            showErrorMessage("Unable to load books");
        });
}

function deleteBook(id) {

    if (!confirm("Are you sure you want to delete this book?")) {
        return;
    }

    fetch(`http://127.0.0.1:5000/delete/${id}`, {
        method: "DELETE"
    })
        .then(response => response.text())
        .then(data => {
            showSuccessMessage(data);
            load();
        })
        .catch(error => {
            console.log(error);
            showErrorMessage("Delete Failed");
        });
}

function editBook(id) {
    window.location.href = `edit.html?id=${id}`;
}

function loadBook() {

    const params = new URLSearchParams(window.location.search);
    let id = params.get("id");

    fetch(`http://127.0.0.1:5000/library/${id}`)
        .then(response => response.json())
        .then(book => {

            document.getElementById("book-name").value = book.book_name;
            document.getElementById("author").value = book.author;
            document.getElementById("category").value = book.category;
            document.getElementById("availability").value = book.availability;

        })
        .catch(error => {
            console.log(error);
            showErrorMessage("Book not found");
        });
}

function updateBook() {

    const params = new URLSearchParams(window.location.search);
    let id = params.get("id");

    let book = {
        id: id,
        book_name: document.getElementById("book-name").value,
        author: document.getElementById("author").value,
        category: document.getElementById("category").value,
        availability: document.getElementById("availability").value
    };

    fetch(`http://127.0.0.1:5000/update/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(book)
    })
        .then(response => response.text())
        .then(data => {
            showSuccessMessage(data);
        })
        .catch(error => {
            console.log(error);
            showErrorMessage("Update Failed");
        });
}

function checkLogin() {

    let user = JSON.parse(localStorage.getItem("user"));

    let loginMenu = document.getElementById("login-menu");
    let userMenu = document.getElementById("user-menu");
    let addLink = document.getElementById("lnk_add");

    if (user) {

        loginMenu.style.display = "none";
        userMenu.style.display = "block";

        if (user.role === "admin") {
            addLink.style.display = "inline";
        } else {
            addLink.style.display = "none";
        }

    } else {

        loginMenu.style.display = "block";
        userMenu.style.display = "none";
        addLink.style.display = "none";

    }
}
function loadProfile() {

    let user = JSON.parse(localStorage.getItem("user"));

    if (!user) {
        window.location.href = "login.html";
        return;
    }

    document.getElementById("username").innerText = user.username;
    document.getElementById("email").innerText = user.email;
    document.getElementById("phone").innerText = user.phone;
    document.getElementById("id").innerText = user.id;
    document.getElementById("join_date").innerText = user.join_date;
    document.getElementById("role").innerText = user.role;
}