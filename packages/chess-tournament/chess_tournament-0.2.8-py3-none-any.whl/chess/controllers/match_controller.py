"""Controller for creating and viewing chess matches."""

import logging
from chess.models.match import Match
from chess.storage import load, save

logger = logging.getLogger(__name__)


class MatchController:
    """Handles the creation and viewing of matches."""

    def __init__(self, player_controller):
        self.player_controller = player_controller
        logger.debug("Initializing MatchController")
        self.matches = [Match.from_dict(m) for m in load("matches")]

    def save_matches(self):
        """Save the current list of matches via storage.py."""
        save("matches", [m.to_dict() for m in self.matches])
        logger.info("Matches saved via storage.py")

    def interactive_create_match(self):
        """Interactively prompts the user to create a new match."""
        print("\n--- Create a Match ---")
        id1 = input("Enter first player's national ID: ").strip()
        id2 = input("Enter second player's national ID: ").strip()
        result = input("Enter result (1 for win, 2 for loss, 0 for draw): ").strip()
        self.create_match(id1, id2, result)

    def create_match(self, id1, id2, result):
        """Create a new match between two players with the given result."""
        p_white = self.player_controller.find_player_by_id(id1)
        p_black = self.player_controller.find_player_by_id(id2)

        if not p_white or not p_black:
            logger.error("One or both player IDs not found: %s, %s", id1, id2)
            return False

        if id1 == id2:
            logger.warning("A player cannot play against themselves: id=%s", id1)
            return False

        score_map = {"1": [1, 0], "2": [0, 1], "0": [0.5, 0.5]}
        score = score_map.get(result)
        if score is None:
            logger.error("Invalid result provided: %s", result)
            return False

        new_match = Match(player_white=p_white, player_black=p_black, score=score)
        self.matches.append(new_match)
        self.save_matches()
        logger.info(
            "Match created between %s %s and %s %s with score %s",
            p_white.first_name,
            p_white.last_name,
            p_black.first_name,
            p_black.last_name,
            score,
        )
        return True

    def list_matches(self):
        """Return the list of all matches."""
        # Always reload from storage to avoid stale data
        self.matches = [Match.from_dict(m) for m in load("matches")]
        logger.debug("Returning match list (%d items)", len(self.matches))
        return self.matches
