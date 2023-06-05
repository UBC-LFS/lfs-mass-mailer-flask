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
    document.getElementById("writeEmailSection").style.display = "block";
    const columns = document.getElementById("columns");
    const variablesList = document.getElementById("variablesList")
    
    let rows = 0;
    let validEmails = 0;
    let invalidEmails = 0;

    for (const column of data["columns"]) {
        // Table
        const columnTh = document.createElement("th")
        columnTh.innerHTML = column
        columns.appendChild(columnTh)
        // Variables list
        const columnLi = document.createElement("li")
        columnLi.innerHTML = `%${column.replace(' ', '_').toUpperCase()}%`
        variablesList.appendChild(columnLi)
        varList.push(column)
    }
    const contactTable = document.getElementById("contactTable");
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
        if (rows <= 10) {
            contactTable.appendChild(row);
        }
    }

    if (rows > 10) {
        document.getElementById("rowsDisplayed").innerHTML = 10;
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

// const placeholderData = [{"First Name":"Christian","Last Name":"Gage","Email":"donald.lee@ubc.ca"},{"First Name":"Deana","Last Name":"Eartha","Email":"donald.lee@ubc.ca"},{"First Name":"Ricky","Last Name":"Frazier","Email":"donald.lee@ubc.ca"},{"First Name":"Benton","Last Name":"Demelza","Email":"donald.lee@ubc.ca"},{"First Name":"Aden","Last Name":"Branda","Email":"donald.lee@ubc.ca"},{"First Name":"Dorian","Last Name":"Edie","Email":"donald.lee@ubc.ca"},{"First Name":"Meriel","Last Name":"Margie","Email":"donald.lee@ubc.ca"},{"First Name":"Angelina","Last Name":"Daren","Email":"donald.lee@ubc.ca"},{"First Name":"Yolanda","Last Name":"Emmerson","Email":"donald.lee@ubc.ca"}]

csvData = placeholderData
buildTable(placeholderData)

