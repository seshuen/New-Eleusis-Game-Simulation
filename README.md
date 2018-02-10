
# The Game of New Eleusis
## Project By: Anonymous Agents
### Implementation:
As per the problem statement for Phase 2, we have implemented the New Eleusis game as a
multi-player game. Considering the plays of the other players who are the adversaries, we have
updated the board state accordingly for every play. Also, in contradiction to Phase 1 where
there the player had an infinite hand to play from, in Phase 2, each player is given only a set of
14 cards. Whenever the player plays a card from the hand, a new randomly generated card is
added to the hand so that the player has 14 cards in hand at any point in the game.
Furthermore, 14 rounds of games are played by each player and the adversaries starting with
our player as the first player. We also considered the fact that the game ends whenever any of
the​ ​ player​ ​ predicts​ ​ the​ ​ rule.
In Phase 1, we maintained a threshold of 20 plays, only after which the single player predicts a
rule. Also, the player randomly played the card to build the decision tree and in turn predict the
rule in Phase 1. However, in Phase 2, since the game is to come up with a rule before the other
adversaries, our player played a card from hand which would help him in predicting the rule.
Additionally, bonus scores are given in Phase 2 for the player who comes up with a correct rule
first. Particularly, we have tried to enhance our player function in this phase rather than trying to
change the way the rule is being predicted. We have implemented the decision tree using gain
ratio like we have done in the first phase, but tried to generate a rule within few plays; thus
applying​ ​ constraints​ ​ to​ ​ our​ ​ decision​ ​ tree​ ​ function​ ​ to​ ​ generate​ ​ a ​ ​ rule​ ​ as​ ​ early​ ​ as​ ​ possible.
In addition, since the threshold to predict the rule is very less, there are few cases wherein all
the cards that are being played are ‘Legal’ according to God’s rule. In such cases, when there is
no classification, forming a decision tree is hard. To deal with such cases when there is no
classification and when an adversary is predicting the rule before our player, we have taken the
‘Legal’​ ​ which​ ​ is​ ​ True​ ​ node​ ​ as​ ​ the​ ​ predicted​ ​ rule.
### Files Present:
 - Game.py​ ​ - ​ ​ Contains​ ​ the​ ​ play()​ ​ and​ ​ update_board_state()​ ​ functions​ ​ and​ ​ the​ ​ game​ ​ play​ ​ is
being​ ​ dealt​ ​ here.​ ​ God’s​ ​ rule​ ​ and​ ​ the​ ​ first​ ​ 3 ​ ​ legal​ ​ cards​ ​ are​ ​ explicitly​ ​ given​ ​ here.​ ​ Also,​ ​ the
game​ ​ is​ ​ initialized​ ​ in​ ​ this​ ​ file.
 - AnonymousAgents.py​ ​ - ​ ​ Contains​ ​ the​ ​ functions​ ​ for​ ​ testing​ ​ the​ ​ hypothesis,​ ​ calculating​ ​ the
logical​ ​ equivalence​ ​ and​ ​ giving​ ​ the​ ​ score​ ​ to​ ​ the​ ​ player.
 - StandAlone.py​ ​ - ​ ​ Contains​ ​ the​ ​ function​ ​ to​ ​ generate​ ​ random​ ​ cards​ ​ from​ ​ a ​ ​ deck​ ​ of​ ​ 52
cards.
 - attribute.py​ ​ - ​ ​ Contains​ ​ the​ ​ logic​ ​ for​ ​ creation​ ​ of​ ​ decision​ ​ tree​ ​ and​ ​ gain​ ​ ratio.
 - God.py​ ​ - ​ ​ Contains​ ​ the​ ​ function​ ​ to​ ​ set​ ​ the​ ​ rule​ ​ and​ ​ validate​ ​ the​ ​ cards.
 - boardState​ ​ - ​ ​ Contains​ ​ the​ ​ functions​ ​ for​ ​ updation​ ​ of​ ​ the​ ​ board​ ​ state​ ​ in​ ​ accordance​ ​ to​ ​ the
cards​ ​ played.
 - trainingData​ ​ - ​ ​ Contains​ ​ the​ ​ attribute​ ​ data​ ​ and​ ​ mapping​ ​ the​ ​ attribute​ ​ to​ ​ the​ ​ functions​ ​ in
new_eleusis.py

#### Project Inspiration: http://matuszek.org/eleusis0.html
