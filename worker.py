class Employee():
    def __init__(self, name, hour_total, desired_dayoffs):
        self.name: str = name
        self.hour_total: int = hour_total
        self.desired_dayoffs: list[int] = desired_dayoffs
        
