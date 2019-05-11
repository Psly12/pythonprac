def minutes_to_hours(minutes):
    '''while minutes > 0'''
    return minutes//60,minutes%60
hrs,mins = minutes_to_hours(int(input("Enter minutes : ")))
print("Hour/s : {} & Minute/s : {}".format(hrs,mins))