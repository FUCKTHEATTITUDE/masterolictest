class Script(object):
    START_TXT = """Hello {},

My name is <a href=https://t.me/{}>{}</a>!

<b>I can provide Movies. A Telegram Auto Filter Bot. Its Easy To Use Me :)

Just Add me to Your Group As Admin, Hit The Help Button For More Info..</b>"""

    HELP_TXT = """Hey {}

<b>Here Is The Help For My Commands.</b>

/start - C𝗁𝖾𝖼𝗄 W𝗁𝖾𝗍𝗁𝖾𝗋 a𝗆 O𝗇𝗅𝗂𝗇𝖾 
/help - G𝖾𝗍 T𝗁𝗂𝗌 H𝖾𝗅𝗉 M𝖾𝗌𝗌𝖺𝗀𝖾
/about - A𝖻𝗈𝗎𝗍 M𝖾"""

    ABOUT_TXT = """<b>➥ 𝙈𝙮 𝙉𝙖𝙢𝙚 : {}

➥ 𝘾𝙧𝙚𝙖𝙩𝙤𝙧 : <a href='https://t.me/Y2say'>Dhanush-TG</a>

➥ 𝙇𝙞𝙗𝙧𝙖𝙧𝙮 : <a href='https://docs.pyrogram.org/'>Pyrogram</a>

➥ 𝙇𝙖𝙣𝙜𝙪𝙖𝙜𝙚 : Python 𝟹

➥ 𝘿𝙖𝙩𝙖 𝘽𝙖𝙨𝙚 : <a href='https://www.mongodb.com/'>MongoDB</a>

➥ 𝘽𝙤𝙩 𝙎𝙚𝙧𝙫𝙚𝙧 : <a href='https://heroku.com'>Heroku</a>

➥ 𝘽𝙪𝙞𝙡𝙙 𝙎𝙩𝙖𝙩𝙪𝙨 : v2.0.1 [ Beta ]"""

    SOURCE_TXT = """<b>Source:</b>
Dhanush is not a Open source project.

𝖲𝖮𝖴𝖱𝖢𝖤 𝖢𝖮𝖣𝖤 ~ 𝖭𝖮𝖳 𝖠𝖵𝖠𝖨𝖫𝖠𝖡𝖫𝖤 𝖱𝖨𝖦𝖧𝖳 𝖭𝖮𝖶</b>

<b>𝖮𝖳𝖧𝖤𝖱 𝖪𝖨𝖭𝖣 𝖡𝖮𝖳𝖲:</b>
<b>𝖠𝖴𝖳𝖮 𝖥𝖨𝖫𝖳𝖤𝖱</b> : <a href='https://github.com/EvamariaTG/EvaMaria'>𝖤𝗏𝖺 𝖬𝖺𝗋𝗂𝖺</a>
<b>𝖲𝖮𝖭𝖦</b> :  <a href='https://github.com/AsmSafone/RadioPlayerV2'>𝖠𝗌𝗆𝖲𝖺𝖿𝗈𝗇𝖾</a>
<b>𝖥𝖨𝖫𝖳𝖤𝖱</b> : <a href='https://github.com/TroJanzHEX/Unlimited-Filter-Bot'>𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽 𝖥𝗂𝗅𝗍𝖾𝗋 𝖡𝗈𝗍</a>
<b>PLUGINS</b> : <a href='https://github.com/EvamariaTG/EvaMaria'>Eva Maria</a>

<b>DEVS:</b>
- <a href='https://t.me/Naveen_TG'>Naveen-TG</a>"""

    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Dhamush should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - add a filter in chat.
• /filters - list all the filters of a chat.
• /del - delete a specific filter in chat.
• /delall - delete the whole filters in a chat (chat owner only)."""

    WARN_TXT = """Here is the help for the <b>Warns</b> module:

Keep your members in check with warnings; stop them getting out of control!
If you're looking for automated warnings, read about the blacklist module!

<b>Admin Commands</b>:
- /warn <reason>: Warn a user.
- /dwarn <reason>: Warn a user by reply, and delete their message.
- /swarn <reason>: Silently warn a user, and delete your message.
- /warns: See a user's warnings.
- /rmwarn: Remove a user's latest warning.
- /resetwarn: Reset all of a user's warnings to 0.
- /resetallwarns: Delete all the warnings in a chat. All users return to 0 warns.
- /warnings: Get the chat's warning settings.
- /setwarnmode <ban/kick/mute>: Set the chat's warn mode.
- /setwarnlimit <number>: Set the number of warnings before users are punished.

