# KeyLoop 🎮

A powerful keyboard and mouse macro automation tool that automatically presses keys or clicks the mouse at regular intervals. Features hotkey controls for easy on/off toggling.

## Features

- ⌨️ **Keyboard & Mouse modes**: Choose between automated key presses or mouse clicks
- 🎯 **Customizable input**: Press any keyboard key or mouse button repeatedly
- ⏱️ **Adjustable interval**: Set custom time between actions (supports decimals)
- 🚀 **Hotkey controls**: Press 'i' to start/pause and 'q' to stop (much easier than Ctrl+C)
- ⏳ **Startup delay**: 2-second countdown before macro begins

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

### Configuration Prompts

1. **Choose mode** (1 for keyboard, 2 for mouse - default is keyboard)
   
2. **Specify your input**:
   - **Keyboard mode**: Enter the key to press (e.g., `space`, `a`, `enter`, `shift`, `ctrl`)
   - **Mouse mode**: Enter the button (e.g., `left`, `right`, `middle`)

3. **Enter the interval** in seconds between actions (default is 1)
   - Examples: `0.1`, `0.5`, `1`, `2`, `5`

### Controls

- **'i' key**: Start/Pause the macro (hotkey - suppressed input)
- **'q' key**: Stop the macro completely and exit (hotkey - suppressed input)
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

- **keyboard** (0.13.5) - Cross-platform keyboard event handling and hotkey detection
- **mouse** (0.7.1) - Cross-platform mouse control and clicking
- **colorama** (0.4.6) - Cross-platform colored terminal text

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

### Keyboard Mode
```
Welcome to KeyLoop

Choose mode - (1) Keyboard or (2) Mouse autoclicker (default is 1): 1
Enter the key you want to press (default is spacebar): space
Enter the time between presses in seconds (ex: 0.1, 0.5, 1, 2 - default is 1): 0.5

Starting in 2...
Press 'i' to start the macro.
Press 'q' to exit.
```

### Mouse Mode
```
Welcome to KeyLoop

Choose mode - (1) Keyboard or (2) Mouse autoclicker (default is 1): 2
Enter the mouse button (left/right/middle - default is left): left
Enter the time between presses in seconds (ex: 0.1, 0.5, 1, 2 - default is 1): 1

Starting in 2...
Press 'i' to start the macro.
Press 'q' to exit.
```

## Tips & Tricks

- **Gaming**: Great for repetitive tasks in games (e.g., auto-clicking, holding keys)
- **Testing**: Automate UI testing with repeated mouse clicks or key presses
- **Accessibility**: Useful for users who need assistance with repetitive keyboard/mouse tasks
- **AFK tasks**: Perfect for farming or gathering in games
- **Fine-tuning intervals**: Start with 0.1 seconds for fast actions, increase if needed for stability
```

This will press the spacebar every 2 seconds until you press 'q'.
