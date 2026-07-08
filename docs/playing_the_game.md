---
hide:
  - title
  - toc
---

# Playing the Game

## The Game Master

Before the start of the session, the players designate one of them as Game Master. They act as moderators and final judge for the session. Such person should be familiar with the rules and being comfortable in taking decisions and monitor the behaviour of each participant, encouraging a playful and respectful environment.

## Setting up the Board

For this game you will need:

- 3-10 players and a Game Master.
- A pawn (meeple) for each player.
- A Game of Goose board, usually made of 63 stations, or a custom one.
- 1 to 3 hours, depending on the size of the group and the end-of-game station designated.
- Pencils, post-its and small index cards to write down entities.
- A set of 4-8 eight-sided dice for each player and 3 six-sided dice for the station advancement.
- Hexagonal tiles
- A (digital) hourglass in order to keep track of time slots.

### Preparatory Phase

Each player collects 2 eight-sided dice.

Afterwards, the GM asks each player to place one entity on the board. These entities can be tied to a theme, such as the players' research interest or topics of a conference.

Once every player has placed an entity on the board they define their initial position on the Game of Goose by rolling a six-sided die and place their pawn on the station correspondent to the die result. Ties will eventually emerge, and the GM has the responsibility to decide which player goes first.

Finally, the group determine the end-of-game station that will trigger the end of the session.

## Player's Turn

1. Roll 2d10 and look for proportions according to the [**Resonance System**](core_rules.md)
2. Eventually, add one die from your own **Resonance Pool** or ask it from another player.
3. Choose one pair of dice and perform the corresponding [**Eloquent Action**](core_rules.md)
4. Advance or regress the station of your pawn on Goose Game board according to the chosen action.
5. Store the die that was not chosen for the pair from the initial 2d8s and add it to your **Resonance Pool**.

## The Game Session

The active player is the one with pawn at the lowest station of the **Game of Goose**. In case of ties, the GM decides which player goes first.

### End of the Game

Once a player reaches the end-of-game station the session is over. Complete the following steps in order to determine the final score, called **Eloquence Score**.

1. The GM computes the average $\mu$ of the players' final station values $x_i$ on the Goose Game board, rounded down.

$$
\mu = \dfrac{1}{n} \sum_i^n x_i 
$$


2. Each player calculate the absolute distance $d_i$ between their final station and the average $\mu$

$$
d_i = |\mu - x_i|
$$

3. The GM determines the **Connected Components Penalty** $p$. The more the knowledge graph is connected, the less numerical penalty.

| Connected components | $p$ |
| :--------------------: | :-------: |
| 1                    | 0       |
| 2-3                  | 1       |
| 4-6                  | 4       |
| 7+                   | 8       |

4. The final **Eloquence Score** $E$ is given by 

$$
E = p +\dfrac{1}{n}\sum_i^n d_i
$$

!!! note inline end "Example"

    Four players agreed to play until station 50 of the Goose Game. When one of them reaches the end-of-game station, the GM computes the average of their final positions (12,25,47,50) resulting in a value of 33. The player have generated a network of entities with 2 connected components, resulting in a penalty of 4 (the number of players). Afterwards, the **Eloquence Score** for the group is computed, adding the penalty, resulting in 1 + \[(33-12) + (33-25) + (47-33) + (50-33)\]/4 = 16.

| Eloquence Score range | Victory Level |
| :---------------------------: | :-------------: |
| 0-5                         | Excellent     |
| 6-10                        | Great         |
| 11-15                       | Good          |
| 16-20                       | Mediocre      |
| 20+                         | Unbalanced    |