<b>Examples</b>
- Warn a user.
-> /warn @user For disobeying the rules"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- Dhanush Support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Dhanush supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/josprojects)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    FILLINGS_TXT = """Help: <b>Fillings</b>

You can also customise the contents of your message with contextual data. For example, you could mention a user by name in the filter message, or mention them in a filter!

<b>Supported fillings:</b>
- <code>{first}</code>: The user's first name.
- <code>{last}</code>: The user's last name.
- <code>{fullname}</code>: The user's full name.
- <code{username}</code>: The user's username.
- <code>{mention}</code>: Mentions the user with their firstname.
- <code>{id}</code>: The user's ID.
- <code>{dcid}</code>: The user's DC ID.
- <code>{chatname}</code>: The chat's name.
- <code>{query}</code>: Any Message Text.

<b>Example:</b>
<b>- Save a filter using the mention.</b>
-> <code>/filter test Hello {mention} This Is your Username : {username} And This Is your ID : {id}.</code>
"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    TORRENT_TXT = """Help: <b>Torrent Search</b>

<b>Commands and Usage:</b>
• /torrent or /tor <movie name>: Get Your Torrent Link From Various Resource.
<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
 /connect  - connect a particular chat to your PM.
• /disconnect  - disconnect from a chat.
• /connections - list all your connections."""
    
    TORRENT_TXT = """Help: <b>Torrent Search</b>

<b>Commands and Usage:</b>
• /torrent or /tor <movie name>: Get Your Torrent Link From Various Resource.
<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    COVID_TXT = """<b><u>𝖢𝗈𝗏𝗂𝖽 19 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇</u><b/>

- It is Used to Find 𝖢𝗈𝗋𝗈𝗇𝖺 I𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝗈𝖿 Y𝗈𝗎𝗋 C𝗈𝗎𝗇𝗍𝗋𝗒 / 𝖳𝗈 𝗄𝗇𝗈𝗐 𝗍𝗁𝖾 𝖼𝗈𝗏𝗂𝖽 𝗂𝗇𝖿𝗈 𝗈𝖿 𝖺𝗇𝗒 𝖼𝗈𝗎𝗇𝗍𝗋𝗒            
- 𝖢𝗈𝗎𝗅𝖽 get True and current details and cases
     
<b>NOTE:</b>

1. Users Can Use this to know the Current COVID Info
2. All Users of Dhanush can access this Feature

<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽 and Usage</b>
• /covid (country Name) - 𝖦𝖾𝗍 𝗂𝗇𝖿𝗈 𝖺𝖻𝗈𝗎𝗍 𝖼𝗈𝗏𝗂𝖽 𝖼𝖺𝗌𝖾𝗌 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒

<b>𝖴𝗌𝖺𝗀𝖾</b>
- 𝖢𝗈𝗎𝗅𝖽 𝖻𝖾 𝗎𝗌𝖾𝖽 𝗂𝗇 𝗉𝗆 𝖺𝗇𝖽 𝗀𝗋𝗈𝗎𝗉𝗌."""

    STICKER_TXT ="""Help: <b>StickerID</b>

- It is Used to get the id of the stickers
- Can get instant and unexpirable ids

<b>Commands and Usages</b>
• /stickerid - Reply to a Sticker to get the ids 

<b>Usages</b>
𝖨𝖿 𝖸𝗈𝗎 𝖭𝖾𝖾𝖽 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖲𝗍𝗂𝖼𝗄𝖾𝗋 𝖨𝖽 Use Commands 𝖳𝗈 𝖦𝖾𝗍 𝖲𝗍𝗂𝖼𝗄𝖾𝗋 𝖨𝖽 (𝖱𝖾𝗉𝗅𝗒 𝖶𝗂𝗍𝗁 𝖲𝗍𝗂𝖼𝗄𝖾𝗋)</b>"""
     
    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
