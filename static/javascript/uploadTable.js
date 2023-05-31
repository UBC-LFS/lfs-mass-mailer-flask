var csvData;
function getCSVData() {
    return csvData
}
function buildTable(data) {
    // document.getElementById("uploadFileSection").style.display = "none";
    document.getElementById("writeEmailSection").style.display = "block";
    const columns = document.getElementById("columns");
    for (const column of data["columns"]) {
        const columnLi = document.createElement("th")
        columnLi.innerHTML = column
        columns.appendChild(columnLi)
    }
    const contactTable = document.getElementById("contactTable");
    // console.log(JSON.stringify(data))
    for (const rowData of data) {
        const row = document.createElement("tr");
        for (const column of data["columns"]) {
            const rowItem = document.createElement("td")
            rowItem.innerHTML = rowData[column]
            row.appendChild(rowItem)
        }
        contactTable.appendChild(row);
    }
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
        buildTable(csvData);
    };

    reader.readAsText(input);
});

// const placeholderData = [{"First Name":"Christian","Last Name":"Gage","Email":"donald.lee@ubc.ca"},{"First Name":"Deana","Last Name":"Eartha","Email":"donald.lee@ubc.ca"},{"First Name":"Ricky","Last Name":"Frazier","Email":"donald.lee@ubc.ca"},{"First Name":"Benton","Last Name":"Demelza","Email":"donald.lee@ubc.ca"},{"First Name":"Aden","Last Name":"Branda","Email":"donald.lee@ubc.ca"},{"First Name":"Dorian","Last Name":"Edie","Email":"donald.lee@ubc.ca"},{"First Name":"Meriel","Last Name":"Margie","Email":"donald.lee@ubc.ca"},{"First Name":"Angelina","Last Name":"Daren","Email":"donald.lee@ubc.ca"},{"First Name":"Yolanda","Last Name":"Emmerson","Email":"donald.lee@ubc.ca"}]

// csvData = placeholderData
// buildTable(placeholderData)

