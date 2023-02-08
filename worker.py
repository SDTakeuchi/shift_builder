from dataclasses import dataclass

@dataclass
class Employee():
    name: str
    hour_total: int
    desired_dayoffs: list[int]
    unavailable_days: list[int]

# 0: sunday ... 6: saturday
week = [0, 1, 2, 3, 4, 5, 6]
