var sessionID;

function getSessionID() {
    return sessionID;
}

function logout() {
    document.cookie = "sessionID=null; path=/;";
    $.ajax({
        type: "POST",
        url: "/logout",
        data: {"data": getSessionID()},
        dataType: "json"
    })
    location.reload()
}

function checkSessionID() {
    let cookie = decodeURIComponent(document.cookie);
    let ca = cookie.split(';');
    sessionID = ca[0].split("=")[1];
    if (sessionID == "null") {
        document.getElementById("fullLoginContainer").style.display = "block";
    }
}

checkSessionID()

function loginResult(auth) {
    if (auth) {
        document.getElementById("fullLoginContainer").style.display = "none";
        sessionID = auth;
        document.cookie = "sessionID=" + sessionID + "; path=/";
    }
    else {
        document.getElementById("incorrectLoginText").style.display = "block";
        document.cookie = "sessionID=null; path=/;";
    }
}

// Execute a function when the user presses a key on the keyboard
document.getElementById("cwl").addEventListener("keypress", function(event) {
    // If the user presses the "Enter" key on the keyboard
    if (event.key === "Enter") {
      // Cancel the default action, if needed
      event.preventDefault();
      login()
    }
});

// Execute a function when the user presses a key on the keyboard
document.getElementById("password").addEventListener("keypress", function(event) {
    // If the user presses the "Enter" key on the keyboard
    if (event.key === "Enter") {
      // Cancel the default action, if needed
      event.preventDefault();
      login()
    }
  });