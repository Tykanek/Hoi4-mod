[1mdiff --git a/AGENTS.md b/AGENTS.md[m
[1mnew file mode 100644[m
[1mindex 0000000..f9c1bf0[m
[1m--- /dev/null[m
[1m+++ b/AGENTS.md[m
[36m@@ -0,0 +1,37 @@[m
[32m+[m[32m# Hoi4-mod agent guidance[m[41m[m
[32m+[m[41m[m
[32m+[m[32m## Project shape[m[41m[m
[32m+[m[41m[m
[32m+[m[32m- This is a Hearts of Iron IV data mod centered on Prague and Benesov. See [README.md](README.md) for the project goals and planned content.[m[41m[m
[32m+[m[32m- Country tags are uppercase three-letter IDs. Current tags include `PRA` and `BEN`.[m[41m[m
[32m+[m[32m- Country tags are registered in `common/country_tags/`; country history and colors are in `common/countries/`; characters are in `common/characters/`.[m[41m[m
[32m+[m[32m- Event scripts are in `events/`, interface definitions are in `interface/`, flags are in `gfx/flags/`, and English localization is in `localisation/english/`.[m[41m[m
[32m+[m[32m- Important existing examples are [events/prague_event.txt](events/prague_event.txt), [common/countries/prague.txt](common/countries/prague.txt), and [localisation/english/events_prague_l_english.yml](localisation/english/events_prague_l_english.yml).[m[41m[m
[32m+[m[41m[m
[32m+[m[32m## File conventions[m[41m[m
[32m+[m[41m[m
[32m+[m[32m- Use the `paradox` language mode for HoI4 `.txt` and `.mod` files. Keep localization `.yml` files in YAML mode; the workspace mappings are in [.vscode/settings.json](.vscode/settings.json).[m[41m[m
[32m+[m[32m- Follow the existing HoI4 key/value block syntax and local indentation style. Do not reformat unrelated content.[m[41m[m
[32m+[m[32m- Declare an event namespace before its `country_event` definitions. Keep event IDs, option names, and localization keys consistent.[m[41m[m
[32m+[m[32m- Localization files must start with `l_english:`. Add entries for every referenced event title, description, option, country, character name, and character description.[m[41m[m
[32m+[m[32m- Preserve the intended behavior of existing scripts. Treat CWTools diagnostics as potentially schema/version-related until confirmed against HoI4 syntax and in-game behavior.[m[41m[m
[32m+[m[41m[m
[32m+[m[32m## Validation[m[41m[m
[32m+[m[41m[m
[32m+[m[32m- There is no build system, package manifest, CI workflow, or automated test suite in this repository.[m[41m[m
[32m+[m[32m- Before editing, read the target file and nearby references. After editing, use the narrowest available check: VS Code/CWTools diagnostics, localization/key inspection, then launch HoI4 with the mod enabled and inspect the game `error.log`.[m[41m[m
[32m+[m[32m- When diagnosing a reported error, first confirm the exact file, diagnostic, and active language mode. For localization errors, check the filename, `l_english:` header, key spelling, and event ID before changing script logic.[m[41m[m
[32m+[m[41m[m
[32m+[m[32m## Windows and WSL[m[41m[m
[32m+[m[41m[m
[32m+[m[32m- The Windows project path is `C:\Users\lukas\Documents\Paradox Interactive\Hearts of Iron IV\mod\Hoi4-mod`.[m[41m[m
[32m+[m[32m- The equivalent WSL path is `/mnt/c/Users/lukas/Documents/Paradox Interactive/Hearts of Iron IV/mod/Hoi4-mod`.[m[41m[m
[32m+[m[32m- Run Linux commands such as `pwd`, `cat`, and `git` in WSL from the mod root. Run Windows commands such as `wsl --list --verbose` in PowerShell, not in WSL.[m[41m[m
[32m+[m[41m[m
[32m+[m[32m## Git safety[m[41m[m
[32m+[m[41m[m
[32m+[m[32m- Inspect state before making assumptions: `git status --short --branch`, `git remote -v`, and `git log --oneline --decorate -5`.[m[41m[m
[32m+[m[32m- Before committing, review both `git diff` and `git diff --cached`; stage all changes with `git add -A` and use a descriptive commit message.[m[41m[m
[32m+[m[32m- To update and publish `main`, use `git pull --rebase origin main` followed by `git push origin main`. Never force-push or discard local work with `git reset --hard` or `git clean -fd` unless explicitly requested.[m[41m[m
[32m+[m[32m- Do not put passwords, tokens, or private keys in chat, project files, or remote URLs. For HTTPS authentication, use `gh auth login` and `gh auth status`.[m[41m[m
[32m+[m[32m- Keep changes minimal, do not overwrite unrelated user work, and report which files changed and whether changes are committed.[m
\ No newline at end of file[m
[1mdiff --git a/common/characters/PRA.txt b/common/characters/PRA.txt[m
[1mindex df366ef..38e0d41 100644[m
[1m--- a/common/characters/PRA.txt[m
[1m+++ b/common/characters/PRA.txt[m
[36m@@ -8,5 +8,15 @@[m [mcharacters = {[m
                 large = gfx/leaders/PRA/PRA_great_leader.dds #add later[m
             }[m
         }[m
[32m+[m[41m[m
[32m+[m[32m        country_leader = {[m[41m[m
[32m+[m[32m            ideology = democratic[m[41m[m
[32m+[m[32m            personality = neutral[m[41m[m
[32m+[m[32m            traits = {[m[41m[m
[32m+[m[32m                trait_ideological_communist[m[41m[m
[32m+[m[32m                trait_charismatic[m[41m[m
[32m+[m[32m                trait_industrious[m[41m[m
[32m+[m[32m            }[m[41m[m
[32m+[m[32m        }[m[41m[m
     }[m
 }[m
\ No newline at end of file[m
[1mdiff --git a/history/countries/PRA - start.txt b/history/countries/PRA - start.txt[m
[1mnew file mode 100644[m
[1mindex 0000000..ede83d8[m
[1m--- /dev/null[m
[1m+++ b/history/countries/PRA - start.txt[m	
[36m@@ -0,0 +1,82 @@[m
[32m+[m[32m﻿capital = 908[m
[32m+[m
[32m+[m[32mOOB = "AFA_1936"[m
[32m+[m[32m# Starting tech[m
[32m+[m[32mset_technology = {[m
[32m+[m	[32minfantry_weapons = 1[m
[32m+[m	[32mcamelry = 1[m
[32m+[m[32m}[m
[32m+[m
[32m+[m[32madd_manpower = 15000[m
[32m+[m
[32m+[m[32madd_ideas = {[m
[32m+[m	[32mbba_AFA_skilled_desert_warriors[m
[32m+[m[32m}[m
[32m+[m
[32m+[m[32mITA = {[m
[32m+[m	[32mgive_guarantee = AFA[m
[32m+[m[32m}[m
[32m+[m
[32m+[m[32mset_convoys = 10[m
[32m+[m
[32m+[m[32m1939.1.1 = {[m
[32m+[m
[32m+[m	[32m#generic focuses[m
[32m+[m	[32mcomplete_national_focus = army_effort[m
[32m+[m	[32mcomplete_national_focus = equipment_effort[m
[32m+[m	[32mcomplete_national_focus = motorization_effort[m
[32m+[m	[32mcomplete_national_focus = aviation_effort[m
[32m+[m	[32mcomplete_national_focus = naval_effort[m
[32m+[m	[32mcomplete_national_focus = large_navy[m
[32m+[m	[32mcomplete_national_focus = industrial_effort[m
[32m+[m	[32mcomplete_national_focus = construction_effort[m
[32m+[m	[32mcomplete_national_focus = production_effort[m
[32m+[m
[32m+[m	[32mset_technology = {[m
[32m+[m		[32mtech_support = 1[m
[32m+[m		[32mtech_recon = 1[m
[32m+[m		[32msupport_weapons = 1[m
[32m+[m		[32mgw_artillery = 1[m
[32m+[m
[32m+[m		[32m#doctrines[m
[32m+[m		[32m#air_superiority = 1[m
[32m+[m
[32m+[m		[32m#electronics[m
[32m+[m		[32melectronic_mechanical_engineering = 1[m
[32m+[m		[32mradio = 1[m
[32m+[m		[32mmechanical_computing = 1[m
[32m+[m		[32mcomputing_machine = 1[m
[32m+[m
[32m+[m		[32m#industry[m
[32m+[m		[32mbasic_machine_tools = 1[m
[32m+[m		[32mimproved_machine_tools = 1[m
[32m+[m		[32madvanced_machine_tools = 1[m
[32m+[m		[32mfuel_silos = 1[m
[32m+[m		[32mconstruction1 = 1[m
[32m+[m		[32mconstruction2 = 1[m
[32m+[m		[32mdispersed_industry = 1[m
[32m+[m		[32mdispersed_industry2 = 1[m
[32m+[m	[32m}[m
[32m+[m
[32m+[m[32mset_grand_doctrine = grand_battleplan[m
[32m+[m[32mset_grand_doctrine = new_strategic_destruction[m
[32m+[m
[32m+[m	[32mcomplete_special_project = {[m
[32m+[m		[32mproject = sp:sp_air_radar[m
[32m+[m	[32m}[m
[32m+[m[32m}[m
[32m+[m
[32m+[m[32mrecruit_character = AFA_sultan_mohamed_yayyo_of_aussa[m
[32m+[m
[32m+[m[32mset_politics = {[m
[32m+[m	[32mruling_party = neutrality[m
[32m+[m	[32mlast_election = "1936.1.1"[m
[32m+[m	[32melection_frequency = 48[m
[32m+[m	[32melections_allowed = no[m
[32m+[m[32m}[m
[32m+[m[32mset_popularities = {[m
[32m+[m	[32mdemocratic = 0[m
[32m+[m	[32mfascism = 20[m
[32m+[m	[32mcommunism = 5[m
[32m+[m	[32mneutrality = 75[m
[32m+[m[32m}[m
[1mdiff --git a/history/states/9-Czechoslovakia.txt b/history/states/9-Czechoslovakia.txt[m
[1mnew file mode 100644[m
[1mindex 0000000..e2d4504[m
[1m--- /dev/null[m
[1m+++ b/history/states/9-Czechoslovakia.txt[m
[36m@@ -0,0 +1,47 @@[m
[32m+[m[32mstate={[m
[32m+[m	[32mid=9[m
[32m+[m	[32mname="STATE_9"[m
[32m+[m	[32mmanpower = 4492600[m
[32m+[m	[32mresources={[m
[32m+[m		[32msteel = 5 # was: 8[m
[32m+[m		[32mcoal = 6 # initial distribution / 60 total[m
[32m+[m	[32m}[m
[32m+[m[41m	[m
[32m+[m	[32mstate_category = large_city[m
[32m+[m[41m	[m
[32m+[m	[32mhistory={[m
[32m+[m		[32mowner = CZE[m
[32m+[m		[32mvictory_points = { 11542 30 }[m
[32m+[m		[32mvictory_points = { 6418 5 }[m
[32m+[m		[32mvictory_points = { 9569 5 }[m
[32m+[m		[32m#victory_points = { 9541 3 }[m
[32m+[m		[32mbuildings = {[m
[32m+[m			[32minfrastructure = 4[m
[32m+[m			[32marms_factory = 5[m
[32m+[m			[32mindustrial_complex = 1[m
[32m+[m			[32manti_air_building = 5[m
[32m+[m			[32mair_base = 5[m
[32m+[m			[32m 11542 = {	#marijn211: if too big, move to 6440[m
[32m+[m			[41m [m	[32mlandmark_prague_castle = {[m
[32m+[m			[41m [m		[32mlevel = 1[m
[32m+[m			[41m [m		[32mallowed = {[m
[32m+[m			[41m [m			[32mhas_dlc = "Peace For Our Time"[m
[32m+[m			[41m [m		[32m}[m
[32m+[m			[41m [m	[32m}[m
[32m+[m			[32m }[m
[32m+[m		[32m}[m
[32m+[m		[32madd_core_of = CZE[m
[32m+[m
[32m+[m
[32m+[m		[32m1939.3.14 = {[m
[32m+[m			[32mowner = GER[m
[32m+[m			[32mcontroller = GER[m
[32m+[m		[32m}[m
[32m+[m	[32m}[m
[32m+[m
[32m+[m	[32mprovinces={[m
[32m+[m		[32m445 494 583 3462 6418 6440 6592 9414 9421 9429 9541 9569 11542 11556[m[41m [m
[32m+[m	[32m}[m
[32m+[m
[32m+[m	[32mlocal_supplies=0.0[m[41m [m
[32m+[m[32m}[m
[1mdiff --git a/interface/_Mod_leader_portraits.gfx b/interface/_Mod_leader_portraits.gfx[m
[1mindex 7ce31b8..7c4290a 100644[m
[1m--- a/interface/_Mod_leader_portraits.gfx[m
[1m+++ b/interface/_Mod_leader_portraits.gfx[m
[36m@@ -1,6 +1,6 @@[m
 spritetypes = {[m
 	spriteType = {[m
[31m-		#name = "leader_portraits"[m
[32m+[m		[32mname = "GFX_portraint_PRA"[m[41m[m
 		#texturefile = "gfx/interface/leader_portraits.dds"[m
 	}[m
 }[m
\ No newline at end of file[m
[1mdiff --git a/localisation/english/mod_characters_l_english.yml b/localisation/english/mod_characters_l_english.yml[m
[1mnew file mode 100644[m
[1mindex 0000000..27f0945[m
[1m--- /dev/null[m
[1m+++ b/localisation/english/mod_characters_l_english.yml[m
[36m@@ -0,0 +1,2 @@[m
[32m+[m[32m﻿l_english:[m[41m[m
[32m+[m[32mPRA_great_leader: "Test test 123"[m
\ No newline at end of file[m
[1mdiff --git a/setup-history.txt b/setup-history.txt[m
[1mdeleted file mode 100644[m
[1mindex 8f2b45e..0000000[m
[1m--- a/setup-history.txt[m
[1m+++ /dev/null[m
[36m@@ -1,285 +0,0 @@[m
[31m-VS Code, GitHub, WSL, and Terminal Setup History[m
[31m-===============================================[m
[31m-[m
[31m-This file records the setup steps and commands used during this chat.[m
[31m-Passwords, personal access tokens, and private keys are intentionally not recorded.[m
[31m-Run commands from the repository folder unless stated otherwise:[m
[31m-[m
[31m-C:\Users\lukas\Documents\Paradox Interactive\Hearts of Iron IV\mod\Hoi4-mod[m
[31m-[m
[31m-[m
[31m-1. Repository and Git inspection[m
[31m-================================[m
[31m-[m
[31m-# Show the current branch and working-tree state.[m
[31m-git status --short --branch[m
[31m-[m
[31m-# Show configured GitHub remotes.[m
[31m-git remote -v[m
[31m-[m
[31m-# Show recent commits.[m
[31m-git log --oneline --decorate -8[m
[31m-[m
[31m-# Show all branches and upstream relationships.[m
[31m-git branch -avv[m
[31m-[m
[31m-# Show repository-local Git configuration.[m
[31m-git config --local --list[m
[31m-[m
[31m-# Show recent local branch movements.[m
[31m-git reflog --date=local -10[m
[31m-[m
[31m-# Show the latest commit and changed files.[m
[31m-git show --stat --format=fuller HEAD[m
[31m-[m
[31m-# Show all local references and their commits.[m
[31m-git log --all --oneline --decorate --date=local --pretty='%h %ad %d %s' -10[m
[31m-[m
[31m-# Check global remote and branch settings.[m
[31m-git config --global --get-regexp '^(remote|branch)\.'[m
[31m-[m
[31m-# Check configured credential helpers.[m
[31m-git config --global --get credential.helper[m
[31m-git config --local --get credential.helper[m
[31m-git config --show-origin --get-all credential.helper[m
[31m-[m
[31m-# Show the latest commit only.[m
[31m-git log -1 --oneline[m
[31m-[m
[31m-[m
[31m-2. GitHub remote setup[m
[31m-======================[m
[31m-[m
[31m-# Add the GitHub repository as the origin remote.[m
[31m-# This was configured for this project:[m
[31m-git remote add origin https://github.com/Tykanek/Hoi4-mod.git[m
[31m-[m
[31m-# Verify the remote URL.[m
[31m-git remote -v[m
[31m-[m
[31m-# Download remote history without changing local files.[m
[31m-git fetch origin[m
[31m-[m
[31m-# Display local and remote commit history together.[m
[31m-git log --oneline --graph --decorate --all[m
[31m-[m
[31m-The current remote is:[m
[31m-https://github.com/Tykanek/Hoi4-mod.git[m
[31m-[m
[31m-The main branch is configured to track:[m
[31m-origin/main[m
[31m-[m
[31m-[m
[31m-3. GitHub authentication[m
[31m-========================[m
[31m-[m
[31m-GitHub no longer accepts normal account passwords for Git over HTTPS.[m
[31m-A personal access token was created or used instead of a password.[m
[31m-[m
[31m-# Push using HTTPS.[m
[31m-git push -u origin main[m
[31m-[m
[31m-When prompted:[m
[31m-[m
[31m-Username: Tykanek[m
[31m-Password: paste the GitHub personal access token, not the account password[m
[31m-[m
[31m-The token is hidden while typing. It must never be committed to a file or put[m
[31m-inside the remote URL.[m
[31m-[m
[31m-The GitHub token was configured with repository Contents read/write permission[m
[31m-for the Hoi4-mod repository.[m
[31m-[m
[31m-[m
[31m-4. SSH host verification[m
[31m-========================[m
[31m-[m
[31m-GitHub SSH host verification was encountered in the terminal.[m
[31m-The official GitHub ED25519 fingerprint shown was:[m
[31m-SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU[m
[31m-[m
[31m-The confirmation prompt was:[m
[31m-[m
[31m-Are you sure you want to continue connecting (yes/no/[fingerprint])?[m
[31m-[m
[31m-yes[m
[31m-[m
[31m-Only confirm this after verifying that the fingerprint matches GitHub's official[m
[31m-published fingerprint.[m
[31m-[m
[31m-No private SSH key was recorded in this file.[m
[31m-[m
[31m-[m
[31m-5. Optional GitHub CLI authentication[m
[31m-======================================[m
[31m-[m
[31m-# Install GitHub CLI in Ubuntu/WSL if it is not installed.[m
[31m-sudo apt update[m
[31m-sudo apt install gh[m
[31m-[m
[31m-# Authenticate GitHub CLI through a browser.[m
[31m-gh auth login[m
[31m-[m
[31m-Choose:[m
[31m-1. GitHub.com[m
[31m-2. HTTPS[m
[31m-3. Login with a web browser[m
[31m-[m
[31m-# Verify authentication.[m
[31m-gh auth status[m
[31m-[m
[31m-After authentication, normal commands can use the saved GitHub credentials:[m
[31m-git pull[m
[31m-git push[m
[31m-[m
[31m-[m
[31m-6. Safe daily Git workflow[m
[31m-==========================[m
[31m-[m
[31m-# Inspect current changes.[m
[31m-git status[m
[31m-git diff[m
[31m-[m
[31m-# Stage all changed, deleted, and renamed files.[m
[31m-git add -A[m
[31m-[m
[31m-# Or stage only a chosen file.[m
[31m-git add path/to/file.txt[m
[31m-[m
[31m-# Review what will be committed.[m
[31m-git diff --cached[m
[31m-[m
[31m-# Create a local commit.[m
[31m-git commit -m "Describe the changes"[m
[31m-[m
[31m-# Download and integrate newer GitHub commits without rewriting history.[m
[31m-git pull --rebase origin main[m
[31m-[m
[31m-# Push normally without force-overwriting GitHub.[m
[31m-git push origin main[m
[31m-[m
[31m-After the upstream is configured, these shorter commands work:[m
[31m-git pull[m
[31m-git push[m
[31m-[m
[31m-[m
[31m-7. Safe handling of local deletions[m
[31m-===================================[m
[31m-[m
[31m-If folders or files were deleted locally and those deletions should be sent to[m
[31m-GitHub, stage the deletions explicitly:[m
[31m-[m
[31m-git status[m
[31m-git add -A[m
[31m-git commit -m "Remove obsolete files"[m
[31m-git pull --rebase origin main[m
[31m-git push origin main[m
[31m-[m
[31m-A normal push refuses to overwrite newer remote commits. If GitHub changed after[m
[31m-the local commit, pull with rebase first and then push again.[m
[31m-[m
[31m-Do not use these commands unless intentionally discarding or rewriting data:[m
[31m-[m
[31m-# Discards local tracked changes and makes the branch match GitHub.[m
[31m-# git reset --hard origin/main[m
[31m-[m
[31m-# Permanently removes untracked files and directories.[m
[31m-# git clean -fd[m
[31m-[m
[31m-# Can overwrite remote history.[m
[31m-# git push --force[m
[31m-[m
[31m-[m
[31m-8. Pulling GitHub as the local copy[m
[31m-===================================[m
[31m-[m
[31m-To intentionally make the local branch match GitHub exactly, first create a[m
[31m-backup branch, then reset:[m
[31m-[m
[31m-git branch backup-before-github-reset[m
[31m-git fetch origin[m
[31m-git reset --hard origin/main[m
[31m-[m
[31m-This discards local tracked changes not present on GitHub. Use it only when that[m
[31m-is the desired result.[m
[31m-[m
[31m-[m
[31m-9. Conflict recovery[m
[31m-====================[m
[31m-[m
[31m-# See files involved in a conflict.[m
[31m-git status[m
[31m-[m
[31m-# After resolving a file, stage it.[m
[31m-git add path/to/resolved-file.txt[m
[31m-[m
[31m-# Continue a rebase.[m
[31m-git rebase --continue[m
[31m-[m
[31m-# Cancel a rebase and return to the pre-rebase state.[m
[31m-git rebase --abort[m
[31m-[m
[31m-# Merge unrelated initial histories only when that is genuinely required.[m
[31m-git pull --no-rebase origin main --allow-unrelated-histories[m
[31m-[m
[31m-# After resolving a merge conflict:[m
[31m-git add -A[m
[31m-git commit[m
[31m-git push origin main[m
[31m-[m
[31m-[m
[31m-10. VS Code setup[m
[31m-=================[m
[31m-[m
[31m-The workspace contains:[m
[31m-[m
[31m-.vscode/settings.json[m
[31m-[m
[31m-Its current setting is:[m
[31m-[m
[31m-{[m
[31m-    "files.associations": {[m
[31m-        "**/*.txt": "paradox",[m
[31m-        "**/*.mod": "paradox"[m
[31m-    }[m
[31m-}[m
[31m-[m
[31m-This makes Paradox script files use the Paradox language mode instead of a[m
[31m-HOI4-specific mode. Localization .yml files remain YAML.[m
[31m-[m
[31m-To reload VS Code after changing workspace settings:[m
[31m-[m
[31m-1. Press Ctrl+Shift+P.[m
[31m-2. Run Developer: Reload Window.[m
[31m-3. Reopen the file if its language mode did not update.[m
[31m-[m
[31m-The installed Paradox language extension identified the language mode as:[m
[31m-paradox[m
[31m-[m
[31m-The CWTools extension was also found during diagnostics:[m
[31m-tboby.cwtools-vscode, version 0.10.31[m
[31m-[m
[31m-No CWTools ignore rules are currently configured in the workspace.[m
[31m-[m
[31m-[m
[31m-11. Text command-reference file[m
[31m-===============================[m
[31m-[m
[31m-A previous file named git-commands.txt was created with commented Git commands.[m
[31m-It was later removed or overwritten during synchronization with GitHub and is not[m
[31m-currently part of the repository listing.[m
[31m-[m
[31m-[m
[31m-12. Current repository check[m
[31m-============================[m
[31m-[m
[31m-Use these commands to check the current state before making changes:[m
[31m-[m
[31m-git status --short --branch[m
[31m-git remote -v[m
[31m-git log --oneline --decorate -5[m
[31m-[m
[31m-The expected remote is:[m
[31m-https://github.com/Tykanek/Hoi4-mod.git[m
[31m-[m
[31m-Never share GitHub tokens, passwords, or private SSH keys.[m
