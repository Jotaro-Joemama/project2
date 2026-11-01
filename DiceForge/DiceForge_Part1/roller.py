"""
Program: DiceForge
Author: Makaden Eveland
Purpose: Parse dice expressions and calculate their results.
Resources: Original project concept based on the author's earlier dice roller.
Date: 2026-11-01
"""

import random
import re

from dice import StandardDie


class DiceRoller:
    """Roll dice expressions such as 2d6+3 or 1d20-2."""

    EXPRESSION_PATTERN = re.compile(r"^(\d*)d(4|6|8|10|12|20|100)([+-]\d+)?$", re.IGNORECASE)

    def __init__(self, rng=None):
        """Create a roller with an optional random-number generator."""
        self.rng = rng if rng is not None else random.Random()

    def parse_expression(self, expression):
        """Validate an expression and return its dice count, sides, and modifier."""
        if not isinstance(expression, str):
            raise ValueError("Enter the expression as text.")

        cleaned = expression.replace(" ", "").lower()
        match = self.EXPRESSION_PATTERN.fullmatch(cleaned)

        if match is None:
            raise ValueError("Use a format like 1d20, 2d6+3, or 4d8-1.")

        count_text, sides_text, modifier_text = match.groups()
        count = int(count_text) if count_text else 1
        sides = int(sides_text)
        modifier = int(modifier_text) if modifier_text else 0

        if count < 1 or count > 100:
            raise ValueError("You can roll between 1 and 100 dice at a time.")

        return count, sides, modifier

    def roll(self, expression):
        """Roll an expression and return its details in a dictionary."""
        count, sides, modifier = self.parse_expression(expression)
        die = StandardDie(sides, self.rng)
        rolls = [die.roll() for _ in range(count)]
        total = sum(rolls) + modifier

        return {
            "expression": expression.replace(" ", "").lower(),
            "rolls": rolls,
            "modifier": modifier,
            "total": total,
        }
