"""Model for representing a chess match between two players."""

import logging
from .player import Player

logger = logging.getLogger(__name__)


class Match:
    """Represents a match between two players."""

    def __init__(
        self, player_white: Player, player_black: Player, score: list | None = None
    ):
        """Initialize a Match instance with two players and their scores.

        Args:
            player_white: The first player.
            player_black: The second player.
            score: A list with two elements [score1, score2]
            or None (not yet played).
        """
        self.player_white = player_white
        self.player_black = player_black
        self.score = score if score is not None else [None, None]
        logger.debug(
            "Creating Match: %s vs %s, score: %s",
            player_white,
            player_black,
            self.score,
        )

    def is_played(self) -> bool:
        """Return True if the match has a valid result entered."""
        return all(s is not None for s in self.score)

    def __str__(self):
        score_white = self.score[0] if self.score[0] is not None else "-"
        score_black = self.score[1] if self.score[1] is not None else "-"
        return (
            f"{self.player_white.last_name} vs {self.player_black.last_name} :"
            f"{score_white}-{score_black}"
        )

    def to_dict(self):
        """Converts the Match object to a dictionary for serialization."""
        logger.debug("Converting Match to dict")
        return {
            "player_white": self.player_white.to_dict(),
            "player_black": self.player_black.to_dict(),
            "score": self.score,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Match instance from a dictionary."""
        player_white = Player.from_dict(data["player_white"])
        player_black = Player.from_dict(data["player_black"])
        logger.debug("Creating Match from dict: %s", data)
        return cls(
            player_white=player_white,
            player_black=player_black,
            score=data["score"],
        )
