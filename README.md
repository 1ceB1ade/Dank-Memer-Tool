# Dank Memer Tool

This tool automates certain tasks in the Dank Memer Discord bot, allowing users to perform actions such as typing commands and clicking buttons.

## Description

Dank Memer Tool is a Python script designed to streamline interactions with the Dank Memer bot in Discord. It provides functionalities to automate tasks like typing commands and clicking buttons on the screen.

## Features

- **Command Typing**: Automatically types commands such as `/beg`, `/hunt`, and more, at configurable intervals.
- **Button Clicking**: Scans the screen for specific button images and clicks on them when detected.
- **Configurability**: Configurable via a `config.json` file, allowing users to customize text inputs, keybinds, and button images.

## Requirements

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/1ceB1ade/dank-memer-tool.git
    ```

2. Navigate to the project directory:

    ```bash
    cd dank-memer-tool
    ```

3. Install the required Python modules:

    ```bash
    pip install -r requirements.txt / Run the .bat file
    ```

## Usage

1. Configure the `config.json` file with your desired settings.
2. Run the `main.py` script:

    ```bash
    python main.py / Run the .bat file
    ```

3. Use the toggle keybind (default is Insert) to enable/disable the tool.
4. Press F2 to exit the tool.

## Configuration

The `config.json` file contains the following settings:

- `beg_text`: The text to be typed for the "/beg" command.
- `hunt_text`: The text to be typed for the "/hunt" command.
- `crime_text`: The text to be typed for the "/crime" command.
- `deposit_text`: The text to be typed for the "/deposit" command.
- `toggle_keybind`: The keybind to toggle the tool on/off.
- `button_images`: List of button images for the tool to click on.

## Disclaimer

This tool is provided for educational and personal use only. Any misuse or abuse of this tool for malicious purposes is strictly prohibited. The creator(s) of this tool are not responsible for any damages caused by the misuse of this tool.


## Contributing

Contributions are welcome! Feel free to open issues for any bugs or feature requests, or submit pull requests with improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
