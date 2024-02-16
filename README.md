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

##

# Markdown axioms

### Leaf node axioms

**Format:** 

**Header** (The name of the leaf along with its coordinates)

**Description:** The description for a leaf node can be short or long depending on the section, but it does not need to be comprehensive.

**Requirements:** This section must have a list of requirements needed to learn the contents of a leaf. Requirements are split further into external and internal requirements. Any requirements present on the skill tree are internal. Any skill that needs to be learnt externally before learning the particular skill is an external requirement. A leaf node need not have either of these sections filled if there are no requirements to learn the skill. Local requirements must be linked within the Skill Tree and the Wiki.

**Learning Objectives:** Learning objectives is essentially a list of everything you need to learn to acquire a certification for the particular leaf node. It is a comprehensive list of everything you need to know. The learning objectives also form the base of the testing phase of HPC CF, where candidates will be tested online for their knowledge of the topics covered under the learning objectives.

**Get tested:** This section appears when an online test for a particular leaf is available. It links the user directly to an online test. 

**Sections which are blank need not be represented in the Markdown. However, some sections like Header, Description and Learning Objectives are compulsory in the leaf nodes markdown file.**

### Overview node axioms

**Format:** 

**Header:** (The name of the overview section along with its coordinates)

**Description:** This is the most crucial section of the Overview leaf. Unlike leaf nodes, where descriptions don’t need to be comprehensive. Descriptions on the Overview nodes must cover every leaf present on its branch. Overview is meant to be an introductory topic, a way to cover a topic without going in depth. While the description explains all the leaves on the branch, it need not be an in-depth description. Instead, it should only cover the critical information that the user must know. The overview node, however, must have more of a structure to its description. The structure must represent the other leaves on the branch, complete with links and coordinates.

**Requirements:** This section must have a list of requirements needed to understand the leaves on the branch. Requirements are split further into external and internal requirements. Any requirements present on the skill tree are internal. Any skill that needs to be learnt externally before learning the particular skill is an external requirement. An overview node need not have either of these sections filled if there are no requirements to learn the skill. Local requirements must be linked within the Skill Tree and the Wiki.


**There are no learning objectives or tests for an overview branch. The overview branch lets trainers pick and choose relevant topics within a branch to teach at any level required so it doesn’t need to complete the learning objectives that are strictly specified in the leaf sections.** 

**In Overview, only the Header and Description are required.**
