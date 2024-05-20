from enum import Enum

class WaveParameters(Enum):
    WAVE_1 = {
        "ennemi_number" : 5,
        "base_number" : 5,
        "strong_number" : 0,
        "elite_number" : 0,
        "number_of_ticks" : 1400,
        "next_wave": None,
        "radius_spawn":[300,350],
        "wave_number":1
    }
    WAVE_2 = {
        "ennemi_number" : 10,
        "base_number" : 8,
        "strong_number" : 2,
        "elite_number" : 0,
        "number_of_ticks" : 1800,
        "next_wave": None,
        "radius_spawn":[300,350],
        "wave_number":2
    }
    WAVE_3 = {
        "ennemi_number" : 15,
        "base_number" : 12,
        "strong_number" : 3,
        "elite_number" : 0,
        "number_of_ticks" : 2400,
        "next_wave": None,
        "radius_spawn":[300,350],
        "wave_number":3
    }
    WAVE_4 = {
        "ennemi_number" : 25,
        "base_number" : 20,
        "strong_number" : 5,
        "elite_number" : 0,
        "number_of_ticks" : 2800,
        "next_wave": None,
        "radius_spawn":[300,350],
        "wave_number":4
    }
    WAVE_5 = {
        "ennemi_number" : 35,
        "base_number" : 26,
        "strong_number" : 7,
        "elite_number" : 2,
        "number_of_ticks" : 3200,
        "next_wave": None,
        "radius_spawn":[300,350],
        "wave_number":5
    }
    WAVE_6 = {
        "ennemi_number" : 50,
        "base_number" : 35,
        "strong_number" : 10,
        "elite_number" : 5,
        "number_of_ticks" : 3600,
        "next_wave": None,
        "radius_spawn":[300,350],
        "wave_number":6
    }

    @classmethod
    def set_next_waves(cls):
        cls.WAVE_1.value["next_wave"] = cls.WAVE_2
        cls.WAVE_2.value["next_wave"] = cls.WAVE_3
        cls.WAVE_3.value["next_wave"] = cls.WAVE_4
        cls.WAVE_4.value["next_wave"] = cls.WAVE_5
        cls.WAVE_5.value["next_wave"] = cls.WAVE_6

WaveParameters.set_next_waves()