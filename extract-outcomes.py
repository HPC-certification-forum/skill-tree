#!/usr/bin/env python3

import os
import sys

def find_skills():
  data = {}
  for root, dirs, files in os.walk("."):
      for f in files:
        if(f[-4:] == ".txt"):
          c = root[2:]
          if c in data:
            data[c].append(f)
          else:
            data[c] = [f]
  del data[""]
  return data

def find_section(data, section):
  pos = data.find("# " + section)
  if pos == -1:
    return ""
  rest = data[pos + 2 + len(section):].strip()
  pos = rest.find("# ")
  if pos == -1:
    return rest
  return rest[0:pos].strip()


def removeSection(data, section):
  pos = data.find("# " + section)
  if pos == -1:
    return data
  head = data[0:pos]
  rest = data[pos + 2:]

  pos = rest.find("# ")
  if pos == -1:
    return head

  return head + rest[pos:]

def extract_outcomes(file):
  fd = open(file, "r")
  data = fd.read()
  fd.close()
  return find_section(data, "Outcomes")


exist = find_skills()

for dir in exist:
  outcome_basic = ""
  files = exist[dir]
  files.sort()
  for f in files:
    path = dir + "/" + f
    outcomes = extract_outcomes(path)
    if len(outcomes) < 5:
      print("Missing learning objectives: " + path)
    if f == "b.txt":
      outcome_basic = outcomes
    else:
      if outcomes == outcome_basic:
        print("Same learning objectives as basic: " + path)

      removeSection("Subskills")

      if data != datanew:
      fd = open(file, "w")
      fd.write(datanew)
      fd.close()
