# HOI4 Mod — Research System Stable Backup (v1.0)

- **Date:** 2026-11-05
- **Target HOI4 Version:** 1.19.4.1
- **Stable Git Commit Hash:** `1deccb92bb821edb3e5dcec5a73deb048fddca21` (`1deccb9`)
- **Backup Branch Name:** `backup/research_system_final_pass`
- **Annotated Tag Name:** `research-system-v1.0-stable`

---

## 1. Executive Summary

This document marks the permanent baseline of the fully verified custom research system for the mod **German-Czech Advanced** (`Hoi4-mod`). All technologies, GUI components, equipment templates, leader traits, and event-driven universal leader synchronization scripts have been confirmed functional in-game on HOI4 version 1.19.4.1.

---

## 2. Research System Structure & Verified Technologies

The custom research folder **Praha vs. Benešov** (`GCA_praha_benesov_folder`) contains seven technologies organized into three branches:

### Branch 1: Territorial Strongpoints & Tank Calibration (1936)
- **Benesov Roundabout Defense** (`GCA_benesov_roundabout_tech`):
  - **DLC Condition:** Active when *No Step Back* is **NOT** present (`NOT = { has_dlc = "No Step Back" }`).
  - **Modifier:** `army_defence_factor = 0.02` (+2.0% Division Defense).
- **Prague Tank Tuning Garage** (`GCA_prague_tank_tuning_tech`):
  - **DLC Condition:** Active when *No Step Back* is present (`has_dlc = "No Step Back"`).
  - **Modifier:** `armor_tech_reliability_factor = 0.02` (+2.0% Armor Technology Reliability).

### Branch 2: Czech Logistics & Mechanization
- **Škoda Fabia 1.9 TDI** (`GCA_skoda_fabia_tech`, 1936):
  - Unlocks motorized transport equipment `GCA_skoda_fabia_19_tdi_equipment`.
  - Fully researchable and producible in national production lines.
- **Škoda Octavia RS — Mechanized Edition** (`GCA_skoda_octavia_rs_mechanized_tech`, 1938):
  - Unlocks mechanized equipment `GCA_skoda_octavia_rs_mechanized_equipment`.
  - Prerequisite: Requires `GCA_skoda_fabia_tech`.

### Branch 3: Steroids & Doping (Vertical Progression)
Arranged vertically (`y = 0`, `y = 2`, `y = 4`) in `interface/countrytechtreeview.gui`:
1. **Steroids I — Natural Transformation** (`GCA_steroids_natural_transformation_tech`, 1937):
   - Grants political leader trait `GCA_steroids_natural_transformation_trait`: **+1.0% Division Attack** (`army_attack_factor = 0.01`).
2. **Doping II — Enhanced Performance** (`GCA_doping_enhanced_performance_tech`, 1939):
   - Prerequisite: Requires Steroids I.
   - Grants political leader trait `GCA_doping_enhanced_performance_trait`: **+1.0% Division Defense** (`army_defence_factor = 0.01`).
3. **Doping III — Grznar's Final Form** (`GCA_grznar_final_form_tech`, 1942):
   - Prerequisite: Requires Doping II.
   - Grants political leader trait `GCA_grznar_final_form_trait`: **+1.0% Division Attack** (`army_attack_factor = 0.01`).

### Final Combined Doping Bonuses
When a nation completes all three doping technologies, the additive stacking provides:
- **+2.0% Division Attack**
- **+1.0% Division Defense**

---

## 3. Universal Political Leader Synchronization Engine

The research bonuses permanently belong to the researching nation. Rather than hardcoding specific character IDs, parties, or ideologies, traits dynamically synchronize to whichever political character currently leads the country.

### Architecture
1. **Immediate Execution:** On technology completion, `on_research_complete` dispatches hidden country event `GCA_doping_events.1`, safely firing `GCA_sync_doping_leader_traits = yes` within country scope (avoiding startup/research completion crash `0xC0000005`).
2. **Universal Leadership Transfer:** Handled through `common/on_actions/GCA_doping_on_actions.txt` across:
   - `on_ruling_party_change` (coups, civil wars, ideology flips)
   - `on_government_change` (constitutional changes)
   - `on_new_term_election` (democratic elections)
   - `on_coup_succeeded`
   - `on_civil_war_end`
   - `on_startup` (game launch & save/load cycles)
   - `on_daily` (catches intra-party leader changes via focus trees or scripted events)
3. **Duplicate Prevention Guard:**
   Each synchronization block evaluates:
   ```pdx
   if = {
       limit = {
           has_tech = <doping_tech>
           NOT = { has_country_leader_with_trait = <doping_trait> }
       }
       add_country_leader_trait = <doping_trait>
   }
   ```
   This prevents log spam and avoids duplicate trait warnings in `error.log`.

---

## 4. Key Files Preserved

| Component | File Path |
| :--- | :--- |
| Technology Definitions | `common/technologies/GCA_praha_benesov_technologies.txt` |
| Folder Tag | `common/technology_tags/GCA_praha_benesov_folder.txt` |
| Equipment Definitions | `common/units/equipment/zz_GCA_praha_benesov_equipment.txt` |
| Leader Traits | `common/country_leader/GCA_research_traits.txt` |
| Scripted Sync Effects | `common/scripted_effects/GCA_doping_scripted_effects.txt` |
| Synchronization On-Actions | `common/on_actions/GCA_doping_on_actions.txt` |
| Safe Trigger Event | `events/GCA_doping_events.txt` |
| Research GUI Integration | `interface/countrytechtreeview.gui` |
| Research & Equipment GFX | `interface/GCA_praha_benesov_technologies.gfx` |
| Localisation (UTF-8 BOM) | `localisation/english/GCA_praha_benesov_tech_l_english.yml` |

---

## 5. Safe Inspection & Comparison Commands

To safely inspect this backup without modifying working files:

- **View commit details and modified files:**
  ```powershell
  git show --stat research-system-v1.0-stable
  ```
- **Compare current files against this stable backup:**
  ```powershell
  git diff research-system-v1.0-stable
  ```
- **Compare a single file against the stable backup:**
  ```powershell
  git diff research-system-v1.0-stable -- common/technologies/GCA_praha_benesov_technologies.txt
  ```
- **Inspect commit history leading up to the verified baseline:**
  ```powershell
  git log -n 5 --oneline research-system-v1.0-stable
  ```

---

## 6. Safe File Restoration Instructions

If future changes cause regressions or unintended behavior, individual files or the entire system can be restored cleanly:

- **Restore a single file to its verified stable state:**
  ```powershell
  git checkout research-system-v1.0-stable -- <file_path>
  ```
- **Create an isolated branch from this verified state for experimentation:**
  ```powershell
  git checkout -b experiment/new-tech research-system-v1.0-stable
  ```

---

## 7. Storage & External Backup Reminder

> [!IMPORTANT]
> The Git branch `backup/research_system_final_pass` and annotated tag `research-system-v1.0-stable` are stored locally on this machine within the `.git` repository.
> 
> Local Git references protect against code regressions, editing mistakes, and branch conflicts, but they **do not protect against local hardware failure or disk loss**.
> 
> To ensure complete disaster recovery, an external off-computer backup (such as pushing the branch and tags to an authorized remote repository or copying the folder to secure secondary media) is strongly recommended when external operations are authorized.
