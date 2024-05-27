# Screenshotinator
Automate screenshot drudgery! This Python script captures your screen at set intervals, freeing you from repetitive clicking. Ideal for monitoring tasks or replacing tedious button mashing for screenshots.

## Table of content

- [Motivation](#motivation)
- [Installation & Usage](#installation--usage)
    - [Installation](#installation)
    - [Usage](#usage)
- [Contributing](#contributing)
- [History](#history)
- [Credits](#credits)
- [License](#license)

## Motivation
This Python script was born from the frustration of clicking a button in an outdated application to capture screenshots at regular intervals - automates the tedium and saves your sanity!

## Installation & Usage

### Installation
1. Download the contents of this repo and navigate to the screenshotinator directory using the terminal.
2. (Optional) Once in the directory you might want to create and activate a virtual environment using venv.
3. Install the dependancies:
    ```bash
    pip install -r requirements.txt
    ```




### Usage
1. Modify the script by specifying the following parameters:
   - **Coordinates of the screenshot area**: Define the region of the screen you want to capture.
   - **Number of repetitions**: Set how many times you want the screenshot to be taken.
   - **Time interval**: Specify the amount of time to wait between each repetition.
   - **Button click coordinates (optional)**: Provide the coordinates for any button that needs to be clicked in each repetition.
2. Run the script:
    ```bash
    python screenshotinator.py
    ```

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Added some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History
22/05/19: v1 published to github.  
08/06/22: v2 updated an error in the 'Contributing' section and added examples of project 'History'.  

## Credits
- Script created by <a href="https://iamzain.com">Zain Khan</a>
- Inspired by <a href="https://medium.com/analytics-vidhya/automate-gui-clicks-and-save-screenshots-fcbc9d52a08c">Syed Meesam Ali</a>
- Template for this README is <a href="https://github.com/gitzain/template-README">Template-README</a> created by <a href="https://iamzain.com">Zain Khan</a>

## License
See the LICENSE file in this project's directory.
