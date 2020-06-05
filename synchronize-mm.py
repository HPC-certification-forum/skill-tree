#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import re
import os


# This program compares the directory tree with the markdown and the MindMap, it:
# 1) prints the differences
# 2) creates new directories for the markdown

root = ET.parse('skill-tree.mm').getroot()

type = "B"
typeL = type.lower()
file_extension = "/" + typeL + ".txt"
modify_tree = True
verbose = False


def extractSkillPath(parents, txt):
  m = re.match("([A-Z0-9.]+): (.*)", txt)
  if m == None:
    return (None, None)

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
  return (p, title)

def addSubskills(data, parents, node):
  pos = data.find("# Subskills")
  if pos == -1:
    pos = len(data)
  head = data[0:pos]
  rest = data[len(head) + len("# Subskills"):].strip("\n")
  head = head.strip() + "\n\n# Subskills\n"

  for c in reversed(node):
    if not "TEXT" in c.attrib:
      continue
    txt = c.attrib["TEXT"]
    (path, title) = extractSkillPath(parents, txt)
    # get child identifier
    if path == None:
      continue

    path.append(typeL)
    link = ("[[skill-tree:%s]]" % ":".join(path)).lower()
    if rest.find(link) == -1:
      rest = "  * %s\n%s" % (link, rest)
      print("L " + "/".join(parents) + " ADDING " + link)
  data = head + rest

  return data

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



def addLinks(parents, type):
  data = ["# Links"]
  str = ("/".join(parents) + "/" + type).lower()
  data.append("  * [[https://www.hpc-certification.org/contribute-question/%s|Submit a proposal for an examination question]]" % str)

  return "\n\n" + "\n".join(data) + "\n"

def update(file, node, parents, txt):
  fd = open(file, "r")
  data = fd.readline()
  fd.close()

  # compare the content with the expected head
  head = "%s%s-%s %s" % (parents[0], ".".join(parents[1:]), type, txt)
  filehead = data[2:].strip()
  if filehead != head:
    print("M" + "  " * len(parents) + "\"" + head + "\" expected in " + file)
    print("F" + "  " * len(parents) + data[2:].strip())

  if modify_tree:
    fd = open(file, "r")
    data = fd.read()
    fd.close()
    data = data.replace(filehead, head)
    data = removeSection(data, "Links")

    datanew = addSubskills(data, parents, node)
    #datanew = datanew + addLinks(parents, type)
    if data != datanew:
      fd = open(file, "w")
      fd.write(datanew)
      fd.close()

def create(file, parents, txt):
  print("CREATED " + file + " - " + txt)

  head = parents[0] + ".".join(parents[1:])
  dir = "/".join(parents).lower()
  if not os.path.isdir(dir):
    os.makedirs(dir)

  fd = open(file, "w")
  fd.write("# %s-%s %s\n# Background\n\n# Aim\n\n# Outcomes" % (head, type, txt))
  fd.close()

def traverse(parents, node):
  prefix = "  " * len(parents)
  for child in node:
    if not "TEXT" in child.attrib:
      continue
    txt = child.attrib["TEXT"]
    (path, title) = extractSkillPath(parents, txt)
    if path == None:
      continue

    file = "/".join(path).lower()
    if verbose:
      print(prefix + txt)

    # now check if the expected file exist
    if not os.path.isfile(file + file_extension):
      if modify_tree:
        create(file + file_extension, path, title)
      else:
        update(file + file_extension, child, path, title)
    else:
      update(file + file_extension, child, path, title)

    traverse(path, child)

traverse([], root[0])
