# KeyLoop 🎮

A simple keyboard macro automation tool that automatically presses a specified key at regular intervals.

## Features

- 🎯 **Customizable key**: Press any keyboard key repeatedly
- ⏱️ **Adjustable interval**: Set custom time between key presses
- 🛑 **Easy stop**: Press 'q' to stop the macro at any time

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. Clone or download this project
2. Navigate to the project directory
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python main.py
```

### Prompts

1. **Enter the key you want to press** (default is spacebar)
   - Examples: `space`, `a`, `enter`, `shift`, `ctrl`

2. **Enter the time between presses in seconds** (default is 1)
   - Examples: `0.5`, `2`, `5`

### Controls

- **'q' key**: Stop the macro immediately (suppressed - won't appear in terminal)
- **Ctrl+C**: Interrupt the macro (alternative way to stop)

## System Requirements & Cross-Platform Notes

### Windows ✅
- **Full support** - Works perfectly without any additional configuration
- Can run with regular user privileges

### macOS ⚠️
- **Requires permissions** - You may need to grant accessibility permissions
- Go to: System Preferences → Security & Privacy → Accessibility
- Add your terminal/IDE to the approved list
- May require running with elevated privileges

### Linux ⚠️
- **Requires elevated privileges** - Must run with `sudo`
- Some systems need to configure `/dev/uinput` permissions:
  ```bash
  sudo usermod -a -G input $USER
  ```

## Dependencies

- **keyboard** (0.13.5+) - Cross-platform keyboard event handling
- **colorama** (0.4.4+) - Cross-platform colored terminal text

See `requirements.txt` for exact versions.

## Troubleshooting

### "Permission denied" error on Linux/macOS
- Try running with `sudo`: `sudo python main.py`
- Or configure permissions as described above

### Keyboard events not detected
- Ensure the terminal window has focus
- On macOS, check System Preferences → Security & Privacy → Accessibility

### Key not working as expected
- Use the exact key name (e.g., `space` not `spacebar`)
- Check the `keyboard` library documentation for supported keys

### Colorama not working
- Reinstall: `pip install --upgrade colorama`
- Ensure terminal supports ANSI colors (most modern terminals do)

## Example Usage

```
Welcome to KeyLoop

Enter the key you want to press (default is spacebar): space
Enter the time between presses in seconds (default is 1): 2
Press 'q' to stop the macro.
```

This will press the spacebar every 2 seconds until you press 'q'.
