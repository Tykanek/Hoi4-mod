with open('interface/BEN_focus_icons.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

# Check if already added
if 'GFX_focus_BEN_eyes_on_prague' in text:
    print('Already added!')
else:
    new_sprites = """
	# ============================================================
	# Anti-Prague Covert Rivalry Focus Icons (8)
	# ============================================================

	spriteType = {
		name = "GFX_focus_BEN_eyes_on_prague"
		texturefile = "gfx/interface/goals/focus_BEN_eyes_on_prague.dds"
	}
	spriteType = {
		name = "GFX_focus_BEN_eyes_on_prague_shine"
		texturefile = "gfx/interface/goals/focus_BEN_eyes_on_prague.dds"
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationmaskfile = "gfx/interface/goals/focus_BEN_eyes_on_prague.dds"
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = "add"
			animationtype = "scrolling"
			animationrotationoffset = { x = 0.0 y = 0.0 }
			animationtexturescale = { x = 1.0 y = 1.0 }
		}
	}

	spriteType = {
		name = "GFX_focus_BEN_the_missing_rifles"
		texturefile = "gfx/interface/goals/focus_BEN_the_missing_rifles.dds"
	}
	spriteType = {
		name = "GFX_focus_BEN_the_missing_rifles_shine"
		texturefile = "gfx/interface/goals/focus_BEN_the_missing_rifles.dds"
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationmaskfile = "gfx/interface/goals/focus_BEN_the_missing_rifles.dds"
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = "add"
			animationtype = "scrolling"
			animationrotationoffset = { x = 0.0 y = 0.0 }
			animationtexturescale = { x = 1.0 y = 1.0 }
		}
	}

	spriteType = {
		name = "GFX_focus_BEN_follow_the_money"
		texturefile = "gfx/interface/goals/focus_BEN_follow_the_money.dds"
	}
	spriteType = {
		name = "GFX_focus_BEN_follow_the_money_shine"
		texturefile = "gfx/interface/goals/focus_BEN_follow_the_money.dds"
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationmaskfile = "gfx/interface/goals/focus_BEN_follow_the_money.dds"
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = "add"
			animationtype = "scrolling"
			animationrotationoffset = { x = 0.0 y = 0.0 }
			animationtexturescale = { x = 1.0 y = 1.0 }
		}
	}

	spriteType = {
		name = "GFX_focus_BEN_a_better_life_in_benesov"
		texturefile = "gfx/interface/goals/focus_BEN_a_better_life_in_benesov.dds"
	}
	spriteType = {
		name = "GFX_focus_BEN_a_better_life_in_benesov_shine"
		texturefile = "gfx/interface/goals/focus_BEN_a_better_life_in_benesov.dds"
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationmaskfile = "gfx/interface/goals/focus_BEN_a_better_life_in_benesov.dds"
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = "add"
			animationtype = "scrolling"
			animationrotationoffset = { x = 0.0 y = 0.0 }
			animationtexturescale = { x = 1.0 y = 1.0 }
		}
	}

	spriteType = {
		name = "GFX_focus_BEN_the_irregular_migration_scandal"
		texturefile = "gfx/interface/goals/focus_BEN_the_irregular_migration_scandal.dds"
	}
	spriteType = {
		name = "GFX_focus_BEN_the_irregular_migration_scandal_shine"
		texturefile = "gfx/interface/goals/focus_BEN_the_irregular_migration_scandal.dds"
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationmaskfile = "gfx/interface/goals/focus_BEN_the_irregular_migration_scandal.dds"
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = "add"
			animationtype = "scrolling"
			animationrotationoffset = { x = 0.0 y = 0.0 }
			animationtexturescale = { x = 1.0 y = 1.0 }
		}
	}

	spriteType = {
		name = "GFX_focus_BEN_the_invisible_hand_of_benesov"
		texturefile = "gfx/interface/goals/focus_BEN_the_invisible_hand_of_benesov.dds"
	}
	spriteType = {
		name = "GFX_focus_BEN_the_invisible_hand_of_benesov_shine"
		texturefile = "gfx/interface/goals/focus_BEN_the_invisible_hand_of_benesov.dds"
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationmaskfile = "gfx/interface/goals/focus_BEN_the_invisible_hand_of_benesov.dds"
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = "add"
			animationtype = "scrolling"
			animationrotationoffset = { x = 0.0 y = 0.0 }
			animationtexturescale = { x = 1.0 y = 1.0 }
		}
	}

	spriteType = {
		name = "GFX_focus_BEN_a_city_that_bleeds_its_rival"
		texturefile = "gfx/interface/goals/focus_BEN_a_city_that_bleeds_its_rival.dds"
	}
	spriteType = {
		name = "GFX_focus_BEN_a_city_that_bleeds_its_rival_shine"
		texturefile = "gfx/interface/goals/focus_BEN_a_city_that_bleeds_its_rival.dds"
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationmaskfile = "gfx/interface/goals/focus_BEN_a_city_that_bleeds_its_rival.dds"
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = "add"
			animationtype = "scrolling"
			animationrotationoffset = { x = 0.0 y = 0.0 }
			animationtexturescale = { x = 1.0 y = 1.0 }
		}
	}

	spriteType = {
		name = "GFX_focus_BEN_the_prague_files"
		texturefile = "gfx/interface/goals/focus_BEN_the_prague_files.dds"
	}
	spriteType = {
		name = "GFX_focus_BEN_the_prague_files_shine"
		texturefile = "gfx/interface/goals/focus_BEN_the_prague_files.dds"
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationmaskfile = "gfx/interface/goals/focus_BEN_the_prague_files.dds"
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = "add"
			animationtype = "scrolling"
			animationrotationoffset = { x = 0.0 y = 0.0 }
			animationtexturescale = { x = 1.0 y = 1.0 }
		}
	}
"""
    last_brace = text.rfind('}')
    if last_brace != -1:
        updated = text[:last_brace] + new_sprites + '\n}\n'
        with open('interface/BEN_focus_icons.gfx', 'w', encoding='utf-8') as f:
            f.write(updated)
        print('Updated interface/BEN_focus_icons.gfx with 8 new focus sprites!')
    else:
        print('ERROR: closing brace not found!')
