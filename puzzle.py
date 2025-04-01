from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# Intial condition for charcters A, B, C
# Charcter can be a knight or knave but not knight and knave
ConditionA = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave))
)

ConditionB = And(
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave))
)

ConditionC = And(
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave))
)

# Puzzle 0
# A says "I am both a knight and a knave."

# Puzzle0 Information
# A is a knight and a knave
A0 = And(AKnight, AKnave)

knowledge0 = And(

    # Initial Condition
    ConditionA,

    # Implication
    # If A is a knight thne A has to be both knight and a knave
    Implication(AKnight, A0),
    # If A is a knave then A cannot be both a knight and a knave
    Implication(AKnave, Not(A0)),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.

# Puzzle1 Information
# A and B are both knaves
A1 = And(AKnave, BKnave)

knowledge1 = And(

    # Initial Condition
    ConditionA,
    ConditionB,

    # Implication
    # If A is a knight then A and B have to be knave
    Implication(AKnight, A1),
    # else if A is a knave then A and B cannot be both knaves
    Implication(AKnave, Not(A1)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

# Puzzle2 Information
# A and B are both knights or kanve
A2 = Or(And(AKnight, BKnight), And(AKnave, BKnave))
# A is a knight and B is a knave or A is a knave and B is knight
B2 = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(

    # Initial Condition
    ConditionA,
    ConditionB,

    # Implication
    # If A is knight then A and B have to B knights or have to be kanves
    Implication(AKnight, A2),
    # else if A is a knave then B is a Knight
    Implication(AKnave, Not(A2)),
    # If B is a knight then A is knave
    Implication(BKnight, B2),
    # If B is a knave then A is knight or knave
    Implication(BKnave, Not(B2))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

# Puzzle3 Information
# If A is a knight then A must be a knight
A3_knight = And(
    Implication(AKnight, AKnight),
    Implication(AKnave, Not(AKnight))
)
# If A is knave then A must have said "I am knight"
A3_knave = And(
    Implication(AKnight, AKnave),
    Implication(AKnave, Not(AKnave))
)

knowledge3 = And(

    # Initial Condtion
    ConditionA,
    ConditionB,
    ConditionC,

    # Implication
    # A is either a knight or a knave
    Or(A3_knight, A3_knave),
    # If B is knight then A is knave and C is knave
    Implication(BKnight, And(A3_knave, CKnave)),
    # If B is knave then A is not knave and C is not knave
    Implication(BKnave, And(Not(A3_knave), Not(CKnave))),
    # If C is a knight then A is knight
    Implication(CKnight, AKnight),
    # If C is a knave then A is not a knight
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
