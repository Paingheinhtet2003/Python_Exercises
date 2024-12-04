def valid_date(date, month):
    max_days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return "Invalid month! Month must be between 1 and 12"

    max_days = max_days_in_months[month - 1]
    if day < 1 or day > max_days:
        return "Invalid date! Month {} has {} days.".format(month, max_days)
    return "The date is valid."

date_input = input("Enter the date in DD/MM format: ")

day, month = map(int, date_input.split('/'))

print(valid_date(day, month))
