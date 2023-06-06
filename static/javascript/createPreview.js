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

function buildResults(receivers, failedReceivers) {
    document.getElementById("resultsContainer").style.display = "block";

    const failedResults = document.getElementById("failedResults");
    const successfulResults = document.getElementById("successfulResults");
    // Create columns
    const varList = getVarList()

    const row1 = document.createElement("tr");
    for (const variable of varList) {
        const column = document.createElement("th");
        column.innerHTML = variable;
        row1.appendChild(column)
    }
    successfulResults.appendChild(row1)
    const row2 = document.createElement("tr");
    for (const variable of varList) {
        const column = document.createElement("th");
        column.innerHTML = variable;
        row2.appendChild(column)
    }
    failedResults.appendChild(row2)
    // Create columns ^^

    // Failed results
    for (const receiver of failedReceivers) {
        const row = document.createElement("tr");
        for (const column of varList) {
            const rowItem = document.createElement("td")
            rowItem.innerHTML = receiver[column]
            row.appendChild(rowItem)
        }
        failedResults.appendChild(row)
    }
    // Successful results
    for (const receiver of receivers) {
        const row = document.createElement("tr");
        for (const column of varList) {
            const rowItem = document.createElement("td")
            rowItem.innerHTML = receiver[column]
            row.appendChild(rowItem)
        }
        successfulResults.appendChild(row)
    }
}