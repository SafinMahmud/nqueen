# nqueen
I used local search algorithm to solve this constraint satisfaction problem.
Because Backtracking takes a lot time to solve this n queen problem.

First I put randomly n number of queens in n columns.
so there is one queen in every row. 
But there can be multiple queens in one row. Because the row is chosen randomly
and then I stored the row number where queen exits in a list.

Then I started finding which column's queen is attacking maximum number of queen
then i changed that queen's row position in that column.
to where it is attacking less number of queen from it's previous position.
Thus minimizing the number of violations in every iterations.
and in every iteration i am calculating the sum of all the violations(number of queens the queen is attacking) of every queen.
Until that sum is zero meaning no queen is attacking any other queen the loop will continue.

After the loop ends N queens will be placed on an N x N chessboard so that no two queens attack each other.