• /paste [text] - paste the given text on Pasty
• /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
• Dhanush should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
• /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
• Dhansuh should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

   LOCK_TXT = """Here is the help for the <b>Locks</b> module:
<b>Admin only</b>:
× /lock <permission>: Lock Chat permission..
× /unlock <permission>: Unlock Chat permission.
× /locks: View Chat permission.
× /locktypes: Check available lock types!
Locks can be used to restrict a group's users.
Locking urls will auto-delete all messages with urls, locking stickers will delete all stickers, etc.
Locking bots will stop non-admins from adding bots to the chat.
Example:
/lock media: this locks all the media messages in the chat."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
• /id - get id of a specified user.
• /info  - get information about a user.
• /json - get the json details of a message.

<b>NOTE:</b>
• Dhanush should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
• /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
• Dhanush should have admin privillage.
• These commands works on both pm and group.
• Dhanush can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
• /imdb  - get the film information from IMDb source.
• /search  - get the film information from various sources.

<b>NOTE:</b>
• Dhanush should have admin privillage.
• More search tools can be found on inline.
• Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
• /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
• Dhanush should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
• /ban - ban a user.
• /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /mute - mute a user.
• /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
• Dhanush should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""

    PIN_MESSAGE_TXT = """Help: <b>Pin Message</b>

All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

<b>Commands and Usage:</b>
• /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
• /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.

<b>NOTE:</b>
• Dhanush should have admin privillage.
• These commands works only group.
• These commands can be used by Only admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - to get the rescent errors.
• /stats - to get status of files in db.
• /delete - to delete a specific file from db.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids.
• /leave - to leave from a chat.
• /disable - do disable a chat.
• /ban_users - to ban a user.
• /unban_users - to unban a user.
• /channel - to get list of total connected channels.
• /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>📁 𝙏𝙤𝙩𝙖𝙡 𝙁𝙞𝙡𝙚𝙨 : </b> <code>{}</code>

<b>👤 𝙏𝙤𝙩𝙖𝙡 𝙐𝙨𝙚𝙧𝙨 : </b> <code>{}</code>

<b>👥 𝙏𝙤𝙩𝙖𝙡 𝘾𝙝𝙖𝙩𝙨 : </b> <code>{}</code>

<b>⚙️ 𝙐𝙨𝙚𝙙 𝙎𝙩𝙤𝙧𝙖𝙜𝙚 : </b> <code>{}</code> MiB

<b>🆓 𝙏𝙤𝙩𝙖𝙡 𝙎𝙩𝙤𝙖𝙜𝙚 : </b> <code>{}</code> MiB


𝙈𝙮 𝙎𝙚𝙧𝙫𝙚𝙧 𝙎𝙩𝙖𝙩𝙪𝙨 🍀

💻 𝘾𝙋𝙐 𝙐𝙨𝙖𝙜𝙚 :</b> {}%
☄️ 𝙍𝘼𝙈 𝙐𝙨𝙖𝙜𝙚 :</b> {}%"""

    FORCESUB_TXT = """**♦️ READ THIS INSTRUCTION ♦️**

__🗣 In Order To Get The Movie Requested By You in Our Groups, You Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately 🙈__

**👇 JOIN THIS CHANNEL & TRY AGAIN 👇**"""

    MEMES_TXT = """Help: <b>Memes</b>

Some dank memes for fun or whatever!

<b>Commands and Usage:</b>
• /throw or /dart - t𝗈 m𝖺𝗄𝖾 drat 
• /roll or /dice - roll the dice 
• /goal or /shoot - to make a goal or shoot
• /luck or /cownd - Spin the Lucky
• /runs strings

<b>NOTE:</b>
• Dhanush should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    WELCOME_TXT ="""Here is the help for the <b>Greetings</b> module:

Welcome new members to your groups or say Goodbye after they leave!

<b>Admin Commands</b>:

× /setwelcome <reply/text>: Sets welcome text for group.
× /welcome <yes/no/on/off>: Enables or Disables welcome setting for group.
× /resetwelcome: Resets the welcome message to default.
× /setgoodbye <reply/text>: Sets goodbye text for group.
× /goodbye <yes/no/on/off>: Enables or Disables goodbye setting for group.
× /resetgoodbye: Resets the goodbye message to default.
× /cleanservice <yes/no/on/off>: Delete all service messages such as 'x joined the group' notification.
× /cleanwelcome <yes/no/on/off>: Delete the old welcome message, whenever a new member joins."""
     
    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b>🎲 NOTHING MUCH JUST SOME FUN THINGS</b>
