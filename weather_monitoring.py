import requests

def get_weather_data(city, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    
    # Debug: Print the URL and response
    print(f"Request URL: {response.url}")  # Print the URL being requested
    response_json = response.json()
    print(f"Response JSON: {response_json}")  # Print the entire response for debugging
    
    if response.status_code != 200:
        return {}  # Return an empty dict if the request failed
    
    return response_json

def display_weather(data):
    if not data or data.get('cod') != 200:
        print("City not found!")
        return
    
    # Display weather information
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

def main():
    api_key = '699df711088fc34794664656ad6ebe5a'  # Replace with your actual OpenWeatherMap API key
    city = input("Enter the city name: ")
    weather_data = get_weather_data(city, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
