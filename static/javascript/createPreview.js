function previewEmail(open) {
    if (open) {
        document.getElementById("previewEmailContainer").style.display = "block";
        document.getElementById("previewEmailTint").style.display = "block";
    }
    else {
        document.getElementById("previewEmailContainer").style.display = "none";
        document.getElementById("previewEmailTint").style.display = "none";
    }
}