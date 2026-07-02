"""Functions simulating each game mechanics"""


"""DATA SCTRUCTURES

results = [x_1,x_2...] (from active player)

resonance_pools = [{"player": 0, "resonance_pool": [r_1,r_2,r_n..]}, ...]

stations = [{"player": 0, "station_value": s_0 }]

actions = {"action_0": {"limit": 1, "change_station_value": +1d6, description": ""}, ... }

"""


final_station = 63

import random
import numpy as np
import itertools


def roll_dice(dice_pool=[10, 10]):  # returns the result of a dice pool with dx dice
    results = []
    for die in dice_pool:
        results.append(random.randint(1, die))

    return results


def prime_factorization_polyhedral_die(
    value,
    primes=[
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ],
):
    residual = value
    factorization = []
    end_factorization = False
    while end_factorization is False:
        for prime in primes:
            if residual % prime == 0:
                factorization.append(prime)
                residual = residual / prime
                break
        if residual == 1:
            end_factorization = True

    return factorization


def get_limit_of_proportion(
    proportion,
):  # The limit is defined as the biggest prime number after dividing the two numbers of the factorization
    value_a = prime_factorization_polyhedral_die(proportion[0])
    value_b = prime_factorization_polyhedral_die(proportion[1])

    # cancel out factors
    for factor in value_a:
        if factor in value_b:
            value_b.remove(factor)
            value_a.remove(factor)

    if len(value_a) > 0:
        limit = max(value_a + value_b)
    else:
        limit = 1

    # print(f"Limit of {proportion} is {limit}")
    return limit


# TO BE TESTED
def remove_die_to_resonance_pool(die, player, resonance_pools):
    # player value = player position in resonance_pools dictionary
    resonance_pools[player]["resonance_pool"].remove(die)

    return resonance_pools


# TO BE TESTED
def add_die_to_resonance_pool(die, player, resonance_pools):
    # player value = player position in resonance_pools dictionary
    resonance_pools[player]["resonance_pool"].append(die)

    return resonance_pools


# TO BE TESTED
def change_station_value(
    amount, player_id, stations, min_station=0, max_station=final_station
):  # updates station values and check end_game condition
    # player value = player position in stations dictionary
    end_game = False
    stations[player_id]["station_value"] += amount
    if stations[player_id]["station_value"] < min_station:
        stations[player_id]["station_value"] = 0
    elif stations[player_id]["station_value"] >= max_station:
        end_game = True
        stations[player_id]["station_value"] = final_station
    else:
        pass

    return stations, end_game


def average_station_value(stations):
    return sum([player["station_value"] for player in stations]) / len(stations)


def choose_random_entity_with_open_connection_slots(
    playing_space, connected_entity_id, maximal_connections
):
    condition = True
    while condition is True:
        random_integer = random.choice(range(len(playing_space["board"])))
        if playing_space["board"][random_integer]["entity_id"] != connected_entity_id:
            if (
                len(playing_space["board"][random_integer]["connected_to"])
                < maximal_connections
            ):
                condition = False
                return random_integer


def get_players_lowest_station(stations):
    # get lowest station
    lowest_station = min([station["station_value"] for station in stations])

    players = []

    for player in stations:
        if player["station_value"] == lowest_station:
            players.append(player["player_id"])

    return players


def perform_action(
    action,
    active_player_id,
    playing_space,
    entities,
    maximal_connections=6,
):
    # Add entity and connections
    if (
        action["add_entity"] is True
    ):  # implicitly assume that new entity -> new connection
        random_integer = random.randint(0, len(entities) - 1)
        playing_space["board"].append(
            {
                "entity_id": len(playing_space["board"]) - 1,
                "entity_name": entities[random_integer]["label"],
                "connected_to": [],
            }
        )
        # add random connection until you select a suitable entity. THIS SECTION COULD BE IMPROVED WITH SOME TACTICAL CHOICES!
        random_integer = choose_random_entity_with_open_connection_slots(
            playing_space, len(entities) - 1, maximal_connections
        )
        playing_space["board"][-1]["connected_to"].append(
            playing_space["board"][random_integer]["entity_id"]
        )
        playing_space["board"][random_integer]["connected_to"].append(
            playing_space["board"][-1]["entity_id"]
        )

    # add only connection
    elif action["add_connection"] is True:
        random_entity_id = random.choice(range(len(playing_space["board"])))
        random_integer = choose_random_entity_with_open_connection_slots(
            playing_space, random_entity_id, maximal_connections
        )
        playing_space["board"][random_entity_id]["connected_to"].append(
            playing_space["board"][random_integer]["entity_id"]
        )
        playing_space["board"][random_integer]["connected_to"].append(
            playing_space["board"][random_entity_id]["entity_id"]
        )

    # delete all resonance polls after friction
    try:
        if action["delete_resonance_pools"] is True:
            for player in playing_space["resonance_pools"]:
                player["dice_pool"] = []
    except KeyError:
        pass

    # Change station values

    # Active player
    direction_coefficient = action["active_player_change"][0]
    number_of_dice = action["active_player_change"][1]
    die_type = action["active_player_change"][2]

    dice_pool = [int(die_type[1:]) for die in range(number_of_dice)]

    dice_result = roll_dice(dice_pool)
    stations = playing_space["stations"]
    stations, end_game = change_station_value(
        direction_coefficient * sum(dice_result), active_player_id, stations
    )

    # Select target players
    target_players = []
    exclude = [active_player_id]
    for target_player in range(action["number_target_players"]):
        target_players.append(
            random.choice(list(set(range(0, len(stations) - 1)) - set(exclude)))
        )
        # Apply station change
        direction_coefficient = action["target_player_change"][0]
        number_of_dice = action["target_player_change"][1]
        die_type = action["target_player_change"][2]

        dice_pool = [int(die_type[1:]) for die in range(number_of_dice)]

        dice_result = roll_dice(dice_pool)
        stations, end_game = change_station_value(
            direction_coefficient * sum(dice_result), target_players[-1], stations
        )

    # Update resonance pools

    return playing_space, end_game


