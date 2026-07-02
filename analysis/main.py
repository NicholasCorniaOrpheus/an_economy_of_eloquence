import sys

sys.path.append("./modules")

from modules.game_mechanics import *
from modules.utilities import *


# TO DO

"""
- Find an efficient way to calculate choice of action probability (horizon of actions)
- Simulate round of play
- Check update of pools, station values and co.
- harmony score and end_conditons
- Adjust choice of action according to history (horizon of intent) for optimal strategy
- Store entities information in networkx graph.

"""

#### FUCTIONS ####


def get_random_board(playing_space, entities, players, entities_per_player):
	number_of_entities = players * entities_per_player

	# Cleanup previous configuration
	playing_space["board"] = []

	for i in range(number_of_entities):
		random_entity = random.choice(entities)
		entities.remove(random_entity)
		playing_space["board"].append(
			{
				"entity_id": i,
				"entity_name": random_entity["label"],
				"connected_to": [],
			}
		)

	return playing_space


def set_initial_conditions(
	playing_space, players, station_values, resonance_pools, board=[]
):
	# Reset everything
	playing_space["stations"] = []
	playing_space["resonance_pools"] = []
	# create new values
	i = 0
	for player in range(players):
		playing_space["stations"].append(
			{"player_id": i, "station_value": station_values[i]}
		)

		playing_space["resonance_pools"].append(
			{"player_id": i, "dice_pool": resonance_pools[i]}
		)

		i += 1

	return playing_space


#### CODE #####

print("Importing initial conditions")
data_directory = "./data"
actions = json2dict(os.path.join(data_directory, "actions.json"))
playing_space = json2dict(os.path.join(data_directory, "playing_space.json"))
entities = json2dict(os.path.join(data_directory, "composers_wikidata.json"))
game_sessions = json2dict(os.path.join(data_directory, "game_sessions.json"))

# Initialize game sessions dictionary
game_sessions = []

# Set initial conditions

players = 4

entities_per_player = 1

initial_station_values = [sum(roll_dice([6])) for i in range(players)]

print(f"Initial station values: {initial_station_values}")

initial_resonance_pools = [[2, 5], [3, 1], [], [4]]

playing_space = get_random_board(playing_space, entities, players, entities_per_player)

playing_space = set_initial_conditions(
	playing_space, players, initial_station_values, initial_resonance_pools
)

# Save to JSON

print("Setting initial conditions...")
dict2json(playing_space, os.path.join(data_directory, "playing_space.json"))

# TESTING

print("Test cycle of actions")
turns = 1
exit = False
while exit is False:
	print("New Turn")
	players_lowest_station = get_players_lowest_station(playing_space["stations"])
	if len(players_lowest_station) > 1:
		# choose a random player from those with the lowest station
		active_player = random.choice(players_lowest_station)
	else:
		active_player = players_lowest_station[0]

	print(f"Active player: {active_player}")

	action = actions[choose_random_action(actions, playing_space, active_player)]

	print(f"Random action: {action}")

	playing_space, end_game = perform_action(
		action["action"], active_player, playing_space, entities
	)

	# Update resonance_pools

	if action["resonance_pool"] is True:
		print(f"Removing {action["donor_die"]} from resonance pool of {action["donor_player_id"]}...")
		playing_space["resonance_pools"] = remove_die_to_resonance_pool(action["donor_die"], action["donor_player_id"], playing_space["resonance_pools"])

	# Active player adds one action die to resonance pool:
	print(f"Active players keeps {action["keep_die"]}")
	playing_space["resonance_pools"] = add_die_to_resonance_pool(action["keep_die"], action["active_player_id"], playing_space["resonance_pools"])

	input()


	if end_game is True:
		print("End-of-game station is reached.")
		exit = True
		print(playing_space)

	else:
		print(f"Turn {turns}: \n {playing_space}")
		turns += 1
