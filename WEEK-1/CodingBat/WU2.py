def string_times(str, n):
  result = ""
  for i in range(n):
    result = result + str
  return result


def front_times(str, n):
  result = ""
  if len(str) < 3:
    for i in range(n):
      result = result + str
    return result
  else:
    for i in range(n):
      result = result + str[0:3]
    return result

def string_bits(str):
  result = ""
  if len(str) == 1:
    return str
  else:
    for i in range (len(str)):
      if i%2 == 0:
       result = result + str[i]
    return result

def string_splosion(str):
  r1 = len(str)
  result = ""
  if r1 <= 1:
    return str
  else:
    for i in range(r1):
      result = result + str[:i+1]
    return result

def array_count9(nums):
  cnt = 0
  for i in nums:
    if i == 9:
      cnt += 1
  return cnt


def array_front9(nums):
  range1 = len(nums)
  if range1 > 4:
    range1 = 4
  for i in range(range1):
    if nums[i] == 9:
      return True
  else:
    return False

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  else:
    return False

def string_match(a, b):
  for i in range((len(a)-1) and (len(b)-1)):
    if a[i]+a[i+1] == b[i]+b[i+1]:
      return True
  else:
    return False
