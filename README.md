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

## How to TAG using the skill tree

Before showing examples, we are reiterating important rules and definitions of skills and the skill tree.
All the rules can be found in the skill tree [Readme.md](https://github.com/HPC-certification-forum/skill-tree/blob/master/README.md).

### Skills

A skill is a learnable unit of content, which can be taught in no more then 4 hours and no less then 1 hours.
A skill does not have a difficulty but can have requirements.

If the content of a skill has more content then or grows beyond 4 hours of teaching, it will be split into sub skills.
The simple, original name remains and becomes an overview.
All sub skill get more descriptive names.
Splitting has to be done in a way which ensures that an update of the certificate to the new sub skill is possible.

A skill overview contains the content of all the sub skills and can be used for linking as requirement.
Linking it means, that only a broad understanding of the skill is required and not a specific set of skills.
Using an overview of a skill for a course, means that only some of the content is relevant for a course and only an overview of a topic is given.

An overview cannot be examined an no credentials will be handed out, only actual skills do this.

### Skill tree

The skill tree contains the architecture of the skills.
Architecture means division of skill and skill categories.

Requirements are not mapped in the tree.
A network representation would be required for this to work properly.

### Skill Markdown files

Each skill and skill overview has a Markdown file containing information about the content as well as requirements.
They are directly linked in the Mind Map.

### Changes to the skill tree

Usually, only the leaves will change, meaning they will split into smaller and smaller leaves.
An overview will be created and the certificated updated to the new sub skill.
All requirements will now link to the overview unless changed by a skill curator.

### Example 1

The skill "Linux Bash" can be taught within two hours.
It has no difficulty, but many beginner courses list this skill.

If this skill is split in the future, this becomes an overview.
The content this skill had will be put into a sub skill and all certificates will be updated to the new skill.

### Example 2

The skill "Shell scripting" can be taught within four hours and has the requirement "Linux Bash".
It is a larger topic and could be taught in beginner and advanced user courses.
Using this skill as is will work if only basics are taught.
If the content growth beyond four hours, the skill has to be split into sub skills (shown below)
Calling them "shell scripting basic", "shell scripting advanced" is not accurate enough.

The advised procedure is to name the skill with regards to the specific content.
A course about basic Linux usage would list these skills:
* Linux Bash commands
* Linux Bash, environment and variables
* Shell scripting bash commands

A advance Linux course would list these requirements:
* Linux Bash (the overview)
* Shell scripting bash commands
The course also lists these skills as content:
* Linux Bash, sed, grep and awk
* Shell scripting, branching
* Shell scripting, loops and list iterations
