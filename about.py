def about():
    print("""
Adventure RPG Game
Overview

Welcome to Adventure RPG Game, a turn-based role-playing game where you take on the role of a hero battling fearsome monsters, collecting powerful weapons, and leveling up to take on even greater challenges. Your wits, strategy, and preparation will determine your fate!

Features

    Combat System: Engage in turn-based battles with various monsters.
    Inventory Management: Equip weapons, use items, and manage your inventory wisely.
    Character Progression: Gain experience, level up, and enhance your stats to grow stronger.
    Exploration: Encounter random weapons and items during your journey to assist in battles.
    Challenging Enemies: Fight a variety of enemies including Skeletons, Falmer, Dragons, and the powerful Boss.

Getting Started
Prerequisites

To run this game, ensure you have the following installed:

    Python 3.7 or later
    A terminal or console that supports Python execution

Installation

    Clone the repository or download the project files.
    Ensure all required files (weapons.py, items.py, caracters.py, and the main game file) are in the same directory.

How to Play

    Run the game in your terminal:

    python main.py

    Follow the prompts to:
        Fight monsters.
        Choose weapons and items from your inventory.
        Level up and progress your hero.

    Combat:
        Choose from available weapons to attack.
        Open your inventory to use items or check your equipment.
        Survive enemy attacks and defeat them to earn experience points.

    Inventory Management:
        Collect new items and weapons during exploration.
        Replace weaker weapons if your inventory is full.

Game Mechanics
Hero Stats

    Health (HP): Determines how much damage you can take before being defeated.
    Attack: Determines how much damage you deal.
    Defense: Reduces the damage you take from enemies.
    Level: Gain levels by earning experience points (XP) to boost your stats.

Weapons

Each weapon has:

    Damage: The amount of attack power it adds.
    Miss Rate: The likelihood of an attack missing the target.

Items

    Items can restore health or provide other benefits during battles.

Enemies

    Different enemies have unique stats and difficulty levels, including:
        Skeleton: A beginner-level enemy.
        Falmer: A mid-tier enemy with stronger stats.
        Dragons: High-level enemies requiring strategy to defeat.
        Boss: The ultimate challenge with the highest stats.

Code Structure
Files

    main.py:
        Contains the main game logic, including the fight loop and inventory interactions.

    weapons.py:
        Defines all available weapons with their attributes (damage, miss_rate, etc.).

    items.py:
        Defines usable items such as health potions and other tools.

    caracters.py:
        Defines the hero and enemies, along with their stats and methods.

Key Classes

    caracters: Base class for all characters in the game.
    hero: A subclass of caracters representing the player. Includes additional features like leveling up and inventory management.
    weapons: Defines various weapons the hero can use.
    items: Defines items the hero can collect and use.

Future Improvements

    Add more enemy types and randomized encounters.
    Introduce new weapons and items with unique abilities.
    Expand the world with exploration features.
    Implement a save/load system for game progress.

Contact

For suggestions or issues, feel free to reach out or submit an issue in the repository.

Enjoy your adventure and good luck, hero! 🌟
""")
