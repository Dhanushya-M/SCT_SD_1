function convert() {
    const temperature = document.getElementById("temperature").value;
    const scaleFrom = document.getElementById("from").value;
    const scaleTo = document.getElementById("to").value;

    fetch("/convert", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            temperature: temperature,
            from: scaleFrom,
            to: scaleTo
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            document.getElementById("result").innerText = data.result;
        }
    })
    .catch(error => console.error(error));
}

function resetForm() {
    document.getElementById("temperature").value = "";
    document.getElementById("from").value = "Celsius";
    document.getElementById("to").value = "Fahrenheit";
    document.getElementById("result").innerText = "";
}
