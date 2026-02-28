# HCC Game — Project Memory

## CRITICAL: Session Behavior
**This is a learning project.** Do NOT write or edit code directly unless the user explicitly asks.
- Explain concepts, offer pseudocode, describe approaches
- Snippets are fine for illustration; full implementations are not
- This is documented in docs/project.txt (line 41-42) as a standing instruction

## Project Overview
Text-based adventure game (Python, CLI). Eldritch horror / dark academia set at Hagerstown Community College. Tone: tongue-in-cheek (Control / Night Vale vibes). Single file: `main.py`.

## Current State (as of 2026-02-28)
Working prototype with: room navigation, item examine/take/drop/read, inventory, parser (verb/noun), locked exits, visited room tracking, item aliases. Helpers module in place with `typewrite()` and `clear_screen()`. All narrative output uses `typewrite()`.

**Next priorities:**
1. **Class refactor (Room, Player, Item, Game)** — do this BEFORE adding new mechanics
2. Room descriptions/atmosphere for remaining IT building rooms (atrium, parking lot, stairwell, campus exterior are empty)
3. Help desk office — planned player start room (stub already in main.py, commented out)
4. `use` verb mechanic — item-use state (e.g. workstation powered/unpowered) belongs on Item objects, not parallel dicts
5. Plan Library and Theatre buildings
6. Sanity system + zalgo text corruption
7. MIDI soundtrack (pygame.mixer, Satie Gnossienne No. 1)
8. Multiple endings

**Class refactor design (agreed upon):**
- `Item`: name, description, aliases, takeable, usable, readable, read_text, state, sanity-tiered descriptions
- `Room`: name, description, exits, items (list of Items), visited (bool), sanity-tiered descriptions
- `Player`: inventory, sanity, location (Room) — location moves here from local var in main()
- `Game`: owns game loop, rooms dict, player, parse(), command dispatch
- `use` items identified so far: power cable (repairs workstation), USB drive (use on powered workstation), key/keycard TBD (not the intern's — that's just a clue item)

## Key Architecture
- `rooms` dict: keys are lowercase strings
- `locked_exits`: set of `(room_name, direction)` tuples — unlock with `.discard()`
- `item_descriptions`: flat dict, keys match room items list exactly (lowercase)
- `item_aliases`: maps short names → canonical item keys
- `readable_items`: separate dict for `read` verb
- `player` dict: `inventory` (list), `sanity` (int, 0-100), `visited_rooms` (set)
- `location`: local variable in `main()`, NOT stored in player dict
- `parse()` returns `(verb, noun)` — strips articles, lowercases
- `helpers.py`: `typewrite(text, char_delay=0.03, line_delay=0.4)`, `clear_screen()` — utility functions, no game state
- `colorama` imported but commented out — reserved for sanity/zalgo effects later
- `parse()` still in main.py — deferred to class refactor before moving

## Story
- Player: generic IT staff
- Opening: rainy gray morning, player in help desk office, ServiceDesk ticket appears on screen (urgent, passive-aggressive tone)
- Steps out to find building empty — flickering lights, cryptic note(s) planned
- Finds keycard (belongs to missing intern) + broken workstation = inciting clue
- IT building is tutorial. Library (LRC) and Theatre are main game.
- Draft in docs/story_notes.txt

## Map (IT Building Tutorial)
See docs/session_summary.txt for full map. Player starts in help desk office (west of IT dept).

## Deferred Ideas
See docs/notes.txt for full list. Key ones:
- Oxford comma item list formatting — deferred until after class refactor
- Sanity-gated room/item description tiers (threshold dict pattern)
- Item aliases pipeline: input → aliases → canonical key → display_names → output
- Pronoun reference ("take it") via `last_item` variable
- Inventory corruption at low sanity (items rename themselves)
- Zalgo/unicode corruption for sanity effects (`rich` library recommended)
- Exit mechanic ideas (workstation, phone, parking lot)
- Ambient interrupt mechanic: after random 5–10 min of play, print a creepy message. Check timer after each command resolves (can't interrupt `input()`). Use `time.time()` + `random.uniform(300, 600)`. Can recur by resetting trigger after firing.
- Splash screen / terminal image display options:
  - Option 1 (preferred): Pre-convert to ASCII art offline, hardcode as multiline string — zero deps, fits aesthetic
  - Option 2: Half-block Unicode (`▀`) + ANSI truecolor — much better quality, needs Pillow + colorama (already imported)
  - Option 3: `rich` library Image renderable — consolidates deps if rich is added for zalgo
  - Option 4: Kitty/Sixel protocols — skip, too terminal-specific

## GitHub
https://github.com/s-dodge/hcc_game.git | Branch: master
