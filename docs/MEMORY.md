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
- `helpers.py` - `typewrite()`, `clear_screen()`, `pause()`, `display_inventory()` — no game state; `rich` (Table, Console) imported here
- `docs/notes.txt` - deferred ideas (always check this)
- `docs/project.txt` - original design brief
- `docs/story_notes.txt` - narrative/story draft
- `docs/session_summary.txt` - progress log
- GitHub: https://github.com/s-dodge/hcc_game.git | Branch: master

## Next Priorities (in order)
1. Finish room sanity-tiered descriptions (atrium has placeholders; need real content + other rooms)
2. Zalgo/unicode text corruption in typewrite() at low sanity
3. sanity_cost on examine: items that should drain sanity when examined
4. Badge/keycard unlock mechanic (use badge on door to unlock exits)
5. USB drive persistent state redesign (see notes.txt)
6. Write USB drive file content (placeholder in handle_use)
7. Room descriptions: parking_lot, south_stairwell, campus_exit, library, kepler_theatre
8. Plan Library and Theatre buildings
9. MIDI soundtrack (pygame.mixer, Satie Gnossienne No. 1)
10. Multiple endings

## Current Architecture
- `Item`: name, description, aliases, takeable, untakeable_reason, usable, read_text, state, sanity_descriptions, sanity_read_texts, sanity_name (parked)
- `Room`: name, description, exits, items (list of Items), visited (bool), sanity_descriptions
- `Player`: inventory (list), sanity (int 0-100), location (Room)
- `Game`: rooms dict, player, locked_exits set, game loop, parse(), exit_labels(), display_room(), handle_*()
- `rooms` dict keys: lowercase strings with spaces ("help desk office", "IT department")
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
- badge: TBD

## Story
- Player: generic IT staff
- Opening: rainy gray morning, player in help desk office, ServiceDesk ticket appears (urgent, passive-aggressive)
- Steps out to find building empty — flickering lights, cryptic notes
- Finds badge (missing intern's) + broken workstation = inciting clue
- USB drive in storage room: disturbing file contents (TBD)
- IT building is tutorial. Library (LRC) and Theatre are main game.

## Sanity System (partially implemented)
- Three tiers: normal (>70), unsettled (≤70), broken (≤40). No visible meter — player feels effects.
- `whoami` (debug): prints current sanity. `setsanity [n]` (debug): sets sanity for testing. Both undocumented.
- `get_description(sanity)` and `get_read_text(sanity)` on Item; `get_description(sanity)` on Room — all working.
- `handle_read` updated to call `get_read_text(self.player.sanity)`.
- Items with sanity tiers so far: bin_of_mice (descriptions), book (read_texts), sticky_note (read_texts).
- Atrium room has placeholder sanity_descriptions for testing. Other rooms TBD.
- Room visited reset on tier crossing: deferred (see notes.txt).
- Still to implement: sanity_cost on examine, Zalgo text corruption in typewrite(), badge unlock mechanic.
- See docs/notes.txt for full details and deferred ideas.

## User Preferences
- Learning project: explain and guide, only make direct edits when explicitly asked
- Keep notes.txt updated with deferred ideas
- Commit regularly when asked
- No over-engineering — scope is a 30-min easter egg game
