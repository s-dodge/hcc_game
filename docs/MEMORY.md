# HCC Game - Project Memory

## What This Is
Text-based horror adventure game (Python, CLI) embedded as an easter egg in a personal IT helpdesk CLI tool. Set at Hagerstown Community College. Tone: Control/Night Vale — genuinely eerie but darkly humorous. Target length: <30 minutes.

## CRITICAL: Session Behavior
**This is a learning project.** Do NOT write or edit code directly unless explicitly asked.
- Explain concepts, offer pseudocode, describe approaches
- Snippets are fine for illustration; full implementations are not

## Project Structure
- `main.py` - entry point; instantiates Player, loads rooms, starts Game
- `game.py` - Game class: game loop, parse(), command dispatch, all handle_* methods
- `items.py` - Item class + all item instances + `all_items` dict
- `rooms.py` - Room class + all room instances + `all_rooms` dict + `locked_exits` set
- `helpers.py` - `typewrite()`, `clear_screen()`, `pause()` — no game state
- `docs/notes.txt` - deferred ideas (always check this)
- `docs/project.txt` - original design brief
- `docs/story_notes.txt` - narrative/story draft
- `docs/session_summary.txt` - progress log
- GitHub: https://github.com/s-dodge/hcc_game.git | Branch: master

## Next Priorities (in order)
1. Write USB drive reveal content (placeholder in game.py handle_use)
2. Write cinematic intro block content (placeholders in game.py run())
3. Room descriptions for: parking_lot, south_stairwell, campus_exit, library, kepler_theatre
4. Sanity system implementation
5. Plan Library and Theatre buildings
6. Zalgo/unicode text corruption at low sanity
7. MIDI soundtrack (pygame.mixer, Satie Gnossienne No. 1)
8. Multiple endings

## Current Architecture
- `Item`: name, description, aliases, takeable, untakeable_reason, usable, read_text, state, sanity_descriptions
- `Room`: name, description, exits, items (list of Items), visited (bool), sanity_descriptions
- `Player`: inventory (list), sanity (int 0-100), location (Room)
- `Game`: rooms dict, player, locked_exits set, game loop, parse(), exit_labels(), display_room(), handle_*()
- `rooms` dict keys: lowercase strings with spaces ("help desk office", "it department")
- `locked_exits`: set of `(room.name, direction)` tuples — room.name must use spaces not underscores
- `from items import *` in rooms.py — pragmatic for small game, avoids updating imports when adding items
- `Item.aliases`: list; resolved in `room.get_item()` and `player.has_item()`
- `Item.state`: arbitrary string for stateful items (None by default)
- `parse()`: strips leading article from noun, lowercases, returns `(verb, noun)`
- `handle_use()`: splits noun on `" on "`, strips article from target_name after split
- `exit_labels()`: shows "north (storage room)" for visited rooms, plain "north" for unvisited
- Multi-word verb normalization before parse(): `"pick up"→"take"`, `"look at"→"examine"`
- Verb synonyms: n/s/e/w, x=examine, l=look, get=take, i=inventory, h=help, walk=go, leave
- `display_room(force_full=True)` suppresses "You have entered" header, shows full description
- Cinematic intro block in `run()`: sets `visited=True` manually, shows items/exits directly
- All narrative output uses `typewrite()`
- `pause()` in helpers.py: waits for Enter, erases blank line with ANSI — available but not currently used

## use Mechanic (implemented)
- `power cable on workstation` → workstation.state="powered", description updates, cable consumed
- `usb drive on powered workstation` → placeholder content shown, sanity -20, drive.state="used"
- keycard: TBD

## Story
- Player: generic IT staff
- Opening: rainy gray morning, player in help desk office, ServiceDesk ticket appears (urgent, passive-aggressive)
- Steps out to find building empty — flickering lights, cryptic notes
- Finds keycard (missing intern's) + broken workstation = inciting clue
- USB drive in storage room: disturbing file contents (TBD)
- IT building is tutorial. Library (LRC) and Theatre are main game.

## Sanity System (planned)
- Drains as player examines things. No visible meter — player feels effects.
- Threshold dict pattern already on Item and Room: `{75: "unsettling", 50: "wrong", 25: "incomprehensible"}`
- Room descriptions change (moss growth motif)
- Item descriptions change per threshold (e.g. "bin of mice" → real mice at low sanity)
- Inventory corruption: items rename at low sanity ("keycard"→"a tooth", "ddr5"→"a finger bone")
- Zalgo/unicode fragmentation before descriptions go full eldritch
- Sanity-gated workstation exit
- See docs/notes.txt for full details

## User Preferences
- Learning project: explain and guide, only make direct edits when explicitly asked
- Keep notes.txt updated with deferred ideas
- Commit regularly when asked
- No over-engineering — scope is a 30-min easter egg game
