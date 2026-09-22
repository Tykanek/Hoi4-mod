# Hoi4-mod agent guidance

## Project shape

- This is a Hearts of Iron IV data mod centered on Prague and Benesov. See [README.md](README.md) for the project goals and planned content.
- Country tags are uppercase three-letter IDs. Current tags include `PRA` and `BEN`.
- Country tags are registered in `common/country_tags/`; country history and colors are in `common/countries/`; characters are in `common/characters/`.
- Event scripts are in `events/`, interface definitions are in `interface/`, flags are in `gfx/flags/`, and English localization is in `localisation/english/`.
- Important existing examples are [events/prague_event.txt](events/prague_event.txt), [common/countries/prague.txt](common/countries/prague.txt), and [localisation/english/events_prague_l_english.yml](localisation/english/events_prague_l_english.yml).

## File conventions

- Use the `paradox` language mode for HoI4 `.txt` and `.mod` files. Keep localization `.yml` files in YAML mode; the workspace mappings are in [.vscode/settings.json](.vscode/settings.json).
- Follow the existing HoI4 key/value block syntax and local indentation style. Do not reformat unrelated content.
- Declare an event namespace before its `country_event` definitions. Keep event IDs, option names, and localization keys consistent.
- Localization files must start with `l_english:`. Add entries for every referenced event title, description, option, country, character name, and character description.
- Preserve the intended behavior of existing scripts. Treat CWTools diagnostics as potentially schema/version-related until confirmed against HoI4 syntax and in-game behavior.

## Validation

- There is no build system, package manifest, CI workflow, or automated test suite in this repository.
- Before editing, read the target file and nearby references. After editing, use the narrowest available check: VS Code/CWTools diagnostics, localization/key inspection, then launch HoI4 with the mod enabled and inspect the game `error.log`.
- When diagnosing a reported error, first confirm the exact file, diagnostic, and active language mode. For localization errors, check the filename, `l_english:` header, key spelling, and event ID before changing script logic.

## Windows and WSL

- The Windows project path is `C:\Users\lukas\Documents\Paradox Interactive\Hearts of Iron IV\mod\Hoi4-mod`.
- The equivalent WSL path is `/mnt/c/Users/lukas/Documents/Paradox Interactive/Hearts of Iron IV/mod/Hoi4-mod`.
- Run Linux commands such as `pwd`, `cat`, and `git` in WSL from the mod root. Run Windows commands such as `wsl --list --verbose` in PowerShell, not in WSL.

## Git safety

- Inspect state before making assumptions: `git status --short --branch`, `git remote -v`, and `git log --oneline --decorate -5`.
- Before committing, review both `git diff` and `git diff --cached`; stage all changes with `git add -A` and use a descriptive commit message.
- To update and publish `main`, use `git pull --rebase origin main` followed by `git push origin main`. Never force-push or discard local work with `git reset --hard` or `git clean -fd` unless explicitly requested.
- Do not put passwords, tokens, or private keys in chat, project files, or remote URLs. For HTTPS authentication, use `gh auth login` and `gh auth status`.
- Keep changes minimal, do not overwrite unrelated user work, and report which files changed and whether changes are committed.