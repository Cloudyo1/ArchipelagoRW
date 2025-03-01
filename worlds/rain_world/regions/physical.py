from ..game_data.general import region_code_to_name, scugs_all
from ..game_data import static_data
from ..conditions.classes import Simple, AllOf
from ..options import RainWorldOptions
from .classes import ConnectionData, PhysicalRegion


def _generate(_: RainWorldOptions) -> list[PhysicalRegion | ConnectionData]:
    ret = []
    for region, region_data in static_data["MSC"].items():
        rooms = set(region_data.keys())

        match region:
            case "SU":
                # Not in logic (except for Saint) to go backwards through the tutorial/filtration area.
                filt = {r for r in rooms if "CAVE" in r or "PUMP" in r
                        or r in ("SU_VR1", "SU_PS1", "SU_C04", "SU_A41", "SU_A42", "SU_A43", "SU_A44", "SU_S05",
                                 "SU_INTRO01", "SU_X02", "SU_S10", "GATE_OE_SU[SU]")}
                ret += [
                    PhysicalRegion("Outskirts", "SU", rooms.difference(filt)),
                    PhysicalRegion("Outskirts filtration", "SU^", filt),
                    ConnectionData("Outskirts filtration", "Outskirts", "Exit Survivor tutorial area"),
                    ConnectionData("Outskirts", "Outskirts filtration", "Return to Survivor tutorial area",
                                   Simple("Scug-Saint")),
                ]

            case "MS":
                # Not in logic to access Bitter Aerie except as Rivulet.
                bitter = {name for name in rooms if "BITTER" in name or "SEWER" in name or "AERIE" in name
                          or name in ("MS_WILLSNAGGING01", "MS_S07", "MS_PUMPS", "MS_SCAVTRADER", "MS_JTRAP",
                                      "MS_COMMS", "GATE_SL_MS[MS]")}
                ret += [
                    PhysicalRegion("Submerged Superstructure", "MS", rooms.difference(bitter)),
                    PhysicalRegion("Bitter Aerie", "MS^", bitter),
                    ConnectionData("Submerged Superstructure", "Bitter Aerie", "Rarefaction cell deposit cutscene",
                                   Simple(["Scug-Rivulet", "Object-EnergyCell"])),
                ]

            case "SB":
                # Not in logic (except for Saint) to go back up the SB ravine.
                ravine = {"SB_A10", "SB_F03", "SB_TOPSIDE", "SB_S09", "GATE_LF_SB[SB]"}
                filt = {"SB_C05", "SB_C06", "SB_s03", "SB_S04", "SB_D04", "SB_F02", "SB_I01", "SB_E07", "SB_C10",
                        "SB_B04", "SB_S10", "SB_G04", "GATE_SB_VS[SB]", "SB_F01", "SB_J03", "GATE_DS_SB[SB]", "SB_S02"}
                ret += [
                    PhysicalRegion("Subterranean", "SB", rooms.difference(ravine.union(filt))),
                    PhysicalRegion("Subterranean ravine", "SB^", ravine),
                    ConnectionData("Subterranean", "Subterranean ravine", "Down the ravine"),
                    ConnectionData("Subterranean ravine", "Subterranean ravine", "Up the ravine",
                                   Simple("Scug-Saint")),

                    PhysicalRegion("Filtration System", "SB^2", filt),
                    ConnectionData("Subterranean", "Filtration System", "Enter Filtration System",
                                   Simple(["The Glow", "Option-Glow"], 1)),
                    ConnectionData("Filtration System", "Subterranean", "Exit Filtration System"),
                ]

            case "SS":
                # Not in logic to go backwards through Five Pebbles puppet room.
                above = {"GATE_SS_UW[SS]", "SS_D08", "SS_S04", "SS_E08", "SS_D07", "SS_AI"}
                ret += [
                    PhysicalRegion("Five Pebbles", "SS", rooms.difference(above)),
                    PhysicalRegion("Five Pebbles above puppet", "SS^", above),
                    ConnectionData("Five Pebbles", "Five Pebbles above puppet", "Out the access shaft")
                ]

            case "VS":
                # Not in logic to go through Sump Tunnel as Artificer.
                sump = {"VS_B15", "VS_A11", "VS_B14", "VS_A12", "VS_A15", "VS_B18", "VS_D05", "VS_C08", "VS_E01",
                        "VS_B05", "VS_D02", "VS_S02", "GATE_SL_VS[VS]"}
                filt = {"VS_C10", "VS_C12", "VS_C11", "VS_E02", "VS_B06", "BS_S03", "VS_H01", "GATE_SB_VS[VS]"}
                ret += [
                    PhysicalRegion("Pipeyard", "VS", rooms.difference(sump.union(filt))),
                    PhysicalRegion("Sump Tunnel", "VS^", sump),
                    ConnectionData("Pipeyard", "Sump Tunnel", "Enter Sump Tunnel",
                                   Simple(list(set(scugs_all).difference({"Artificer"})), 1)),
                    ConnectionData("Sump Tunnel", "Pipeyard", "Exit Sump Tunnel",
                                   Simple(list(set(scugs_all).difference({"Artificer"})), 1)),
                    PhysicalRegion("Pipeyard filtration", "VS^2", filt),
                    ConnectionData("Pipeyard", "Pipeyard filtration", "Enter dark filtration area",
                                   Simple(["The Glow", "Option-Glow"], 1)),
                    ConnectionData("Pipeyard filtration", "Pipeyard", "Exit dark filtration area"),
                ]

            # case "GW":
            #     if "EDGE" in name or name in ("A24", "A25", "S09"):
            #         return "Garbage Wastes (upper east)"
            #     elif name in ("C04", "B08", "S04"):
            #         return "Garbage Wastes (lower east)"
            #     return "Garbage Wastes"
            #
            # case "SL":
            #     if name in ("EDGE02", "EDGE01", "BRIDGE01", "BRIDGEEND", "S13"):
            #         return "Shoreline (broken precipice)"
            #     return "Shoreline"

            case _:
                ret.append(PhysicalRegion(region_code_to_name[region], region, rooms))

    ret.append(ConnectionData("Subterranean", "Rubicon", "Enter Rubicon",
                              AllOf(Simple("Karma", 8), Simple("Scug-Saint"))))

    return ret


def generate(options: RainWorldOptions):
    return _generate(options)
