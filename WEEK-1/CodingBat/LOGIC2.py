def lone_sum(a, b, c):
  if a == b == c:
    return 0
  if a == b:
    return c
  if a == c:
    return b
  if b == c:
    return a
  else:
    return a + b + c

def no_teen_sum(a, b, c):
  def  fix_teen(n):
    if n not in(13, 14, 17, 18, 19):
      return n
    else:
      return 0
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def round_sum(a, b, c):
  def round10(num):
    return (num+5)/10*10

  return round10(a)+round10(b)+round10(c)

