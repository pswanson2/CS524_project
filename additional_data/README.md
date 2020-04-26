# Additional data

## This folder contains additional data
-	class_data.json planned to be parsed in by project
-	class_data.txt
completed by Peter Swanson and Zhiwen Xu
-	toJson.py, very simple script. Run: python toJson.py
compiles class_data.txt into class_data.json
### Below is data structure for class_data.json
#### industry_rating
	int 0-9 
#### research_rating
	int 0-9 
#### Course_type 
determined by the CS department, used solely for determining graduation requirements. Duplicate allowed,
Cannot be empty
	basic_cs = required CS
	basic_math = required Math 
	add_math = additional Math
	theory = theory class
	soft_hard = software/hardware
	app = application
	elect = elective 
//req = required (note required does not imply non-elective)
#### course_cat
used to sort students interests, duplicate also allowed, empty allowed
	Ai = artificial intelligence
	Arc = computer architecture
	Sys = computer system
	App= Application development
	ThAl= Theory and Algorithm
	Eco=Economics
	Rob= Robotics
	Dat= Data analysis
	Bio = Biomedical

#### season_offered
	SP = spring, FA = fall, S=summer, NF = not frequent
#### Professor 
	Lastname, Firstname
