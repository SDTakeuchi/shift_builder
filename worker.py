from dataclasses import dataclass
from datetime import datetime

@dataclass
class Employee():
    name: str
    hour_total: int
    unavailable_day_of_week: list[int]
    unavailable_days: list[int]
    must_work_hours: list[list[datetime]]

# 0: sunday ... 6: saturday
day_of_week = [0, 1, 2, 3, 4, 5, 6]
