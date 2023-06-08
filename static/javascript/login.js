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