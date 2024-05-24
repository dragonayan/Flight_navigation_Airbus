import json

def load_sample_data(filename='./data/sample_data.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def identify_obstacles(data):
    weather_conditions = data['weather'][0]['main']
    obstacles = []
    if weather_conditions in ['Rain', 'Snow', 'Fog']:
        obstacles = [(i, i) for i in range(10, 20)]
    return obstacles

if __name__ == '__main__':
    data = load_sample_data()
    obstacles = identify_obstacles(data)
    print(obstacles)
