# Tic Tac Toe

This game is all about two players taking turns entering X or O in a board and trying to connect three in a line to win the game.

This version uses Greg Surma's "Unbeatable AI" algorithm to make it a frustrating single player experience.

## Algorithm

[https://gsurma.medium.com/tic-tac-toe-creating-unbeatable-ai-with-minimax-algorithm-8af9e52c1e7d#14e6](Greg Surma's blog post can be found here)

The algorithm essentially simulates all possible turns that any player can do in any of the upcoming turns and assigns a value to the outcomes. A "1" denotes a win for the computer, a "-1" a win for the Player, a "0" a draw. The results then get propagated backwards, and the previous decisions leading to these outcomes get assigned the values of the outcomes. A min/max approach follows, where for player turns the worst result gets propagated upwards as a "worst case if the computer takes this turn", while for computer turns the best result gets propagated upwards as a "this would be a good turn for the computer to take" until at the highest level the computer has a clear idea of possible outcomes for each of their turns and only takes one, that's guaranteed to end in at least a draw.

To use the example also given in the blog post, assuming the PC has three possible fields to put their "X" in.
* Field one leads to a gameover, PC victory.
* Field two does not end the game and leaves two fields for the Player to take.
** Field one leads to a gameover, Player victory.
** Field three does not end the game and leaves one field for the PC to take.
*** Field one leads to a gameover, PC victory.
* Field three does not end the game and leaves two fields for the Player to take.
** Field one leads to a gameover, Player victory.
** Field two does not end the game and leaves one field for the PC to take.
*** Field three leads to a gameover, PC victory.