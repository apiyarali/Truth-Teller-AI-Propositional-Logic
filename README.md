# Knights (True) and Knaves (False) Puzzle Solver (Propositional Logic AI Solver)

## Overview
This project implements a logic-based AI solver for "Knights and Knaves" puzzles, a type of logical puzzle introduced by Raymond Smullyan. In these puzzles, each character is either a knight (who always tells the truth) or a knave (who always lies). Given a set of statements made by the characters, the goal is to determine their identities using propositional logic and model checking.

## Files
- **logic.py**: Contains propositional logic classes and a model-checking function.
- **puzzle.py**: Defines the logic for solving Knights and Knaves puzzles, including knowledge bases for different puzzles.

## Puzzles Solved
The solver handles the following puzzles:

1. **Puzzle 0**
   - Single character (A) who states: "I am both a knight and a knave."
   - Logical reasoning determines A must be a knave.

2. **Puzzle 1**
   - Two characters (A and B)
   - A states: "We are both knaves."
   - B remains silent.
   - The solver determines the true identities of A and B.

3. **Puzzle 2**
   - Two characters (A and B)
   - A states: "We are the same kind."
   - B states: "We are of different kinds."
   - The solver logically deduces their identities.

4. **Puzzle 3**
   - Three characters (A, B, C)
   - A states either "I am a knight." or "I am a knave."
   - B says: "A said 'I am a knave.'"
   - B also says: "C is a knave."
   - C states: "A is a knight."
   - The solver determines the correct classification of A, B, and C.

## How It Works
The solver uses propositional logic to represent the rules of the puzzle. The knowledge bases contain:
- Structural rules (each character is either a knight or a knave, but not both).
- Logical translations of the statements given by characters.
- A model-checking algorithm to evaluate possible truth assignments and deduce correct solutions.

## Running the Solver
To execute the solver and see the solutions, run:
```sh
python puzzle.py
```
The output will display the correct classification of each character in all puzzles.

## Notes
- The solver follows a direct logical encoding of the given information (in logic.py file) rather than manually reasoning through solutions.

## Credits
Inspired by the logical puzzles of Raymond Smullyan and implemented as part of Harvard's CS80 AI curriculum.
