Triangle Puzzle (Local Search)
------------------------------

Solve the triangle puzzle using local search strategies.  Simulated annealing is
strongly recommended.  A two minute (120 second) time limit will be enforced 
per puzzle.

It is requested that the solver program receive the puzzle either as standard 
input, or as a filename on the command line.

In the first case, this shell script would ask the program to solve all puzzles:

    for p in puzzles/*; do
        cat $p | ./solver
    done

In the second case, this is how we would ask the program to solve all puzzles:

    for p in puzzles/*; do
        ./solver $p
    done


Requirements
------------

- Provide a program to solve triangle puzzles using local search
- Puzzles will have no more than 4 rows.
- Time will be limited to 120 seconds per puzzle.
- Provide a README(.txt|.md) with information on running the program on a single puzzle.
- The program should not need to be edited to change the puzzle input file.
- Submit via the git repository for this assignment.


Input File Format
-----------------

A single puzzle file will have the format:

    load
    
    number_of_rows
    number_of_animals
    piece_1
    piece_2
    ...
    piece_n
    row_1_left
    row_2_left
    ...
    row_n_left
    row_1_right
    row_2_right
    ...
    row_n_right
    bottom_1
    bottom_2
    ...
    bottom_n


    solve hillclimb


The lines with "load", "solve hillclimb", or blanks should be
ignored.

- `number_of_rows` an integer, the number of rows in the puzzle
- `number_of_animals` an integer, the maximum number of animals
- `piece_x` a 3 character string, one character per edge, in clockwise order
- `row_x_left` a 1 character string, the character on the border for row x
- `row_x_right` a 1 character string, the character on the border for row x
- `bottom_x` a 1 character string, the character on bottom border, position x

Sample File
-----------

    load

    3
    5
    BDc
    Cca
    Cbd
    ECE
    ccB
    eeA
    CCC
    ebb
    aab
    A
    A
    E
    A
    B
    c
    a
    B
    c


    solve hillclimb

This is a 3 row puzzle, with 5 animals: Aa, Bb, Cc, Dd, and Ee.  Since it
is a 3 row puzzle, there are 1+3+5 = 9 pieces, and 3 + 3 + 3 = 9 border
characters.


Output Format
------------------

The program's output will have the following format
A single puzzle file will have the format:

    piece_1
    piece_2
    ...
    piece_n


- The pieces will be listed from top row to bottom row, with each
  row listed from left to right.
- An individual piece will have its left-most edge displayed
  first, and edges in clockwise order.
  

Sample File
-----------

    aab
    aCc
    cBc
    Cbd
    eeA
    ECE
    ebb
    BDc
    CCC

This is a solution to the sample input file above.


