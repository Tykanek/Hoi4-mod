# HOI4 Mod — Loading Screens System Stable Backup (v1.0)

- **Date:** 2026-11-05
- **Target HOI4 Version:** 1.19.4.1
- **Stable Git Commit Hash:** `7772e637b675de8ec06b339781bc79cca5139393` (`7772e63`)
- **Backup Branch Name:** `backup/loading_screens_v1_pass`
- **Annotated Tag Name:** `loading-screens-v1.0-stable`
- **Tag Annotation:** `Verified in-game: 8 bonus loading screens, existing loading images preserved, main menu backgrounds unchanged.`

---

## 1. Executive Summary

This document marks the permanent baseline of the fully verified custom loading screen system for the mod **German-Czech Advanced** (`Hoi4-mod`). All eight bonus illustrations (`bonus_1` through `bonus_8`), the nine original custom loading screens (`load_1` through `load_9`), eighteen vanilla DLC loading screen overrides, and the six main menu backgrounds have been verified in-game on Hearts of Iron IV 1.19.4.1.

The game starts cleanly, the random loading screen rotation smoothly rotates through all custom images, and the main menu background selector remains isolated and unaffected.

---

## 2. Asset Structure & File Counts

All active loading assets reside in `gfx/loadingscreens/`, while the original source copies of the bonus illustrations remain safely preserved in `gfx/bonus/`.

### Texture Categories in `gfx/loadingscreens/` (41 Full-Size DDS Files)

| Category | Filenames | Count | Dimensions | Format |
| :--- | :--- | :---: | :---: | :---: |
| **Standard Loading Screens** | `load_1.dds` to `load_9.dds` | 9 | 1920×1440 | 32-bit ARGB uncompressed DDS |
| **Bonus Loading Screens** | `bonus_1.dds` to `bonus_8.dds` | 8 | 1920×1440 | 32-bit ARGB uncompressed DDS |
| **Main Menu Backgrounds** | `main_menu_1.dds` to `main_menu_6.dds` | 6 | 1920×1440 | 32-bit ARGB uncompressed DDS |
| **DLC Loading Screen Overrides** | `load_aat.dds`, `load_aat2.dds`, `load_bba.dds`, `load_botb.dds`, `load_dod.dds`, `load_goe.dds`, `load_lar.dds`, `load_mtg.dds`, `load_mtg_2.dds`, `load_ncns_chi.dds`, `load_ncns_jap.dds`, `load_nsb.dds`, `load_nsb2.dds`, `load_taog_ast.dds`, `load_tfv.dds`, `load_tiger.dds`, `load_toa.dds`, `load_ww.dds` | 18 | 1920×1440 | 32-bit ARGB uncompressed DDS |
| **Total Full-Size Loading Screens** | | **41** | | |

### Matching Thumbnail Files (`*_small.dds`)

Every full-size texture is paired with an exact 192×144 thumbnail:
- `load_1_small.dds` through `load_9_small.dds` (9 files)
- `bonus_1_small.dds` through `bonus_8_small.dds` (8 files)
- `main_menu_1_small.dds` through `main_menu_6_small.dds` (6 files)
- DLC thumbnail overrides (16 files)
- UI frame asset: `loading_screen_border_small.dds` (1 file)

### Preserved Archive Directory (`gfx/bonus/`)

The original 16 bonus DDS files remain completely intact in `gfx/bonus/`:
- `bonus_1.dds` through `bonus_8.dds` (1920×1440)
- `bonus_1_small.dds` through `bonus_8_small.dds` (192×144)

---

## 3. How the Loading Screen System Works

### Dynamic Discovery by Clausewitz Engine (`CFrontEndIdler`)
During game initialization and save/load cycles, the game engine's `CFrontEndIdler` reads the virtual file system directory `gfx/loadingscreens/`:
1. It scans for all `.dds` files in `gfx/loadingscreens/`.
2. Any filename ending in `_small.dds` is identified as a thumbnail and excluded from the full-screen loading pool.
3. All remaining `.dds` files are registered into an internal dynamic array of loading screens.
4. The engine randomly selects one texture from this array for each loading screen phase.

