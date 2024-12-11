from collections import namedtuple

ZodiacRange = namedtuple("ZodiacRange", ["sign", "start_month", "start_day", "end_month", "end_day"])

zodiac_ranges = [
    ZodiacRange("魔羯座", 12, 22, 1, 19),
    ZodiacRange("水瓶座", 1, 20, 2, 18),
    ZodiacRange("雙魚座", 2, 19, 3, 20),
    ZodiacRange("牡羊座", 3, 21, 4, 19),
    ZodiacRange("金牛座", 4, 20, 5, 20),
    ZodiacRange("雙子座", 5, 21, 6, 20),
    ZodiacRange("巨蟹座", 6, 21, 7, 22),
    ZodiacRange("獅子座", 7, 23, 8, 22),
    ZodiacRange("處女座", 8, 23, 9, 22),
    ZodiacRange("天秤座", 9, 23, 10, 22),
    ZodiacRange("天蠍座", 10, 23, 11, 21),
    ZodiacRange("射手座", 11, 22, 12, 21),
]

def get_zodiac_sign(day, month):
    for zodiac in zodiac_ranges:
        if(month == zodiac.start_month and day >= zodiac.start_day) or (month == zodiac.end_month and day <= zodiac.end_day):
            return zodiac.sign
    return "Invalid date"

birth_date = input("Enter your birthday in DD/MM format: ").strip()

try:
    day, month = map(int, birth_date.split('/'))

    zodiac_sign = get_zodiac_sign(day, month)
    print(f"Your Zodiac Sign is: {zodiac_sign}")
except ValueError:
    print("Invalid date")
