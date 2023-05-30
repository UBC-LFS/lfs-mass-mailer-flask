function buildTable(data) {
    // document.getElementById("uploadFileSection").style.display = "none";
    document.getElementById("writeEmailSection").style.display = "block";
    
    const contactTable = document.getElementById("contactTable");
    // console.log(JSON.stringify(data))
    for (let i = 0; i < data.length; i++) {
        const row = document.createElement("tr");
        const firstName = document.createElement("td")
        const lastName = document.createElement("td")
        const email = document.createElement("td")
        firstName.innerHTML = data[i]["First Name"]
        lastName.innerHTML = data[i]["Last Name"]
        email.innerHTML = data[i]["Email"]
        row.appendChild(firstName)
        row.appendChild(lastName)
        row.appendChild(email)
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
      const csvData = d3.csvParse(text);
      buildTable(csvData);
    };

    reader.readAsText(input);
});

const placeholderData = [{"First Name":"Christian","Last Name":"Gage","Email":"example@gmail.com"},{"First Name":"Deana","Last Name":"Eartha","Email":"example@gmail.com"},{"First Name":"Ricky","Last Name":"Frazier","Email":"example@gmail.com"},{"First Name":"Benton","Last Name":"Demelza","Email":"example@gmail.com"},{"First Name":"Aden","Last Name":"Branda","Email":"example@gmail.com"},{"First Name":"Dorian","Last Name":"Edie","Email":"example@gmail.com"},{"First Name":"Meriel","Last Name":"Margie","Email":"example@gmail.com"},{"First Name":"Angelina","Last Name":"Daren","Email":"example@gmail.com"},{"First Name":"Yolanda","Last Name":"Emmerson","Email":"example@gmail.com"}]
buildTable(placeholderData)