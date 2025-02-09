#################################################################
# REGION DATA
region_code_to_name = {
    "SU": "Outskirts",
    "HI": "Industrial Complex",
    "DS": "Drainage System",
    "GW": "Garbage Wastes",
    "SL": "Shoreline",
    "VS": "Pipeyard",
    "SH": "Shaded Citadel",
    "UW": "The Exterior",
    "SS": "Five Pebbles",
    "CC": "Chimney Canopy",
    "SI": "Sky Islands",
    "LF": "Farm Arrays",
    "SB": "Subterranean",
    "MS": "Submerged Superstructure",
    "OE": "Outer Expanse",
    "LC": "Metropolis",
    "DM": "Looks to the Moon",
    "CL": "Silent Construct",
    "RM": "The Rot",
    "UG": "Undergrowth",
    "LM": "Waterfront Facility",
    "HR": "Rubicon",

    "SU^": "Outskirts filtration",
    "SL^": "Shoreline above Moon",
    "SS^": "Five Pebbles above puppet",
    "SB^": "Subterranean ravine",
    "MS^": "Bitter Aerie",
    "OE^": "Outer Expanse filtration",
    "LM^": "Eastern Precipice",
}

region_name_to_code = {v: k for k, v in region_code_to_name.items()}
regions_all = list(region_code_to_name.keys())

scug_id_to_starting_region = {
    "Yellow": "SU",
    "White": "SU",
    "Red": "LF",
    "Gourmand": "SH",
    "Artificer": "GW",
    "Rivulet": "DS",
    "Spear": "SU^",
    "Saint": "SI",
    "Inv": "SH"
}

setting_to_region_code = {
    1: "SU",
    2: "HI",
    3: "DS",
    4: "GW",
    5: "SL",
    6: "SH",
    7: "UW",
    8: "SS",
    9: "CC",
    10: "SI",
    11: "LF",
    12: "SB",

    20: "VS",
    21: "LM",
}

story_regions_vanilla = {"SU", "HI", "DS", "GW", "SL", "SH", "UW", "SS", "CC", "SI", "LF", "SB"}

story_regions = {
    "Vanilla": {scug: story_regions_vanilla for scug in ["Yellow", "White", "Red"]},
    "MSC": {
        "Yellow": story_regions_vanilla.union({"VS"}),
        "White": story_regions_vanilla.union({"VS"}),
        "Red": story_regions_vanilla.union({"VS"}),
        "Gourmand": story_regions_vanilla.union({"OE"}),
        "Artificer": story_regions_vanilla.union({"LC", "LM"}).difference({"SL"}),
        "Rivulet": story_regions_vanilla.union({"RM", "MS"}).difference({"SS"}),
        "Spear": story_regions_vanilla.union({"DM", "LM"}).difference({"SL"}),
        "Saint": story_regions_vanilla.union({"UG", "CL", "HR"}).difference({"DS", "SH", "UW", "SS"}),
    }
}

story_regions_msc = story_regions_vanilla.union({"VS"})
story_regions_gourmand = story_regions_msc.union({"OE"})
story_regions_artificer = story_regions_msc.union({"LC", "LM"}).difference({"SL"})
story_regions_rivulet = story_regions_msc.union({"RM", "MS"}).difference({"SS"})
story_regions_spearmaster = story_regions_msc.union({"DM", "LM"}).difference({"SL"})
story_regions_saint = story_regions_msc.union({"UG", "CL", "HR"}).difference({"DS", "SH", "UW", "SS"})

#################################################################
# SCUG DATA
setting_to_scug_id = {
    "monk": "Yellow",
    "survivor": "White",
    "hunter": "Red",
    "gourmand": "Gourmand",
    "artificer": "Artificer",
    "rivulet": "Rivulet",
    "spearmaster": "Spear",
    "saint": "Saint",
    "sofanthiel": "Inv",
    "inv": "Inv",
    0: "Yellow",
    1: "White",
    2: "Red",
    10: "Yellow",
    11: "White",
    12: "Red",
    13: "Gourmand",
    14: "Artificer",
    15: "Rivulet",
    16: "Spear",
    17: "Saint",
    18: "Inv"
}

