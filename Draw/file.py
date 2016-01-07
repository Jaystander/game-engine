import re


def DefString(keyphrase):
  stringrtrn = ''
  with open('file.txt', 'r') as searchfile:
      for line in searchfile:
          if keyphrase in line:
            stringrtrn.append(line)
  return stringrtrn
