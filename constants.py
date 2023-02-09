from enum import Enum, auto

class DayOfWeek(Enum):
    SUNDAY = auto()
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()

    def string():
        res = ''
        match self.value:
            case SUNDAY:
                res = '日'
            case MONDAY:
                res = '月'
            case TUESDAY:
                res = '火'
            case WEDNESDAY:
                res = '水'
            case THURSDAY:
                res = '木'
            case FRIDAY:
                res = '金'
            case SATURDAY:
                res = '土'
        return res

    # def parse_string():
    #     res = ''
    #     match self.value:
    #         case SUNDAY:
    #             res = '日'
    #         case MONDAY:
    #             res = '月'
    #         case TUESDAY:
    #             res = '火'
    #         case WEDNESDAY:
    #             res = '水'
    #         case THURSDAY:
    #             res = '木'
    #         case FRIDAY:
    #             res = '金'
    #         case SATURDAY:
    #             res = '土'
    #     return res



