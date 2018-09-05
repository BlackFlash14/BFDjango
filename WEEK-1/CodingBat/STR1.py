def hello_name(name):
  return 'Hello ' + name + "!"

def make_abba(a, b):
  return a + b + b + a

def make_tags(tag, word):
  return '<' + tag + '>' + word + '</' + tag + '>'

def make_out_word(out, word):
  return out[0:2] + word  + out[2:]

def extra_end(str):
  if len(str) >= 2:
    return str[-2:] + str[-2:] + str[-2:]
  else:
    return False

def first_two(str):
  if len(str) >= 2:
    return str[:2]
  else:
    return str

def first_half(str):
    return str[:len(str) / 2]

def without_end(str):
  if len(str) >= 2:
    return str[1:-1]
  else:
    return False

def combo_string(a, b):
  if len(a) < len(b):
    return a + b + a
  elif len(a) > len(b):
    return b + a + b
  else:
    return False

def non_start(a, b):
  if len(a) >= 1 and len(b) >= 1:
    return a[1:] + b[1:]
  else:
    return False

def left2(str):
  if len(str) >= 2:
    return str[2:] + str[0:2]
