"""Controller for player-related operations in the Chess Tournament Software."""

import logging
import re
import unicodedata
from datetime import datetime, date

from chess.models.player import Player
from chess.storage import load, save

logger = logging.getLogger(__name__)


class PlayerController:
    """Handles player-related operations."""

    def __init__(self):
        logger.info("PlayerController initialized")
        self.players = [Player.from_dict(p) for p in load("players")]

    def is_valid_id(self, id_national):
        """Validate national ID format: two letters + five digits."""
        return bool(re.fullmatch(r"[A-Z]{2}\d{5}", id_national))

    def player_exists(self, id_national: str) -> bool:
        """Check if a player with this ID already exists."""
        return any(p.id_national == id_national for p in self.players)

    def is_valid_name(self, name: str) -> bool:
        """Validate name contains letters, spaces, or hyphens, and is non-empty."""
        return bool(re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ\- ]+", name.strip()))

    def is_valid_birthdate(self, birthdate):
        """Validate birthdate format: YYYY-MM-DD."""
        try:
            datetime.strptime(birthdate, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def add_player(self, id_national, last_name, first_name, birthdate):
        """Add a new player with full details."""
        logger.debug(
            "Trying to add player: %s %s (%s)", first_name, last_name, id_national
        )

        if not self.is_valid_id(id_national):
            logger.warning("Invalid player ID format: %s", id_national)
            return False

        if self.player_exists(id_national):
            logger.warning("Duplicate player ID: %s", id_national)
            return False

        if isinstance(birthdate, str):
            if not self.is_valid_birthdate(birthdate):
                logger.warning("Invalid birthdate format: %s", birthdate)
                return False
            birthdate_iso = birthdate
        elif isinstance(birthdate, date):
            birthdate_iso = birthdate.isoformat()
        else:
            logger.warning("Birthdate type not recognized: %s", type(birthdate))
            return False

        new_player = Player(
            last_name=last_name.strip(),
            first_name=first_name.strip(),
            birth_date=birthdate_iso,
            id_national=id_national,
        )

        self.players.append(new_player)
        save("players", [p.to_dict() for p in self.players])
        logger.info(
            "Player added successfully: %s %s (%s)", first_name, last_name, id_national
        )
        return True

    def list_players(self):
        """Return the list of all players sorted alphabetically
        by last_name, first_name, then id_national."""
        logger.debug("Listing %d players (sorted)", len(self.players))
        return sorted(
            self.players,
            key=lambda p: (
                self._normalize_for_sort(p.last_name),
                self._normalize_for_sort(p.first_name),
                p.id_national,
            ),
        )

    def _normalize_for_sort(self, s: str) -> str:
        """Normalize a string for sorting: remove accents and lowercase."""
        normalized = unicodedata.normalize("NFKD", s)
        return normalized.encode("ASCII", "ignore").decode("utf-8").casefold()

    def find_player_by_id(self, player_id):
        """Find and return a player object by their national ID.
        Returns None if not found."""
        for player_obj in self.players:
            if player_obj.id_national == player_id:
                return player_obj
        return None
