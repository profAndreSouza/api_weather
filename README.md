# Weather Application

This is a weather application built using Python with Django Rest Framework that integrates MongoDB as its database. The application follows the Model-View-Template (MVT) pattern and provides support for calling external APIs to fetch weather data.

## Features

- **Weather Data**: Retrieve weather data from external APIs.
- **Database Integration**: Store and manage weather data using MongoDB.
- **RESTful API**: Expose endpoints to interact with weather data.
- **MVT Pattern**: Organize codebase following the Model-View-Template pattern.

## Requirements

- Python 3.x
- Django
- Django Rest Framework
- MongoDB
- External Weather API (e.g., OpenWeatherMap, WeatherAPI)

## Setup

1. **Clone the Repository**:

```bash
git clone https://github.com/profAndreSouza/api_weather.git
```

2. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

3. **Configure MongoDB**:

- Install and configure MongoDB.
- Update the database settings in `settings.py` to connect to your MongoDB instance.

4. **External API Integration**:

- Sign up for an account on a weather API provider.
- Get API credentials and update settings in the application accordingly.

5. **Start the Server**:

```bash
python manage.py runserver
```

6. **Access the API**:

The API endpoints will be available at `http://localhost:8000/api/`.

## API Endpoints

- `/`: List all weather data.
- `/generate`: Generate aleatory weather record.
- `/reset`: Delete all weather records.

## Usage

1. Fetch Weather Data from External API:

```python
# Example code to fetch weather data from external API
import requests

def fetch_weather_data():
    api_key = 'your_api_key'
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q=London'
    response = requests.get(url)
    data = response.json()
    return data
```

2. Store Weather Data in MongoDB:

```python
# Example code to store weather data in MongoDB
from pymongo import MongoClient

def save_to_mongodb(data):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['weather']
    collection = db['weather_data']
    collection.insert_one(data)
```

3. Access Weather Data via API:

```python
# Example code to access weather data via API
import requests

def get_weather_data():
    response = requests.get('http://localhost:8000/api/weather/')
    data = response.json()
    return data
```

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
