discord_modules = ['nextcord', 'disnake', 'discord']
discord = None
discord_errors = None

for module in discord_modules:
    try:
        discord = __import__(module)
        discord.module = module
        # Attempt to import DiscordException, which is a common base for discord errors
        # If the specific 'discord_errors' is something else, this might need adjustment
        if hasattr(discord, 'DiscordException'):
            discord_errors = discord.DiscordException
        elif hasattr(discord, 'HTTPException'): # Fallback for older versions or specific error types
            discord_errors = discord.HTTPException
        break
    except ImportError:
        continue

if discord is None:
    raise ImportError("Could not find any of the discord modules: nextcord, disnake, or discord")

if discord_errors is None:
    # If DiscordException or HTTPException are not found, we might need to define a generic error
    # or raise a more specific error indicating the problem.
    # For now, we'll try to use a generic Exception if no specific discord error is found.
    # This might not be ideal for chat_exporter, but it will prevent the ImportError.
    try:
        from discord import DiscordException as discord_errors
    except ImportError:
        try:
            from discord import HTTPException as discord_errors
        except ImportError:
            discord_errors = Exception # Generic fallback
