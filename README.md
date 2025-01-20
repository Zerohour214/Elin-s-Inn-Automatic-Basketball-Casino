# Mouse Click and Hold Automation
 
* Elin's Inn Automated Basketball Casino (ABC) is a simple Python tool to automatically play the Basketball game which is the most efficient way to make Casino Chips for Ether Potions. 
* The tool automate mouse click and hold actions at specified coordinates for a given duration and number of repetitions. "0.55" is the optimal duration to get a perfect score.
* It is built using Python and the `tkinter` library for the GUI, and `pyautogui` for mouse automation.

## Description

The application allows users to:
- Enter X and Y coordinates for the mouse click.
- Specify the duration (in seconds) for which the mouse button should be held down.
- Specify the number of repetitions for the click and hold action.
- Retrieve the current mouse position.
- Start the click and hold action with a button click or keyboard shortcut.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Zerohour214/mouse-click-hold-automation.git
   cd mouse-click-hold-automation
   ```

2. **Install the required dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Install PyInstaller** (if you want to compile the script into an executable):
   ```sh
   pip install pyinstaller
   ```

## How to Use

1. **Run the application || The .exe (Which is provided on release page)**:
   ```sh
   python main.py
   ```

2. **Use the GUI**:
   - Enter the X and Y coordinates in the respective fields.
   - Enter the duration (in seconds) for which the mouse button should be held down.
   - Enter the number of repetitions for the click and hold action.
   - Click the "Get Mouse Position(F5)" button || press F5 to retrieve the current mouse position.
   - Click the "Start(F6)" or press F6 button to start the click and hold action.

3. **Keyboard Shortcuts**:
   - Press `F5` to get the current mouse position.
   - Press `F6` to start the click and hold action.

4. **Compile to an Executable** (optional):
   - Run the following command to create a single executable file:
     ```sh
     pyinstaller --onefile main.py
     ```
   - The executable file will be located in the `dist` directory.

## License

This project is licensed under the MIT License.
```