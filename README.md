# Tic Tac Toe

This game is all about two players taking turns entering X or O in a board and trying to connect three in a line to win the game.

This version uses Greg Surma's "Unbeatable AI" algorithm to make it a frustrating single player experience.

## Algorithm

[Greg Surma's blog post can be found here](https://gsurma.medium.com/tic-tac-toe-creating-unbeatable-ai-with-minimax-algorithm-8af9e52c1e7d#14e6 "Greg Surma on Medium")

The algorithm essentially simulates all possible turns that any player can do in any of the upcoming turns and assigns a value to the outcomes. A "1" denotes a win for the computer, a "-1" a win for the Player, a "0" a draw. The results then get propagated backwards, and the previous decisions leading to these outcomes get assigned the values of the outcomes. A min/max approach follows, where for player turns the worst result gets propagated upwards as a "worst case if the computer takes this turn", while for computer turns the best result gets propagated upwards as a "this would be a good turn for the computer to take" until at the highest level the computer has a clear idea of possible outcomes for each of their turns and only takes one, that's guaranteed to end in at least a draw.

To use the example also given in the blog post, assuming the PC has three possible fields to put their "X" in.
* Field one leads to a gameover, PC victory.
* Field two does not end the game and leaves two fields for the Player to take.
   Field one leads to a gameover, Player victory.
   Field three does not end the game and leaves one field for the PC to take.  
   Field one leads to a gameover, PC victory.  
* Field three does not end the game and leaves two fields for the Player to take.
   Field one leads to a gameover, Player victory.
   Field two does not end the game and leaves one field for the PC to take.  
   Field one leads to a gameover, Draw. *note this is different than in the blog example, let's talk hypotethically.  

The PC taking field one is definitely a good result for the PC -> +1
The PC taking field two has multiple different outcomes.
* If the player takes field one, the player wins -> -1
* If the player takes field three, the game goes on.
   The PC has to take field one, PC wins -> +1
This result propagates upward, so on the player turn we have two possible outcomes, (+1,-1). As we assume the worst case for player turns the minimum is taken, so Field two is potentially a bad result for the PC overall -> -1
The PC taking field three again has multiple different outcomes.
* If the player takes field one, the player wins -> -1
* If the player takes field two, PC takes field one, Draw -> 0
Again we have two possible outcomes (0,-1) and again we have to assume the worst case. Field three is also a potentially bad result for the PC -1

The PC therefore has three fields to choose from.
Field 1 leads to a guaranteed victory -> +1
Field 2 and 3 lead to possible defeats -> -1
The maximum value path is taken and the PC chooses Field 1.

This example hopefully illustrates the thoughtprocess nicely. The PC checks all possible scenarios and discards those, where the player has at any point the opportunity to win the game.

Current disadvantages of my implementation:
* If multiple paths lead to the same outcome, a random path is chosen. This has particular impact on Turn 1, when all 3^9 boardstates are evaluated only to determine, that all of them lead to at least a guaranteed draw and to choose a random one. Also in some situations the PC will not take the "obvious" move to immediately win a game, but choose a different move that is guaranteed to win the game 2 turns later.
* Playing a game where you are guaranteed to never win is...not that much fun.