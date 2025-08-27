from flask import Flask, jsonify
from flask_cors import CORS
from simulation import F1Simulation

app = Flask(__name__)
CORS(app)

@app.route('/race', methods=['GET'])
def start_race():
    drivers = ["Hamilton", "Verstappen", "Leclerc", "Norris", "Alonso"]
    sim = F1Simulation(drivers, laps=5)
    leaderboard = sim.run_race()

    results = []
    for driver, laps in leaderboard:
        results.append({
            "driver": driver,
            "total_time": round(sum(laps), 2),
            "laps": laps
        })

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