t𝗋𝗒 𝗍𝗁𝗂𝗌 𝖮𝗎𝗍: 
𝟣. /dice - Roll The Dice 
𝟤. /Throw 𝗈𝗋 /Dart - 𝖳𝗈 𝖬𝖺𝗄𝖾 Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""

    URL_SHORTNER_TXT = """Help: <b>URL Shortner</b>

Some URLs is Shortner

<b>Commands and Usage:</b>
• /short <code>(link)</code> - I will send the shorted links.

<b>Example:</b>
<code>/short https://t.me/josprojects</code>

<b>NOTE:</b>
• Dhamush should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    TTS_TXT = """Help: <b>Text to Speech</b>

A module to convert text to voice with language support.

<b>Commands and Usage:</b>
• /tts - Reply to any text message with language code to convert as audio.

<b>NOTE:</b>
• Dhanush should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    MUSIC_TXT = """Help: <b>Music</b>

Music download modules, for those who love music.

<b>Commands and Usage:</b>
• /song or /mp3 (songname) - download song from yt servers.
• /video or /mp4 (songname) - download video from yt servers.

<b>YouTube Thumbnail Download</b>
• /ytthumb (youtube link)
<b>Example:</b> <code>/ytthumb https://youtu.be/h6PtzFYaMxQ</code>

<b>NOTE:</b>
• Dhanush should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>

There Is Nothing To Know More. Send Me The Limit Of Your Password.
- I Will Give The Password Of That Limit.

<b>Commands and Usage:</b>
• /genpassword or /genpw <code>20</code>

<b>NOTE:</b>
• Only Digits Are Allowed
• Maximum Allowed Digits Till 84 
(I Can't Generate Passwords Above The Length 84)
• Dhanush should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    DISABLE_TXT = """Here is the help for the <b>Disabling</b> module:

This allows you to disable some commonly used commands, so noone can use them. It'll also allow you to autodelete them, stopping people from bluetexting.

<b>Admin commands</b>:

× /disable <commandname>: Stop users from using commandname in this group.
× /enable <item name>: Allow users from using commandname in this group.
× /disableable: List all disableable commands.
× /disabledel <yes/no/on/off>: Delete disabled commands when used by non-admins.
× /disabled: List the disabled commands in this chat.

<b>Note</b>:
When disabling a command, the command only gets disabled for non-admins. All admins can still use those commands.
Disabled commands are still accessible through the /connect feature. If you would be interested to see this disabled too, let me know in the support chat."""
    
    RULES_TXT = """Here is the help for the <b>Rules</b> module:

Every chat works with different rules; this module will help make those rules clearer!

<b>User commands</b>:

× /rules: Check the current chat rules.

<b>Admin commands</b>:

× /setrules <text>: Set the rules for this chat.
× /privaterules <yes/no/on/off>: Enable/disable whether the rules should be sent in private.
× /resetrules: Reset the chat rules to default
× /rulesbtn <custom text>: Sets the text of rules button.
× /resetrulesbutton: Reset the text of rules button to default.
× /resetrulesbtn: Same as above."""

    NOTE_TXT = """Here is the help for the <b>Notes</b> module:

Save data for future users with notes!
Notes are great to save random tidbits of information; a phone number, a nice gif, a funny picture - anything!
User commands:
- /get <notename>: Get a note.
- #notename: Same as /get.

<b>Admin commands</b>:
- /save <notename> <note text>: Save a new note called "word". Replying to a message will save that message. Even works on media!
- /clear <notename>: Delete the associated note.
- /notes: List all notes in the current chat.
- /saved: Same as /notes.
- /clearall: Delete ALL notes in a chat. This cannot be undone.
- /privatenotes: Whether or not to send notes in PM. Will send a message with a button which users can click to get the note in PM."""
    
    SHARE_TXT = """Help: <b>Sharing Text Maker</b>

A bot to create a link to share text in the telegram.

<b>Commands and Usage:</b>
• /share (text or reply to message)

<b>NOTE:</b>
• Dhansuh should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    APPROVE_TXT = """Here is the help for the <b>Approvals</b> module:

Sometimes, you might trust a user not to send unwanted content.
Maybe not enough to make them admin, but you might be ok with locks, blacklists, and antiflood not applying to them.
That's what approvals are for - approve of trustworthy users to allow them to send

<b>User commands</b>:
× /approval: Check a user's approval status in this chat.

<b>Admin Commands</b>:

× /approve: Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.
× /unapprove: Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.
× /approved: List all approved users.

<b>Group Owner Commands</b>:
× /unapproveall: Unapprove ALL users in a chat. This cannot be undone."""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """❗You have to be the group creator to do that."""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """🚮 Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """❗I am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
