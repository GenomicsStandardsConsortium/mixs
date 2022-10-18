

CREATE TABLE "Database" (
	person_set TEXT, 
	pet_set TEXT, 
	org_set TEXT, 
	PRIMARY KEY (person_set, pet_set, org_set)
);

CREATE TABLE "Organization" (
	org_name TEXT, 
	pet_names TEXT, 
	PRIMARY KEY (org_name, pet_names)
);

CREATE TABLE "Person" (
	first_name TEXT, 
	last_name TEXT, 
	hobbies VARCHAR(7), 
	pet_names TEXT, 
	PRIMARY KEY (first_name, last_name, hobbies, pet_names)
);

CREATE TABLE "Pet" (
	pet_name TEXT, 
	species TEXT, 
	PRIMARY KEY (pet_name, species)
);
