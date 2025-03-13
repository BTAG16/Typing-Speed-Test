# Typing Speed Test

This is a typing speed test game built with Python and Tkinter. The game allows users to test their typing speed by typing random words displayed on the screen. The speed is measured in both **characters per minute (CPM)** and **words per minute (WPM)**.

## Features

- **Difficulty Levels**: Select from four difficulty levels – Easy, Intermediate, Advanced, and Expert.
- **Typing Speed Measurement**: Track your performance with CPM and WPM calculations.
- **Game Over Screen**: See your results (correct words, CPM, and WPM) after completing the test.

## Tech Stack

- **Python 3.x**
- **Tkinter**: For creating the GUI.
- **Random Module**: For selecting random words.
- **Timeit Module**: For tracking time during the typing test.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/btag16/typing-speed-test.git
   cd typing-speed-test
   ```

2. Ensure you have Python 3.x installed.

3. You don't need to install external libraries as Tkinter comes pre-installed with Python.

## Usage

1. Run the script `main.py`:
   ```bash
   python main.py
   ```

2. Select a difficulty level from the available options (Easy, Intermediate, Advanced, Expert).

3. The game will display a random word for you to type.

4. Type the word in the text box and press **Done** or hit **Enter** on your keyboard.

5. After completing the game, the app will show your **number of attempts**, **characters per minute (CPM)**, and **words per minute (WPM)**.

## Game Logic

1. **Start Game**: When you press the "Start" button, a random word from the selected difficulty is shown.
2. **Typing Speed Calculation**: After typing the word correctly, the program measures the time taken and calculates CPM and WPM.
3. **Final Results**: Once you've completed 10 attempts, the game ends, and a "Game Over" screen shows your results.

## Word List

The words for the typing test are stored in `words.py`. They are categorized into four levels:

- **Easy**: Simple, short words.
- **Intermediate**: Moderate difficulty words.
- **Advanced**: Longer and more complex words.
- **Expert**: Challenging words.

## License

This project is licensed under the MIT License.

---

Feel free to contribute, suggest improvements, or ask questions by opening an issue in this repository.
