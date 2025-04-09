from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def weather():
    city = "Москва"
    temperature = "+10°C"
    return render_template('weather.html', city=city, temperature=temperature)

if __name__ == '__main__':
    app.run(debug=True)