def set_covering(states, stations):
    final_stations = set()
    while states:
        best_station = None
        states_covered = set()
        for station, coverage in stations.items():
            covered = states & coverage
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states -= states_covered
        final_stations.add(best_station)
    return final_stations


states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

print(set_covering(states, stations))
