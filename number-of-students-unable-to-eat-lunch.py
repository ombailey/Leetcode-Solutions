def countStudents(students,sandwiches):
    
    while students:
        if sandwiches[0] not in students:
            break
        
        elif students[0] == sandwiches[0]:
            del students[0]
            del sandwiches[0]
        
        else:
            stu = students[0]
            del students[0]
            students.append(stu)
       
    return len(students)

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(countStudents(students,sandwiches))