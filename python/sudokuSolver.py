"""
Understanding Sudoku Rules

    The board is 9x9 and split into 9 smaller 3x3 squares
    Each row, column, and 3x3 square must have the numbers 1-9, with no repeats

Steps to Solve

    Start with a Sudoku board that has some numbers already in place
    Create a function to make sure a number fits in a spot without breaking the rules
    Use a method called backtracking to fill in numbers. This means you try options until you find the right one
    Keep going until all spots are filled

Backtracking Algorithm

This method involves trying different numbers in empty spots:

    Pick an empty spot
    Put in a number from 1-9 that fits
    Move to the next spot and repeat
    If you get stuck, go back and try a different number
    
"""