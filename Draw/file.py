import re


def DefString(files, keyphrase):
  strng = ''
  with open(files) as infile:
    copy = False
    for line in infile:
        if line.strip() == keyphrase:
            copy = True
        elif line.strip() == "Finished":
            copy = False
        elif copy:
            strng.append(line)
  if strng == '':
    print "String is empty"
  else:
    return strng


  """stringrtrn = ''
  with open('file.txt', 'r') as searchfile:
      for line in searchfile:
          if keyphrase in line:
            stringrtrn.append(line)
  return stringrtrn"""
