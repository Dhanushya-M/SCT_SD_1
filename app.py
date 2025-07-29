from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    data = request.get_json()
    scale_from = data.get("from")
    scale_to = data.get("to")
    try:
        temp = float(data.get("temperature"))
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid temperature input."}), 400

    result = None

    if scale_from == "Celsius":
        if scale_to == "Fahrenheit":
            result = (temp * 9/5) + 32
        elif scale_to == "Kelvin":
            result = temp + 273.15
        elif scale_to == "Celsius":
            result = temp
    elif scale_from == "Fahrenheit":
        if scale_to == "Celsius":
            result = (temp - 32) * 5/9
        elif scale_to == "Kelvin":
            result = (temp - 32) * 5/9 + 273.15
        elif scale_to == "Fahrenheit":
            result = temp
    elif scale_from == "Kelvin":
        if scale_to == "Celsius":
            result = temp - 273.15
        elif scale_to == "Fahrenheit":
            result = (temp - 273.15) * 9/5 + 32
        elif scale_to == "Kelvin":
            result = temp

    return jsonify({
        "result": f"{temp:.2f}° {scale_from} → {result:.2f}° {scale_to}"
    })

if __name__ == "__main__":
    app.run(debug=True)
