def cigar_party(cigars, is_weekend):
  if is_weekend == True:
    return cigars >= 40
  else:
    return cigars >= 40 and cigars <= 60

def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you > 8 or date > 8:
    return 2
  else:
    return 1

def squirrel_play(temp, is_summer):
  if (is_summer == False and temp in range(60, 91)) or (is_summer == True and temp in range(60, 101)):
    return True
  else:
    return False

def caught_speeding(speed, is_birthday):
  if is_birthday == False and speed in range(61) or (is_birthday == True and speed in range(66)):
    return 0
  elif (speed in range(61, 81)) or (is_birthday == True and speed in range(86)):
    return 1
  elif speed >= 81 or (is_birthday == True and speed >= 86):
    return 2

def sorta_sum(a, b):
  c = a + b
  if c in range(10,20):
    return 20
  else:
    return c

def alarm_clock(day, vacation):
  week_preset = "7:00" if not vacation else "10:00"
  weekend_preset = "10:00" if not vacation else "off"
  return week_preset if day not in [6, 0] else weekend_preset

def love6(a, b):
  if (a == 6 or b == 6) or a + b == 6 or abs(a-b) == 6:
    return True
  else:
     return False

def in1to10(n, outside_mode):
  if n == 1 or n == 10:
    return True
  return (n in range(1,11)) ^ outside_mode

def near_ten(num):
  if (num + 2) % 10 == 0 or (num - 2) % 2 == 0:
    return True
  else:
    return False
