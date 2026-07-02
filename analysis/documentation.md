Here are some instructions behind the design of an algorithmic simulation for _An Economy of Eloquence_. 

- The probability for a player to perform an **action** is dependent on all **station value**s. This means that the configuration of the station values on the Game of the Goose should influence players' strategy.

$$
P(A_i) = \sum^n_j P(A_i|S_j)
$$
where A is the action variable, and S are the possible station values configurations.

A heuristic way to model this is to favour actions that either increase or decrease the station value based on the relative position of the player from the average position.


- The **active player** rolls dice, and can combine them with their **Resonance Pool** or lend a die from another player's pool.
- Player performs the action, then their station value and their pool get updated.