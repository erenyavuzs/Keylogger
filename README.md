# Keyboard Logger

A simple and lightweight Python script that logs keyboard activity with timestamps using the `pynput` library. Ideal for monitoring key presses for educational purposes.

## Features

- **Real-time Key Logging:** Records both alphanumeric and special keys.
- **Timestamping:** Each key press is logged with a precise timestamp.
- **Log File:** Logs are saved in a `log.csv` file for easy analysis.
- **Graceful Exit:** Press the `Esc` key to stop the logging process.

## Requirements

- Python 3.x
- `pynput` library

## Installation

To set up the Keyboard Logger on your local machine, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/erenyavuzs/keylogger.git
    cd keylogger
    ```

2. **Set Up a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install pynput
    ```
    <br>
    Or
    ```bash
    pip install -r requirements.txt
    ```

   
    

## Usage

1. **Run the Script:**
    ```bash
    python3 keylogger.py
    ```

2. **Stopping the Logger:**
    - To stop the logging process, press the `Esc` key. The script will terminate and stop recording key presses.

## Example Log Entry

The `log.csv` file will contain entries like this:
<br>
2024-08-06 14:55:32.123743 a <br>
2024-08-06 14:55:33.456854 Key.space <br>
2024-08-06 14:55:34.789643 Key.enter 
