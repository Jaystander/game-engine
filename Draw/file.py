import re


def DefString(file, key):
  string = ''
  with open(file) as infile:
    copy = False
    for line in infile:
        if line.strip() == key:
            copy = True
        elif line.strip() == "Finished":
            copy = False
        elif copy:
            string = string + ' ' + line
  if string == '':
    raise Exception("String is empty")
  else:
    return string


  """stringrtrn = ''
  with open('file.txt', 'r') as searchfile:
      for line in searchfile:
          if keyphrase in line:
            stringrtrn.append(line)
  return stringrtrn"""
