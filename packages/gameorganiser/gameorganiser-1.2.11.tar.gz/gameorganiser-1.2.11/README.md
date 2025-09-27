# Game Organizer

**Game Organizer** is a Python application that helps you easily organize your board and card games by allowing you to input your game collection along with shelving information (rows and columns). Perfect for keeping track of your collection in a structured way!

## Installation

Option 1:
```bash
pip install gameorganiser
```
Option 2: download the executable from the [releases page](https://github.com/dragonruler1000/Game-organizer/releases/latest)
Warning: there is a bug in the executable that causes it not to generate the JSON file used to save the data. Use the pip install method if you want to save data. I am working on fixing this issue.
## Usage

1. Run the main script/executable:

```bash
python main.py
```
```bash
. ubuntu-latest
```

```cmd
windows-latest.exe
```

2. Follow the prompts to:

   * Add a game to your collection
   * Input shelving information (number of rows and columns)
   * View your organized collection

Example:

```
python main.py 
Enter the game file name (e.g., games.json): games.json

Menu:
1. Add a new game
2. View all games
3. Export games to CSV
4. Save and exit
Enter your choice: 1
Enter game name: catan
Enter game type: board
Enter rows number: 3
Enter columns number: 5

Menu:
1. Add a new game
2. View all games
3. Export games to CSV
4. Save and exit
Enter your choice: 4
Attempting to save game data...
Game data saved. Exiting...
Press Enter to exit...

```

## Contributing

Contributions are welcome! Feel free to submit issues, suggest features, or submit pull requests.

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.