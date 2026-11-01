"""
Program: DiceForge
Author: Makaden Eveland
Purpose: Provide the command-line entry point for the DiceForge application.
Resources: Original project concept based on the author's earlier dice roller.
Date: 2026-11-01
"""

from roller import DiceRoller


def main():
    """Run the DiceForge command-line application."""
    roller = DiceRoller()

    print("=" * 36)
    print("             DICEFORGE")
    print("=" * 36)
    print("Enter a dice expression such as 1d20, 2d6+3, or 4d8-1.")
    print("Type q to quit.")

    while True:
        expression = input("\nDice expression: ").strip()

        if expression.lower() in {"q", "quit", "exit"}:
            print("Thanks for using DiceForge!")
            break

        try:
            result = roller.roll(expression)
            print(f"Roll: {result['expression']}")
            print(f"Individual dice: {result['rolls']}")
            print(f"Modifier: {result['modifier']:+}")
            print(f"Total: {result['total']}")
        except ValueError as error:
            print(f"Invalid expression: {error}")


if __name__ == "__main__":
    main()
