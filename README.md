# Flight Navigation Project

## Overview

The Flight Navigation Project is designed to enhance flight route planning and risk mitigation by utilizing a genetic algorithm to optimize flight paths. This project addresses various challenges encountered during flight navigation such as unavailable GPS signals, adverse weather conditions, and electronic failures. It integrates real-time data to provide optimal routes, risk assessments, and alternative route suggestions to pilots, airlines, and airport authorities.

## Features

- **Real-time Data Collection**: Gathers data from various sources to account for weather conditions, electronic system status, and other environmental factors.
- **Genetic Algorithm**: Implements a genetic algorithm to determine the best possible route between the start and end points.
- **Risk Mitigation**: Identifies and avoids potential risks along the flight path.
- **Dynamic Route Planning**: Allows dynamic input for start and end points to provide flexible and adaptive route planning.
- **Visualization**: Graphical representation of the route, including obstacles and the final path.

## Tech Stack

- **Python**: Core programming language.
- **Libraries**: 
  - `numpy`: For numerical operations.
  - `matplotlib`: For visualization.
  - `requests`: For API requests.
  - `json`: For handling JSON data.
- **APIs**:
  - [OpenWeatherMap API](https://openweathermap.org/api)
  - [Aviation Stack API](https://aviationstack.com)
  
## File Structure








## Setup and Installation

1. **Clone the Repository**:
    ```
    git clone https://github.com/yourusername/flight_navigation_project.git
    cd flight_navigation_project
    ```

2. **Create a Virtual Environment** (optional but recommended):
    ```
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```
    pip install -r requirements.txt
    ```
  
4. **Run the Project**:
    ```
    python src/main.py
    ```

## Usage

1. **Start and End Positions**:
   - When prompted, enter the start and end coordinates for the flight route. The format should be `(x, y)`, where `x` and `y` are integers representing the grid coordinates.

2. **Visualization**:
   - The best route calculated by the genetic algorithm will be displayed in a graphical format, highlighting the path and any obstacles.

## Code Explanation

### data_collection.py

This script collects weather data from an API and saves it into a JSON file.

### genetic_algorithm.py

Implements the genetic algorithm to find the optimal flight path. Key functions include:
- `initialize_population`: Creates an initial set of routes.
- `fitness`: Evaluates each route based on distance and obstacles.
- `selection`: Selects the best routes for reproduction.
- `crossover`: Combines two parent routes to produce offspring.
- `mutate`: Introduces variations to maintain genetic diversity.
- `genetic_algorithm`: Orchestrates the entire genetic algorithm process.

### scenario_identification.py

Loads the sample data and identifies obstacles based on weather conditions.

### visualization.py

Plots the flight path and obstacles using `matplotlib`.

### main.py

The entry point of the project. Collects user input, runs the genetic algorithm, and visualizes the results.

## Contributing

Contributions are welcome! Please create a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## References

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Aviation Stack API](https://aviationstack.com)
- [FlightAware API](https://www.flightaware.com/commercial/aeroapi)
- [AviationWeather.gov API](https://www.aviationweather.gov/dataserver)


