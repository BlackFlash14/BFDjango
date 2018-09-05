def double_char(str):
  result = ""
  for char in str:
    result = result + char*2
  return result

def count_hi(str):
  return str.count('hi')

def cat_dog(str):
  if str.count('cat') == str.count('dog'):
    return True
  else:
    return False
