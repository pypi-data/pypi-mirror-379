# skyter

skyter is a Bluesky client for the terminal built using [atproto](https://github.com/MarshalX/atproto) and [textual](https://github.com/Textualize/textual). Pronounce it however you prefer.

Features:

- View likes of other users
- Optionally hide post and user metrics
- Option for feeds to automatically update with new posts
- Pause/resume notifications
- Run multiple instances of skyter in terminal multiplexer for tweetdeck-like set-up

Not yet supported:

- DMs
- Bookmarks
- Thread composing
- Saving post drafts
- List / starter pack management
- Post interaction settings
- Bluesky settings (other than saved feeds)


## Requirements

- Python 3.8+
- xclip (if on Linux)

### Optional dependencies

- [python-dotenv](https://github.com/theskumar/python-dotenv): run `pip install python-dotenv` if you want to use an `.env` file for credentials
- textual's prepackaged tree-sitter binaries for json syntax highlighting: run `pip install "textual[syntax]"`
- terminal media viewers such as [feh](https://feh.finalrewind.org/) or [mpv](https://mpv.io/) are recommended for opening post media

## Install

`pip install skyter`

## Set-up

- Optional but strongly recommended: create an [app password](https://bsky.app/settings/app-passwords) in the web client or app. You do not need to allow access to direct messages, as DMs are not yet supported. Password login is not supported for 2FA-enabled accounts
- Optionally set `BSKY_LOGIN` and `BSKY_APP_PASSWORD` (and `BSKY_PDS`, if using an alternate PDS) environment variables to be logged in when the app is initialized and skip the login screen.
- Check your default settings by opening the command palette and going to settings: `ctrl+p` -> `Settings`, or configure the `settings.json` file manually. The file will be created automatically at `data/settings.json` in the installed location the first time the app is opened. See <project:settings.md> for more details.
