from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock Weather Data
weather_data = {
    "new york": {"temperature": 22, "condition": "Sunny"},
    "london": {"temperature": 15, "condition": "Cloudy"},
    "tokyo": {"temperature": 28, "condition": "Clear"},
    "sydney": {"temperature": 18, "condition": "Rainy"}
}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the mini Weather API"})

@app.route('/weather', methods=['GET'])
def weather():
    return jsonify(weather_data)

@app.route('/weather/<city>')
def get_city(city):
    city = city.lower()
    if city in weather_data:
        return jsonify({city : weather_data[city]}), 201
    return jsonify({"error" : "City not found"}), 400

@app.route('/weather', methods=["POST"])
def add_city():
    data = request.json
    city = data.get('city', '').lower()
    temperature = data.get('temperature')
    condition = data.get("condition")
    
    if not city or not temperature or not condition:
        return jsonify({'error' : 'Missing City or temperature or condition'}), 400
    
    weather_data[city] = {"temperature" : temperature, "condition" : condition}
    return jsonify({"message" : "Created successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True)