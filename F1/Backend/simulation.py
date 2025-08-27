import random
import time

class F1Simulation:
    def __init__(self, drivers, laps=5):
        self.drivers = drivers
        self.laps = laps
        self.results = {driver: [] for driver in drivers}

    def run_race(self):
        for lap in range(self.laps):
            for driver in self.drivers:
                lap_time = round(random.uniform(60, 80), 2)  # 60–80 sec per lap
                self.results[driver].append(lap_time)
                time.sleep(0.1)  # Simulate delay

        leaderboard = sorted(
            self.results.items(),
            key=lambda x: sum(x[1])
        )
        return leaderboard