Because `bonus_1.dds` through `bonus_8.dds` reside directly in `gfx/loadingscreens/`, the game engine automatically discovers and displays them alongside `load_1.dds` through `load_9.dds`.

### Separation from Main Menu Backgrounds
The main menu background carousel is governed by an entirely separate database:
- **Registry:** `common/frontend/backgrounds/base_backgrounds.txt`
- **User Selection:** `settings.txt` (`background={ ... }`, `weight={ ... }`)
- **Timer Define:** `common/defines/menu_rotation_defines.lua` (`TIME_TO_SWAP_BACKGROUNDS = 20`)

In `base_backgrounds.txt`, only `main_menu_1` through `main_menu_6` are registered:
```pdx
main_menu_1 = { gfx = "GFX_main_menu_1" }
main_menu_2 = { gfx = "GFX_main_menu_2" }
main_menu_3 = { gfx = "GFX_main_menu_3" }
main_menu_4 = { gfx = "GFX_main_menu_4" }
main_menu_5 = { gfx = "GFX_main_menu_5" }
main_menu_6 = { gfx = "GFX_main_menu_6" }
```
Because `bonus_1` through `bonus_8` are **not** defined in `base_backgrounds.txt`, they never appear in the main menu background selector and will never be selected as main menu background images.

### Engine Limitation Note
HOI4 requires all textures defined in `base_backgrounds.txt` to reside physically inside `gfx/loadingscreens/`. Because of this engine requirement, `main_menu_1.dds` through `main_menu_6.dds` are also present in `gfx/loadingscreens/`, meaning they can occasionally appear as startup loading screens. The reverse is fully controlled: bonus images never leak into the main menu.

---

## 4. Key Configuration Files

| Purpose | File Path |
| :--- | :--- |
| Loading Screens Directory | `gfx/loadingscreens/` |
| Bonus Source Directory | `gfx/bonus/` |
| Main Menu Registry | `common/frontend/backgrounds/base_backgrounds.txt` |
| Main Menu Full-Size Sprites | `interface/frontendmainviewbg.gfx` |
| Main Menu Basic Sprites | `interface/frontendmainviewbg_basic.gfx` |
| Main Menu Thumbnails GFX | `interface/small_background.gfx` |
| Rotation Timer Define | `common/defines/menu_rotation_defines.lua` |
| Mod Descriptor (replace_path) | `descriptor.mod` |

---

## 5. Safe Inspection & Comparison Commands

To inspect this backup without modifying working files:

- **View commit details and file list:**
  ```powershell
  git show --stat loading-screens-v1.0-stable
  ```
- **Compare current files against this stable backup:**
  ```powershell
  git diff loading-screens-v1.0-stable
  ```
- **Compare only loading screen assets against this backup:**
  ```powershell
  git diff loading-screens-v1.0-stable -- gfx/loadingscreens/
  ```
- **Inspect commit history leading to the verified baseline:**
  ```powershell
  git log -n 5 --oneline loading-screens-v1.0-stable
  ```

---

## 6. Safe Recovery Instructions

If loading screen assets are ever accidentally corrupted, modified, or deleted:

### Restoring Only Loading Screen Assets
To safely restore the verified loading screens without touching your active research, focus trees, or scripts:
```powershell
git checkout loading-screens-v1.0-stable -- gfx/loadingscreens/
```

### Creating a Fresh Recovery Branch
To explore or branch from this exact verified snapshot without touching active development:
```powershell
git switch -c recovery/loading-screens-v1 loading-screens-v1.0-stable
```

> [!CAUTION]
> **Never use destructive commands:**
> - Do **not** run `git reset --hard` (will discard uncommitted work in other subsystems).
> - Do **not** run `git clean -fd` (will delete untracked scratch tools and work in progress).
> - Do **not** run `git push --force`.

---

## 7. Disaster Recovery & Hardware Protection

> [!WARNING]
> **Local Git backups only protect against software reversions, not hardware failure.**
> Git branches and tags stored exclusively on your local disk will be lost if your hard drive fails, files are deleted, or the operating system is reinstalled.
>
> To safeguard this verified milestone against physical drive failure, push this stable branch and tag to your secure remote repository:
> ```powershell
> git push origin backup/loading_screens_v1_pass
> git push origin loading-screens-v1.0-stable
> ```
