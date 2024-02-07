# Skill tree

The file for the Skill tree  can be read using the open source software [freeplane](https://docs.freeplane.org/).
The newest version of freeplane (1.11.10) is needed.

## Axioms

### Base Axioms

1. A skill set is a general description of broader knowledge (like HPC knowledge or Unix operating system) and has, at maximum, a three-letter abbreviation.
1. A skill topic contains a set of teachable skills or skill topics (skill set: UNIX -> skill topic: CMD Line -> skills: basic commands, scripting, …)
1. A skill is one lecture unit teachable/ learnable in not more than 2 hours.
1. A mother node can be a skill set or a skill topic.
1. A child node can be a skill topic or a skill/lecture unit.
1. A leaf node is the smallest (Atom) child node, skill or lecture unit, or an overview.
1. Two leaf nodes on different mother nodes may have the same name but different coordinates.
1. The tree is a map/ network and both views may be required to comprehend the HPC CF.

### Governing Axioms

1. Names have to be short, to the point, and accurate.
1. A skill set and each skill topic has an overview leaf node, which is a cheat sheet for essential content. It serves as a reference when the entire branch does not need to be taught.
1. All skills on the skill tree need to be related to HPC. For example, when a vast topic like C++ programming is listed in the skill tree, it can only reference parts of the topic that are related to HPC. In this case, the basics of learning to program are beyond the scope of the skill tree.

### Requirements Axioms

1. Required knowledge can be a complete skill set, a specific skill topic, or a selection of skills.
1. Required knowledge is added to a skill set, skill topic, or skill by linking to the required skill, or an overview node of a skill set or topic if required.
1. Required knowledge for a skill topic is added to the overview leaf node.
1. There are instances where the required knowledge may not be part of the skill tree (i.e. rudimentary c++). In that instant, an external requirement will be specified.

### Further knowledge Axioms

1. Knowledge beyond the scope of a skill topic can be added by linking the skill or the overview of a skill set or topic.
1. Further knowledge is added to a skill topic by adding it as a leaf node, which includes the link (It has to be set as a subtopic style).
1. Further knowledge can have the same name as a leaf node on the same mother node.

