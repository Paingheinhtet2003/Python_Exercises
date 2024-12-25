from datetime import datetime

date_str = input("Enter the time in 'yyyy/mm/dd hh:mm:ss' format: ")

date = datetime.strptime(date_str, "%Y/%m/%d %H:%M:%S")

formatted_date = f"{date.strftime('%Y-%m%d')}\n{'PM' if date.hour >= 12 else 'AM'} {date.strftime('%I:%M')}"

print(formatted_date)
                         
