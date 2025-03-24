from typing import Optional, Callable

from BaseClasses import MultiWorld, Location, LocationProgressType, Region
from ..options import RainWorldOptions
from ..conditions.classes import ConditionBlank, Condition
from ..constants import FIRST_ID
from worlds.generic.Rules import add_rule
from ..regions.classes import room_to_region
from ..game_data.general import region_code_to_name

location_map: dict[str, int] = {}
location_hints: dict[str, set[str]] = {}


class LocationData:
    def __init__(self, full_name: str, alt_names: list[str] | None, offset: Optional[int], region: str = "Menu",
                 access_condition: Condition = ConditionBlank):
        """
        Represents a location of any type.
        :param full_name:
        :param alt_names:
        :param offset:
        :param region:
        """
        self.full_name = full_name
        self.alt_names = alt_names or []
        self.id = None
        self.region = region
        self.access_condition: Condition = access_condition
        self.progress_type: LocationProgressType = LocationProgressType.DEFAULT
        if offset is not None:
            self.id = offset + FIRST_ID
            location_map[full_name] = self.id
            for alt_name in self.alt_names:
                location_hints.setdefault(alt_name, set()).update({full_name})

    def make(self, player: int, multiworld: MultiWorld, options: RainWorldOptions) -> bool:
        if self.pre_generate(player, multiworld, options):
            if (region := multiworld.get_region(self.region, player)) and region.populate:
                loc = Location(player, self.full_name, self.id, region)
                loc.progress_type = self.progress_type
                region.locations.append(loc)
                if self.access_condition is not ConditionBlank:
                    add_rule(loc, self.access_condition.check(player))
                return self.id is not None
        return False

    def pre_generate(self, player: int, multiworld: MultiWorld, options: RainWorldOptions) -> bool:
        """Prepare to generate the location, or return False if the location should not be generated."""
        return True


class RoomLocation(LocationData):
    def __init__(self, description: str, alt_names: list[str] | None, offset: Optional[int], room: str):
        """
        Represents a location that exists in a specific room.
        """
        super().__init__(f'{region_code_to_name[room.split("_")[0]]} - {description}', alt_names, offset)
        self.room = room

    def pre_generate(self, player: int, multiworld: MultiWorld, options: RainWorldOptions) -> bool:
        self.region = room_to_region[self.room]
        return True


class AbstractLocation(LocationData):
    def __init__(self, name: str, alt_names: list[str], offset: int, region: str,
                 access_condition: Condition = ConditionBlank):
        super().__init__(name, alt_names, offset, region, access_condition)


class Passage(AbstractLocation):
    def __init__(self, name: str, region: str, offset: int,
                 access_condition: Condition = ConditionBlank,
                 access_condition_generator:  Optional[Callable[[RainWorldOptions], Condition]] = None):
        super().__init__(f"Passage - {self.proper_name(name)}", [f"Passage-{name}"], offset, region, access_condition)
        self.acc_gen = access_condition_generator

    @staticmethod
    def proper_name(name: str):
        if name == "Traveller":
            return "The Wanderer"
        elif name == "DragonSlayer":
            return "The Dragon Slayer"
        return f'The {name}'

    def pre_generate(self, player: int, multiworld: MultiWorld, options: RainWorldOptions) -> bool:
        if self.acc_gen is not None:
            self.access_condition = self.acc_gen(options)
        return super().pre_generate(player, multiworld, options)
