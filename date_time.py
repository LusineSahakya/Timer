import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer)
        time.sleep(1)
        t -= 1

def parse_time(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

time_str = input("Enter the time in HH:MM:SS format: ")
total_seconds = parse_time(time_str)

countdown(total_seconds)