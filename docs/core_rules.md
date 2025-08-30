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

The players will use pools of eight-sides dice (d8s) and assemble pairs of results to generate a rational number. The highest prime number of the fraction (after reducing it) is considered as result. With eight-sides dice there are only five possibilities, each of them reflecting a musical proportion, according to Medieval and Renaissance theory:

- **Unison (U)**: A fraction giving the unit 1, when both dice presents the same number, generates the unison proportion.
- **Octave (O)**: A fraction giving the ratio 2:1, such as <sup>4</sup>/<sub>2</sub>,   generates an octave.
- **Fifth (F)**: A fraction with a ratio such that the highest prime number is 3, such as <sup>4</sup>/<sub>3</sub> or <sup>6</sup>/<sub>4</sub> = <sup>3</sup>/<sub>2</sub>, generates the interval of the fifth or its complementary the fourth.
- **Third (T)**: A fraction with a ration such that the highest prime number is 5, such as <sup>6</sup>/<sub>5</sub> or <sup>5</sup>/<sub>4</sub>, generates the interval of third, and its complementary the sixth.
- **Dissonance (D)**: In this system, ratios with a dominant prime number of 7 are associated with dissonant harsh sounds (at least for 16th centuries ears). 

Below a table describing all the possible combination of number given two d8s:

| d8 x d8 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **U** | **O** | **F** | **O** | **T** | **F** | **D** | **O** |
| 2 | | **U** | **F** | **O** | **T** | **F** | **D** | **O** |
| 3 | | | **U** | **F** | **T** | **O** | **D** | **F** | 
| 4 | | | | **U** | **T** | **F** | **D** | **O** |
| 5 | | | | | **U** | **T** | **D** | **T** |
| 6 | | | | | | **U** | **D** | **F** |
| 7 | | | | | | | **U** | **D** |
| 8 | | | | | | | | **U** |

Given two dice the probability to obtain a given musical interval is not uniform, this means that the game favors some results than others. It is up to the players to bend this asymmetry in their favor thanks to the _Resonance Pool_ mechanics.

### Resonance Pool

At the end of each turn, the active player can store an unused die, one that did not belong to the pair of dice that generated the action just taken, to a personal pool called the _Resonance Pool_. These dice can be used at any moment by the player to assemble musical intervals either during their turn of any other player's. There is no limit of dice that can be kept, but an action like _discord_ can potentially reset a player's pool.

This mechanics has been designed to encourage collaboration and engagement of all players, reducing the burden of _downtime_[^1].


## Eloquent Actions

To determine the available actions, a player rolls 4 eight-sided dice at the beginning of their turn. They can assemble a pair of dice to generate a musical interval, selecting dice from

- the 4 dice just rolled
- a die from their own _Resonance Pool_
- a die from another player's _Resonance Pool_

!!! info "Dissonance"

    Note that if one of the dice just rolled is a 7 it has to be selected by the active player, unless it can be paired with another 7 from the board or _Resonance Pools_ to generate a Unison.

Below the list of actions associated with each musical interval:

<div class="grid cards" markdown>

-   :material-pen: __Invent (Unison)__

    ---
    The interval of an Unison allows the active player to _Invent_. 

    You can introduce a new entity on the knowledge graph and describe it to the fellow players using a time slot. The can create a statement with an entity already present on the board if they wish.

-   :octicons-book-16: __Digress (Fifth)__

    ---
    The interval of a Fifth allows the active player to _Digress_.

    You can use a time slot to deepen the conversation around an entity on the knowledge graph. After that they can create a statement, a new connection with another concept on board.

-   :octicons-book-16: __Quarrel (Octave)__

    ---
    The inverval of an Octave allows the active player to _Quarrel_.

    Choose two players (they can include youself) and an entity on the knowledge graph.

    The designated players receive two time slots to discuss about a topic associated with the entity. 

    After that the other players who did not participated in the content, vote the most convincing speaker who immediately can create a statement.

-   :octicons-book-16: __Summon (Third)__

    ---
    The interval of a Third allows the active player to _Summon_.

    Choose a fellow player and invite them to talk about an entity on board.

    After that you can create a statement.


-   :octicons-book-16: __Strife__ (Dissonance)
    ---
    
    A Dissonance forces the active player to _Strife_.

    TO BE CONTINUED

    

    
</div>

### Invent (Unison)

 



[^1]: _downtime_: term used in board games to indicate the period of inactivity for a player outside of their turn.