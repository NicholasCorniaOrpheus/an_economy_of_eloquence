---
hide:
  - title
  - toc
---

# Core Rules

To embrace the main objectives of this game, namely collaborative knowledge building and unexpected intellectual journeys, we have designed a series of game mechanics that will help the players emulate a fruitful and truly collaborative conversation.

## Knowledge Graphs

A knowledge graph is a non-hierarchical data structure composed by entities, namely any sort of thing you can imagine, and statements connecting them.

In _An Economy of Eloquence_, entities are represented by wooden tiles that can store a small index card. Statements, relating two entities on the graph, are represented by coloured cords. 

<center><img src="../assets/images/entities_example.png" width="500" height="300"></center>

## Resonance System

The Resonance System is a dice pool resolution mechanics designed by the author, and has been used in several experimental games such as [Sprezzatura RPG](https://nicholascornia89.github.io/sprezzatura_rpg/).

The players will use pools of ten-sides dice (d10s) and assemble pairs of results to generate a rational number. The highest prime number of the fraction (after reducing it) is considered as result. With ten-sides dice there are only five possibilities, each of them reflecting a musical proportion, according to Medieval and Renaissance theory:

- **Unison (U)**: A fraction giving the unit 1, when both dice presents the same number, generates the unison proportion.
- **Octave (O)**: A fraction giving the ratio 2:1, such as <sup>4</sup>/<sub>2</sub>,   generates an octave.
- **Fifth (F)**: A fraction with a ratio such that the highest prime number is 3, such as <sup>4</sup>/<sub>3</sub> or <sup>6</sup>/<sub>4</sub> = <sup>3</sup>/<sub>2</sub>, generates the interval of the fifth or its complementary the fourth.
- **Third (T)**: A fraction with a ration such that the highest prime number is 5, such as <sup>6</sup>/<sub>5</sub> or <sup>5</sup>/<sub>4</sub>, generates the interval of third, and its complementary the sixth.
- **Dissonance (D)**: In this system, ratios with a dominant prime number of 7 are associated with dissonant harsh sounds (at least for 16th centuries ears). 

Below a table describing all the possible combination of number given two d10s:

| d10 x d10 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **U** | **O** | **F** | **O** | **T** | **F** | **D** | **O** | **F** | **T** |
| 2 | | **U** | **F** | **O** | **T** | **F** | **D** | **O** | **F**| **T** |
| 3 | | | **U** | **F** | **T** | **O** | **D** | **F** | **T** | **T** |
| 4 | | | | **U** | **T** | **F** | **D** | **O** | **F** | **T** |
| 5 | | | | | **U** | **T** | **D** | **T** | **T** | **O** |
| 6 | | | | | | **U** | **D** | **F** | **F** | **T** |
| 7 | | | | | | | **U** | **D** | **D** | **D** |
| 8 | | | | | | | | **U** | **F** | **T** |
| 9 | | | | | | | | | **U** | **T** |
| 10 | | | | | | | |  | | **U**|

Given two dice the probability to obtain a given musical interval is not uniform, this means that the game favors some results than others. It is up to the players to bend this asymmetry in their favor thanks to the _Resonance Pool_ mechanics.

Here you can find the probability distribution, given two dice of obtaining a certain proportion:

- P(U) = <sup>10</sup>/<sub>100</sub>
- P(O) = <sup>16</sup>/<sub>100</sub>
- P(F) = <sup>26</sup>/<sub>100</sub>
- P(T) = <sup>30</sup>/<sub>100</sub>
- P(D) = <sup>18</sup>/<sub>100</sub>


### Resonance Pool

At the end of each turn, the active player can store an unused die, one that did not belong to the pair of dice that generated the action just taken, to a personal pool called the _Resonance Pool_. These dice can be used at any moment by the player to assemble musical intervals either during their turn of any other player's. There is no limit of dice that can be kept, but an action like _discord_ can potentially reset a player's pool.

This mechanics has been designed to encourage collaboration and engagement of all players, reducing the burden of _downtime_[^1].


## Eloquent Actions

To determine the available actions, a player rolls 4 ten-sided dice at the beginning of their turn. They can assemble a pair of dice to generate a musical interval, selecting dice from

- the 4 dice just rolled
- a die from their own _Resonance Pool_
- a die from another player's _Resonance Pool_

!!! info "Dissonance"

    Note that if one of the dice just rolled is a 7 it has to be selected by the active player, unless it can be paired with another 7 from the board or _Resonance Pools_ to generate a Unison.

Below the list of actions associated with each musical interval:

<div class="grid cards" markdown>

-   :material-pen: __Invent (Fifth)__

    ---
    The interval of a Fifth allows the active player to _Invent_. 

    You can introduce a new entity on the knowledge graph and describe it to the fellow players using a time slot. The can create a statement with an entity already present on the board if they wish.

    Afterwards, gain one _eloquence_ tokens. :material-plus-circle:

-   :octicons-book-16: __Digress (Third)__

    ---
    The interval of a Third allows the active player to _Digress_.

    You can use a time slot to deepen the conversation around an entity on the knowledge graph. After that they can create a statement, a new connection with another concept on board.

    Afterwards, gain one _eloquence_ token. :material-plus-circle:

-   :octicons-comment-discussion-16: __Quarrel (Unison)__

    ---
    The inverval of an Unison allows the active player to _Quarrel_.

    Choose two players (they can include youself) and an entity on the knowledge graph.

    The designated players receive two time slots to discuss about a topic associated with the entity. 

    After that the other players who did not participated in the content, vote the most convincing speaker who immediately can create a statement.

    If you have been part of the quarrel, gain one _eloquence_ token, otherwise lose one. :material-plus-circle: :material-minus-circle:

-   :simple-discourse: __Summon (Octave)__

    ---
    The interval of an Octave allows the active player to _Summon_.

    Choose a fellow player and invite them to talk about an entity on board.

    After that you can create a statement,then lose one _eloquence_ token. :material-minus-circle:


-   :material-lightning-bolt: __Friction (Dissonance)__ 

    ---
    
    A Dissonance forces the active player to _Friction_.

    Choose one of the following options:

    - Reset your _Resonance Pool_ to empty, then lose two _eloquence_ tokens. :material-minus-circle:
    - Designate another player and empty their _Resonance Pool_, then gain two _eloquence_ tokens. :material-plus-circle:
    - Gain four _eloquence tokens_ with no further consequences. :material-plus-circle:

</div>

## The Game of Goose

Inspired by the board game [_Patchwork_](https://boardgamegeek.com/boardgame/163412/patchwork), we decided to use a dynamic initiative system for our game as an alternative to the conventional clockwise or counter-clockwise turn order. Each player places a meeple on a Game of Goose board. At the end of each player's turn, their meeple will advance according to the perfomed _Eloquent Action_.

| Action   | Meeple advance value |
| -------- | -------------- |
| _Invent_ | 2d6  |
| _Digress_ | 2d6 |
| _Quarrel_ | 3d6 |
| _Summon_ | 2d6 |
| _Friction_ | 3d6 |

Usually, the player with meeple in the lowest station of the Game of Goose can take the next turn. In case of ties, the GM can choose which player goes first.

The GM has to decide beforehand which station will end the game. We advise the following values, but bear in mind that larger groups will take longer to reach the end station:

- 28 for a short session
- 42 for a comprehensive exploration
- 63 for a long session ranging multiple hours, for example a conference day.
    
## Harmony Score

_An Economy of Eloquence_ is a cooperative game that takes inspiration to collaborative games such as [_Hanabi_](https://boardgamegeek.com/boardgame/98778/hanabi) and [_Tales of Kunugi_](https://boardgamegeek.com/boardgame/422620/tales-of-kunugi).

The main goal of the group is to achieve the lowest collective _Harmony Score_, reflecting balance and collaboration between the players during the creation of the knowledge graph.

When a player reaches the designated end-of-game station, the game session ends.  The GM computes the average value (rounded up) for all players, based on the amount of coins they own. 

Afterwards, each player computes the absolute distance between their coin amount and the aforementioned average value. This number is called the _Harmony Score_ of a player. Finally, the GM computes the sum of all the Harmony scores, and the final result will reflect how balance and collaborative the game session has been.

For example, a session with 5 players ends with _eloquence_ tokens amounts of 8, 12, 10, 22 and 14.
The average value is 14 (rounded up) and for each player we have _Harmony Scores_ of 6, 2, 4, 8, 0, leading to a final collective value of 20.

Average Harmony score (heuristic) table, based on the number of players _n_

| Average Harmony Score range | Victory Level |
| --------------------------- | ------------- |
| 0 to _n_                    | Excellent     |
| _n+1_ to _2n_               | Great         |
| _2n+1_ to _3n_              | Good          |
| _3n+1_ to _4n_              | Mediocre      |
| more than _4n+1_            | Unbalanced    |
 





[^1]: _downtime_: term used in board games to indicate the period of inactivity for a player outside of their turn.