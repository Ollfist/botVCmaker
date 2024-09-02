# Bot Voice Channel Maker

This is my attempt to create a Discord bot with Discord API.
This code works as follows: 
When the program starts, it connects to the bot by its token taken from the “.env” file, then when a server participant connects to a voice channel (hereafter VC) for example: “create”, a separate VC will be created and then the participant who created it will be moved to the newly created VC. If all members in the VC quit from VC, the created VC will be deleted.

P.S Don't forget to change the token value in the “.env” file to your own, without the quotes.