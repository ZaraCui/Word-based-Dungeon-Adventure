# Word-based Dungeon Adventure 😎

A simple **text-based dungeon crawler game** written in Python.
This project demonstrates recursion, randomness, and user interaction through the console.

## Features

* **Recursive Storytelling**: No loops — the game flow relies purely on recursion.

* **Random Encounters**: Each encounter is chosen randomly, with equal probability:

  1. **Descending Stairs**

     * Ask the player whether to go down.
     * If yes → display a staircase (random size 1–10).
     * If no → display refusal message.
  2. **Treasure Found**

     * 90% chance: **Square gem** (prints a recursive square).
     * 10% chance: **Rare diamond** (prints a recursive diamond, odd size 1–15).
  3. **Mirror Realm**

     * Player enters text → program reverses it recursively.
  4. **Mysterious Stranger**

     * Stranger generates sentences from a grammar structure file (`stranger_structure.txt`).

* **ASCII Art**: Recursive printing of stairs, squares, and diamonds.

* **Interactive Input**: Decisions affect what you see in the dungeon.

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. Make sure you have Python 3 installed.

3. Run the game:

   ```bash
   python "Word-based dungeon adventure😎.py"
   ```

4. Follow the prompts in the console:

   * Enter how many encounters you want.
   * Respond to stairs, mirror, and other challenges.
   * Enjoy your adventure!

## File Structure

```
.
├── Word-based dungeon adventure😎.py   # Main game script
└── stranger_structure.txt              # Grammar rules for stranger’s sentences
├── test_game.py                       
└── README.md                          

```

## Example Gameplay

```
You enter the dungeon...
How many encounters would you like to have? 2
You've found some descending stairs, would you like to go down? y
▥
▥▥
▥▥▥
You found a square gem!
◆◆◆
◆ ◆
◆◆◆
```

## Concepts Demonstrated

* Recursion instead of iteration
* Randomized encounters and structures
* File-based grammar-driven text generation
* String manipulation and ASCII art

## License

This project is provided for educational purposes. Feel free to modify and extend it.
