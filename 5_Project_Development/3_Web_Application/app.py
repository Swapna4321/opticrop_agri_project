from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    N = float(request.form['N'])
    P = float(request.form['P'])
    K = float(request.form['K'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])

    if rainfall > 150 and humidity > 70:
        crop = "Rice"
    elif temperature > 25 and rainfall < 100:
        crop = "Maize"
    elif ph > 6.5 and rainfall > 100:
        crop = "Cotton"
    else:
        crop = "Wheat"

    return render_template(
        'index.html',
        prediction_text=f"Recommended Crop: {crop}"
    )

if __name__ == "__main__":
    app.run(debug=True) idi ela create cheyali endulo run cheyali yela cheyali
