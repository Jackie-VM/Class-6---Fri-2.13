#CRUD example

########### create
next_assignment_id = 1

new_id = "HW" + str(next_assignment_id)
print(new_id)

assignments = [
    {"id": new_id ,
    "title": = "Intro to DB",
    "description" : "basics"
    }
]
next_assignment_id += 1

new_id = "HW" + str(next_assignment_id)
assignments.append(
    {"id": new_id , 
     "title": = "case study",
    "description" : "ER design"
    }
)

print(assignments)

########### read
# goal is to seperate code into input-process-


## Query: display all assignment info
# input

# process

# output  - 1) start here
for assignment in assignments:
    print(assignment)

#-----------------------------------

## Query: find assignment with a title = Intro to DB and display its info
# input

# process
exists = False
found_assignment = None
for assignment in assignments:
    if assignment["title"] == "Intro to DB":
        exists = True
        found_assignment = assignment
        break

# output
if exists:
    print(found_assignment)
else:
    print("Assignment does not exist")

#-----------------------------------

## Query: update the title of an assignment with the title = Intro to DB to Introduction to Database
# input

if assignment["title"] == "Intro to DB":


# process

# output

