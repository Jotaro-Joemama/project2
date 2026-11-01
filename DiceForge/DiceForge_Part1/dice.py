"""
Program: DiceForge
Author: Makaden Eveland
Purpose: Define dice objects used by the DiceForge roller.
Resources: Original project concept based on the author's earlier dice roller.
Date: 2026-11-01
"""

import random


class Die:
    """Represent one die with a configurable number of sides."""

    def __init__(self, sides, rng=None):
        """Create a die and optionally accept a random-number generator."""
        if not isinstance(sides, int) or sides < 2:
            raise ValueError("A die must have at least 2 sides.")

        self.sides = sides
        self.rng = rng if rng is not None else random.Random()

    def roll(self):
        """Return one random result from 1 through the die's side count."""
        return self.rng.randint(1, self.sides)


class StandardDie(Die):
    """Represent a standard tabletop die such as a d4, d6, or d20."""

    def __init__(self, sides, rng=None):
        """Create a standard die after checking its side count."""
        if sides not in {4, 6, 8, 10, 12, 20, 100}:
            raise ValueError("Use a standard die: d4, d6, d8, d10, d12, d20, or d100.")
        super().__init__(sides, rng)
