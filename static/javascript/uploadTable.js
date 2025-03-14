var csvData;
var varList = []
var previewData;

function getPreviewData() {
    return previewData;
}

function getCSVData() {
    return csvData
}

function getVarList() {
    return varList;
}

function buildTable(data) {
    // document.getElementById("uploadFileSection").style.display = "none";

    // clear existing items first

    varList = []

    document.getElementById("columns").innerHTML=""
    document.getElementById("variablesList").innerHTML=""
    document.getElementById("fileHeaders").innerHTML=""
    document.getElementById("contactTableBody").innerHTML=""

    document.getElementById("writeEmailSection").style.display = "block";
    const columns = document.getElementById("columns");
    const variablesList = document.getElementById("variablesList")
    
    let rows = 0;
    let validEmails = 0;
    let invalidEmails = 0;

    let max_rows = 5;

    for (const column of data["columns"]) {
        // Table
        const columnTh = document.createElement("th")
        columnTh.innerHTML = column
        columns.appendChild(columnTh)
        // Variables list
        
        const columnLi = document.createElement("li");

        // Create a "Copy" button
        const copyButton = document.createElement("button");
        copyButton.textContent = "Copy";

        // Create a span for the text
        const textSpan = document.createElement("span");
        textSpan.textContent = `${column.replace(' ', '_').toUpperCase()}`;
        textSpan.style.marginLeft = "10px"; // Add spacing between text and button
        
        // Copy functionality
        copyButton.addEventListener("click", function () {
            navigator.clipboard.writeText(textSpan.textContent).then(() => {
                console.log("Copied: " + textSpan.textContent);
                copyButton.textContent = "Copied!";
                setTimeout(() => {
                    copyButton.textContent = "Copy";
                }, 500); // Reset after 1.5 seconds
            }).catch(err => {
                console.error("Failed to copy text: ", err);
            });
        });
        

        // Append both elements to the list item
        columnLi.appendChild(copyButton);
        columnLi.appendChild(textSpan);

        // Append the list item to the parent list
        variablesList.appendChild(columnLi);
        varList.push(column)
    }
    const contactTable = document.getElementById("contactTableBody");
    for (const rowData of data) {
        const row = document.createElement("tr");
        for (const column of data["columns"]) {
            const rowItem = document.createElement("td")
            rowItem.innerHTML = rowData[column]
            row.appendChild(rowItem)
            const validEmailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
            if (column.toLowerCase() == "email") {
                if (rowData[column].match(validEmailRegex)) {
                    validEmails += 1;
                }
                else {
                    invalidEmails += 1;
                }
            }
        }
        rows += 1;
        if (rows <= max_rows) {
            contactTable.appendChild(row);
        }
    }

    if (rows > max_rows) {
        document.getElementById("rowsDisplayed").innerHTML = max_rows;
    }
    else {
        document.getElementById("rowsDisplayed").innerHTML = rows;
    }
    // Set summary data
    document.getElementById("totalRows").innerHTML = rows;
    document.getElementById("fileRows").innerHTML = rows;
    document.getElementById("fileHeaders").innerHTML = varList.join(", ");
    document.getElementById("fileValidEmails").innerHTML = validEmails;
    document.getElementById("fileInvalidEmails").innerHTML = invalidEmails;

    // Initializes the data used for the email preview
    previewData = data[0];
}

const form = document.getElementById("uploadTableForm")
const data = document.getElementById("uploadTable")

form.addEventListener("submit", function (e) {
    e.preventDefault() // prevents site from reloading

    const input = data.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        const text = e.target.result;
        csvData = d3.csvParse(text);
        console.log(csvData)
        buildTable(csvData);
    };

    reader.readAsText(input);
});

