#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import re
import os


# This program compares the directory tree with the markdown and the MindMap, it:
# 1) prints the differences
# 2) creates new directories for the markdown

root = ET.parse('skill-tree.mm').getroot()

type = "B"
file_extension = "/" + type.lower() + ".txt"
modify_tree = True
verbose = False

def update(file, parents, txt):
  fd = open(file, "r")
  data = fd.readline()
  fd.close()

  # compare the content with the expected head
  head = "%s%s-%s %s" % (parents[0], ".".join(parents[1:]), type, txt)
  filehead = data[2:].strip()
  if filehead == head:
    return
  print("M" + "  " * len(parents) + head)
  print("F" + "  " * len(parents) + data[2:].strip())
  if modify_tree:
    fd = open(file, "r")
    data = fd.read()
    fd.close()
    data = data.replace(filehead, head)
    fd = open(file, "w")
    fd.write(data)
    fd.close()

def create(file, parents, txt):
  print("CREATED " + file + " - " + txt)

  head = parents[0] + ".".join(parents[1:])
  dir = "/".join(parents).lower()
  if not os.path.isdir(dir):
    os.makedirs(dir)

  fd = open(file, "w")
  fd.write("""# %s-%s %s
# Background

# Aim

# Outcomes""" % (head, type, txt))
  fd.close()

def traverse(parents, node):
  prefix = "  " * len(parents)
  for child in node:
    if not "TEXT" in child.attrib:
      continue
    txt = child.attrib["TEXT"]
    m = re.match("([A-Z0-9.]+): (.*)", txt)
    if m == None:
      continue

    e = m.group(1)
    title = m.group(2)
    m2 = re.match("([A-Z]+)([0-9]+[^:]*)?", e)
    if m2:
      if m2.group(2) != None:
        p = [m2.group(1)]
        p.extend(m2.group(2).split("."))
      else:
        p = [m2.group(1)]
    else:
      p = parents.copy()
      p.append(e)

    # now check if the files exist
    file = "/".join(p).lower()
    if verbose:
      print(prefix + txt)

    if os.path.isfile(file + file_extension):
      update(file + file_extension, p, title)
    elif modify_tree:
      create(file + file_extension, p, title)

    traverse(p, child)

traverse([], root[0])
