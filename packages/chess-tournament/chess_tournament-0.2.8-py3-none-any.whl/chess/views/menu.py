"""View for displaying the main menu and handling user interactions."""

import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class MenuView:
    """Handles the main menu and interactive submenus for the Chess Tournament."""

    def __init__(self, player_controller, match_controller, tournament_controller):
        """
        Initialize MenuView with controllers.

        Args:
            player_controller: Controller for player operations.
            match_controller: Controller for match operations.
            tournament_controller: Controller for tournament operations.
        """
        self.player_controller = player_controller
        self.match_controller = match_controller
        self.tournament_controller = tournament_controller
        self.running = True

        self.menu_options = [
            ("1", "Manage players", self.manage_players),
            ("2", "Manage matches", self.manage_matches),
            ("3", "Manage tournaments", self.manage_tournaments),
            ("0", "Exit", self.exit_app),
        ]

    def display_menu(self):
        """Display main menu and handle user choices until exit."""
        while self.running:
            print("\n=== Chess Tournament Menu ===")
            for key, desc, _ in self.menu_options:
                print(f"{key}. {desc}")
            choice = input("Enter your choice: ").strip()
            self.handle_choice(choice)

    def handle_choice(self, choice):
        """Execute the selected main menu action.

        Args:
            choice (str): User input representing menu selection.
        """
        for key, _, action in self.menu_options:
            if choice == key:
                action()
                return
        print(" Invalid choice, try again.")

    # --- Player management ---

    def add_player(self):
        """Interactively add a new player and validate input."""
        print("\n--- Add a Player ---")
        last_name = input("Enter last name: ").strip()
        first_name = input("Enter first name: ").strip()
        player_id = input("National ID (2 capital letters + 5 digits): ").strip()
        birth_date_str = input("Enter birth date (YYYY-MM-DD): ").strip()

        birth_date = None
        if birth_date_str:
            try:
                birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
            except ValueError:
                print(" Invalid date format. Use YYYY-MM-DD.")
                return

        success = self.player_controller.add_player(
            id_national=player_id,
            last_name=last_name,
            first_name=first_name,
            birthdate=birth_date,
        )

        if success:
            print(f" Player {first_name} {last_name} added successfully.")
        else:
            print(
                f" Failed to add player {first_name} {last_name}. "
                "Check ID format or duplication."
            )

    def list_players(self):
        """Display all registered players in alphabetical order."""
        players = self.player_controller.list_players()
        if not players:
            print("No players registered.")
            return
        print("\n=== Registered Players ===")
        for p in players:
            print(
                f"- {p.last_name} {p.first_name} | ID: {p.id_national} | "
                f"Birthdate: {p.birth_date}"
            )

    # --- Match management ---

    def list_matches(self):
        """Display all recorded matches with player names and results."""
        matches = self.match_controller.list_matches()
        if not matches:
            print("No matches recorded.")
            return
        print("\n=== Recorded Matches ===")
        for i, match in enumerate(matches, start=1):
            player_white = match.player_white
            player_black = match.player_black
            score_map = {(1, 0): "1-0", (0, 1): "0-1", (0.5, 0.5): "0.5-0.5"}
            score_str = score_map.get(
                tuple(match.score), f"{match.score[0]}-{match.score[1]}"
            )
            print(
                f"Match {i}: {player_white.first_name} "
                f"{player_white.last_name} vs "
                f"{player_black.first_name} {player_black.last_name} | "
                f"Result: {score_str}"
            )

    # --- Tournament management ---

    def create_tournament(self):
        """Interactively create a new tournament."""
        self.tournament_controller.create_tournament()

    def list_tournaments(self):
        """Display all tournaments available."""
        self.tournament_controller.list_tournaments()

    def add_players_to_tournament(self):
        """Add players to the selected tournament."""
        self.tournament_controller.add_players()

    def start_round(self):
        """Start the next round in the selected tournament."""
        self.tournament_controller.start_round()

    def enter_results(self):
        """Enter results for the current tournament round."""
        self.tournament_controller.enter_results()

    def show_standings(self):
        """Show current standings for the tournament."""
        self.tournament_controller.show_standings()

    def export_tournament_report(self):
        """Export the full tournament report to HTML."""
        self.tournament_controller.export_report()

    # --- Submenus ---

    def manage_players(self):
        """Display the player submenu and handle actions."""
        submenu = {
            "1": ("Add a player", self.add_player),
            "2": ("List players", self.list_players),
            "0": ("Back", None),
        }
        self._interactive_submenu("Player Menu", submenu)

    def manage_matches(self):
        """Display the match submenu and handle actions."""
        submenu = {
            "1": ("Create a match", self.match_controller.interactive_create_match),
            "2": ("List matches", self.list_matches),
            "0": ("Back", None),
        }
        self._interactive_submenu("Match Menu", submenu)

    def manage_tournaments(self):
        """Display the tournament submenu and handle actions."""
        submenu = {
            "1": ("Create a tournament", self.create_tournament),
            "2": ("List tournaments", self.list_tournaments),
            "3": ("Add players", self.add_players_to_tournament),
            "4": ("Start round", self.start_round),
            "5": ("Enter results", self.enter_results),
            "6": ("Show standings", self.show_standings),
            "7": ("Export tournament report", self.export_tournament_report),
            "0": ("Back", None),
        }
        self._interactive_submenu("Tournament Menu", submenu)

    def _interactive_submenu(self, title: str, submenu: dict):
        """
        Run a submenu loop until the user selects 'Back'.

        Args:
            title (str): The submenu title.
            submenu (dict): Dictionary mapping choice keys to (description, action).
        """
        choice = None
        while choice != "0":
            print(f"\n=== {title} ===")
            for key, (description, _) in submenu.items():
                print(f"{key}. {description}")
            choice = input("Enter your choice: ").strip()
            if choice in submenu:
                action = submenu[choice][1]
                if action:
                    action()
            elif choice != "0":
                print("Invalid choice, try again.")

    def exit_app(self):
        """Exit the application."""
        print(" Goodbye!")
        self.running = False
