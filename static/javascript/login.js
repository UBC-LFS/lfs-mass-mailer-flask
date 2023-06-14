var sessionID;

function getSessionID() {
    return sessionID;
}

function loginResult(auth) {
    if (auth) {
        document.getElementById("fullLoginContainer").style.display = "none";
        sessionID = auth;
    }
    else {
        document.getElementById("incorrectLoginText").style.display = "block";
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