Each of the checklists is represented by one file in this directory.

The example.json checklist is a good starting point for creating a new checklist.

Step by step instructions for creating a new checklist:

- git clone the MIxS repository (https://github.com/GenomicsStandardsConsortium/MIxS.git)
- cd into this directory cd MIxS/checklists
- create a copy of the Example.json (e.g. cp Example.json Lunar-Animal.json)
- edit the JSON file using the terms from ../fields/MIxS_terms.json
	- NOTE: any new field needs to be accepted by the MIxS curation team
		attempt to use fields whenever possible, simply search the MIxS_terms.json document for a suitable field
- validate your new checklist
	- ensure it is syntactically correct
	- identify any new fields that need to be introduced
- create a pull request
	NOTE: please make sure to
	- provide a good description of the use case you are trying to cover
	- justify any new fields/terms you want to create