scug_id_to_name = {
    "Yellow": "Monk",
    "White": "Survivor",
    "Red": "Hunter",
    "Gourmand": "Gourmand",
    "Artificer": "Artificer",
    "Rivulet": "Rivulet",
    "Spear": "Spearmaster",
    "Inv": "Sofanthiel",
    0: "Monk",
    1: "Survivor",
    2: "Hunter",
    10: "Monk",
    11: "Survivor",
    12: "Hunter",
    13: "Gourmand",
    14: "Artificer",
    15: "Rivulet",
    16: "Spearmaster",
    17: "Saint",
    18: "Sofanthiel"
}

scugs_all = ['Yellow', 'White', 'Red', 'Gourmand', 'Artificer', 'Rivulet', 'Spear', 'Saint', 'Inv']
scugs_vanilla = ['Yellow', 'White', 'Red']

#################################################################
# PASSAGE DATA
passages_vanilla = ["Chieftain", "DragonSlayer", "Friend", "Hunter", "Monk",
                    "Outlaw", "Saint", "Scholar", "Survivor", "Traveller"]
passages_all = ["Chieftain", "DragonSlayer", "Friend", "Hunter", "Martyr", "Monk", "Mother",
                "Nomad", "Outlaw", "Pilgrim", "Saint", "Scholar", "Survivor", "Traveller"]
# Passages that can't be automatically set as priority until early logic detection improves.
prioritizable_passages = set(passages_all) - {"Chieftain", "Traveller", "Mother"}

dragonslayer_vanilla = ["GreenLizard", "PinkLizard", "BlueLizard", "WhiteLizard", "YellowLizard", "BlackLizard"]
dragonslayer_msc = dragonslayer_vanilla + ["CyanLizard", "RedLizard", "SpitLizard", "ZoopLizard"]
lizards_any = dragonslayer_msc + ["Salamander", "EelLizard", "TrainLizard"]

echoes_vanilla = ['CC', 'SI', 'LF', 'SB', 'SH', 'UW']

monk_foods_vanilla = ['DangleFruit', 'BubbleFruit', 'SeedCob', 'SlimeMold']
monk_foods_msc = ['LillyPuck', 'GlowWeed', 'DandelionPeach', 'GooieDuck', 'Seed', 'FireEgg']

slugpup_normal_regions = ['SU', 'HI', 'DS', 'SL', 'GW', 'SH', 'UW', 'CC', 'SI', 'LF', 'SB', 'VS', 'OE']

outlaw_insignificant = ["Fly", "SmallCentipede", "Snail", "PoleMimic", "TubeWorm", "Overseer"]

scavenger_tolls = ["SU", "GW", "LF", "LC", "CL", "OE", "UG"]

#################################################################
# FOOD QUEST DATA

food_quest_items = [
    "SlimeMold", "DangleFruit", "Fly", "Mushroom", "BlackLizard", "WaterNut",
    "JellyFish", "JetFish", "GlowWeed", "Salamander", "Snail", "Hazer",
    "EggBug", "LillyPuck", "YellowLizard", "TubeWorm", "SSOracleSwarmer", "Centiwing",
    "DandelionPeach", "CyanLizard", "GooieDuck", "RedCentipede"
]
alt_food_quest_items = {"Salamander": ["Salamander", "EelLizard"], "RedCentipede": ["RedCentipede", "Aquapede"]}

food_quest_survivor_inedible = {
    "BlackLizard", "JetFish", "Salamander", "Snail", "EggBug", "YellowLizard", "TubeWorm", "CyanLizard"
}
food_quest_spearmaster_inedible = {
    "SlimeMold", "DangleFruit", "WaterNut", "JellyFish", "GlowWeed", "LillyPuck", "DandelionPeach", "GooieDuck"
}
food_quest_saint_inedible = {
    "Fly", "BlackLizard", "JellyFish", "JetFish", "Salamander", "Snail", "Hazer", "EggBug", "YellowLizard", "TubeWorm",
    "Centiwing", "CyanLizard", "RedCentipede"
}
