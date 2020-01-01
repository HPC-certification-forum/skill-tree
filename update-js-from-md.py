#!/usr/bin/env python3
import re
import os
import json

# This program checks the directory tree from the markdown
# Creates new JSON documents for the webpage

def processFile(file, skill, skill_data):
  refs = []
  fd = open(file, "r")
  enabled = False
  first = True
  for line in fd:
    if re.match("# *[^ ]", line):
      enabled = False
      if first:
        m = re.match("# *(.*)-[A-Z] (.*)", line)
        if m:
          name = m.group(2)
          id = m.group(1)
    if re.match("# *Subskills", line):
      enabled = True
      continue
    if enabled:
      m = re.match(" *[*] *\[\[skill-tree:([^\]]*)\]\]", line)
      if m:
        new = m.group(1).upper().replace(":B", "").replace(":", "", 1).replace(":", ".")
        refs.append(new)
  fd.close()

  if id != skill:
    print("Error in file %s; id found is %s but expected %s " % (file, id, skill))
  d = {}
  d["id"] = skill
  d["define"] = "core data"
  d["level"] = "Merged"
  d["name"] = name
  skill_data.append(d)

  return refs



def addSkill(dict, skill):
  cdict = dict
  depth = 0
  for s in skill.split("/"):
    if depth == 0:
      str = s
    elif depth == 1:
      str = str + s
    else:
      str = str + "." + s
    depth = depth + 1
    if str not in cdict:
      cdict[str] = {}
    cdict = cdict[str]

  return cdict

def addSkills(skills, skill, children):
  d = addSkill(skills, skill)

  for child in children:
    d[child] = {}

sl = open("skill-links.json", "w")
sl.write("""
[
  {
    "attribute" : "links",
    "data" : {
""")

skill_data = []

first = True
skills = {}
for root, dirs, files in os.walk("."):
  path = root.split(os.sep)
  if root == ".":
    continue
  if "b.txt" not in files:
    continue
  if not first:
    sl.write(",\n");
  first = False
  skill = root[2:].upper()
  addSkill(skills, skill)

  skillID = skill.replace("/", "", 1).replace("/", ".")
  children = processFile(root + "/b.txt", skillID, skill_data)
  addSkills(skills, skill, children)
  sl.write("\"" + skillID + "\" : [\"<a href='https://www.hpc-certification.org/wiki/skill-tree/" + root[2:] + "/'>Online description</a>\"]")

sl.write("""    }
  }
]
""")
sl.close()

skill_data.append(
  {
    "id": "ST",
    "define": "core data",
    "category": "All",
    "name": "Skill Tree",
    "level": "Merged"
})

sd = open("skill-data.json", "w")
sd.write(json.dumps(skill_data, indent=2))
sd.close()

# Write tree structure out

st = open("skill-tree-structure.json", "w")
st.write(""" [
    {
        "tree": {
                "ST":
""")

st.write(json.dumps(skills, indent=2))

st.write("""\n                }
        ,
        "define": "tree"
    }
]
""")

st.close()
