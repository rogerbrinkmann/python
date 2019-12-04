import datetime

date = datetime.datetime.now()

# %a weekday short:             Mon
# %A weekday long:              Monday
# %b month short:               Sep
# %B month long:                September
# %d day:                       21
# %m month:                     09
# %H hour:                      20
# %M minute:                    10
# %y year short:                19
# %Y year long:                 2019
# %S seconds:                   10
# %x date:                      09/21/19
# %x time:                      20:26:54
# %T time:                      20:26:54
# %I hour:                      08
# %f microsecond                136691
# %p                            AM/PM
# %j day of the year            256
# %c day time representation:   Sat Sep 21 20:37:21 2019

print(f"The date is: {date: %c}")