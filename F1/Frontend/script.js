async function startRace() {
    const response = await fetch("http://127.0.0.1:5000/race");
    const data = await response.json();

    const tbody = document.querySelector("#leaderboard tbody");
    tbody.innerHTML = "";

    data.forEach((driver) => {
        const row = `<tr>
            <td>${driver.driver}</td>
            <td>${driver.total_time}</td>
            <td>${driver.laps.join(", ")}</td>
        </tr>`;
        tbody.innerHTML += row;
    });
}