# TESTED. OK
def choose_random_action(
    actions, playing_space, active_player_id, action_dice=[10, 10]
):  # active player takes action based on results of dice roll and resonance pools, weigthed based on their relative station value from the average.
    # Roll action dice
    action_dice_result = roll_dice(action_dice)

    print(f"Action dice result: {action_dice_result}")

    combined_resonance_pools = []
    for player in playing_space["resonance_pools"]:
        combined_resonance_pools += player["dice_pool"]

    # get all possible diads, noticing that only a die can come from resonance pool
    possible_proportions = []
    # action die + resonance die case
    for die in action_dice_result:
        for resonance_die in combined_resonance_pools:
            possible_proportions.append((die, resonance_die))

    # 2 action dice case using itertools.combinations()
    possible_proportions += itertools.combinations(action_dice_result, 2)

    print(f"Possible proportions: {possible_proportions}")

    # get limits for each proportion

    limits = []
    for proportion in possible_proportions:
        limits.append(get_limit_of_proportion(proportion))

    # weight according to average station value
    avg_station = average_station_value(playing_space["stations"])

    if playing_space["stations"][active_player_id]["station_value"] >= avg_station:
        above_average = True
    else:
        above_average = False

    actions_distribution = [
        {
            "action_name": key,
            "increases_station_value": actions[key]["increases_station_value"],
            "limit": actions[key]["limit"],
            "frequency": 0,
            "probability": 0,
        }
        for key in actions.keys()
    ]

    # calculate weighted frequency
    for action in actions_distribution:
        action["frequency"] = 0
        for limit in limits:
            if limit == action["limit"]:
                action["frequency"] += 1

        # apply weighting
        if above_average is True:
            if action["increases_station_value"] is True:
                action["frequency"] *= 1.5
            else:
                action["frequency"] *= 0.5
        else:
            if action["increases_station_value"] is True:
                action["frequency"] *= 0.5
            else:
                action["frequency"] *= 1.5

    total_frequency = sum([action["frequency"] for action in actions_distribution])

    # calculate probability of action

    for action in actions_distribution:
        action["probability"] = action["frequency"] / total_frequency

    print(f"Actions distribution: {actions_distribution}")

    # get random number between 0 and 1, according to distribution

    action_names = [action["action_name"] for action in actions_distribution]
    action_probability = [action["probability"] for action in actions_distribution]

    chosen_action = np.random.choice(action_names, size=1, p=action_probability)

    print(f"Choosen action: {chosen_action[0]}")

    # Get dice diad randomly

    dice_diad = None

    candidate_diads = []

    for limit in limits:
        if limit == actions[chosen_action[0]]["limit"]:
            candidate_diads.append(possible_proportions)

    dice_diad = random.choice(candidate_diads)

    if dice_diad in itertools.combinations(action_dice_result, 2):
        return {
            "action": chosen_action[0],
            "active_player_id": active_player_id,
            "dice_diad": dice_diad,
            "donor_player_id": active_player_id,
            "keep_die": random.choice(action_dice_result.remove(dice_diad[0])),
            "donor_die": None,
            "resonance_pool": False,
        }

    else:
        # retrive dice from pools
        donor_player_id = None
        candidate_donor_players = []
        for player in playing_space["resonance_pools"]:
            if dice_diad[1] in player["dice_pool"]:
                candidate_donor_players.append(player["player_id"])

        # Append other die from action pool, if matches action roll
        if dice_diad[1] in action_dice_result[1:]:
            candidate_donor_players.append(active_player_id)

        if len(candidate_donor_players) > 0:
            donor_player_id = random.choice(candidate_donor_players)

        else:
            donor_player_id = active_player_id

        return {
            "action": chosen_action[0],
            "active_player_id": active_player_id,
            "dice_diad": dice_diad,
            "donor_player_id": donor_player_id,
            "keep_die": random.choice(action_dice_result.remove(dice_diad[0])),
            "donor_die": dice_diad[1],
            "resonance_pool": True,
        }
