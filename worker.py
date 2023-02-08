class Employee():
    def __init__(self, name, hour_total, desired_dayoffs, unavailable_days):
        self.name: str = name
        self.hour_total: int = hour_total
        self.desired_dayoffs: list[int] = desired_dayoffs
        self.unavailable_days: list[int] = unavailable_days

# 0:sunday ... 6:saturday
week = [0, 1, 2, 3, 4, 5, 6]
