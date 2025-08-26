def add_time(start, duration, day=None):
    colon_index = start.index(':')
    start_hour = int(start[:colon_index])
    start_min = int(start[colon_index + 1:colon_index + 3])
    am = True if start[colon_index + 4:] == 'AM' else False

    colon_index = duration.index(':')
    hours_elapsed = int(duration[:colon_index])
    mins_elapsed = int(duration[colon_index + 1:])

    days_past = 0

    new_min = (start_min + mins_elapsed) % 60

    if new_min < start_min:
        start_hour = (start_hour + 1) % 12
        if start_hour == 0:
            am = not am
            if am:
                days_past += 1
    
    days_past += hours_elapsed // 24
    hours_elapsed %= 24

    if hours_elapsed >= 12:
        am = not am
        if am:
            days_past += 1
        hours_elapsed %= 12

    new_hour = (start_hour + hours_elapsed) % 12

    if new_hour < start_hour:
        am = not am
        if am:
            days_past += 1

    new_time = str(new_hour) if new_hour != 0 else '12'
    new_time += ':'

    if new_min < 10:
        new_time += '0'

    new_time += str(new_min)

    new_time += ' AM' if am else ' PM'

    if day:
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        day = day[0].upper() + day[1:].lower()
        new_day_index = (days.index(day) + days_past) % 7
        new_time += ', ' + days[new_day_index]
    
    if days_past > 0:
        if days_past == 1:
            new_time += ' (next day)'
        else:
            new_time += f' ({days_past} days later)'

    return new_time
