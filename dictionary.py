student={
    'id1':{
        'name':['Jack'],
        'class':["VIII"],
        'subject_integration':['Science','English','Maths'],
    }, 

    'id2':{
        'name':['Sam'],
        'class':["VIII"],
        'subject_integration':['Science','English','Maths'],
    },
     'id3':{
        'name':['Sam'],
        'class':["VIII"],
        'subject_integration':['Science','English','Maths'],
    },
     'id4':{
        'name':['David'],
        'class':["VIII"],
        'subject_integration':['Science','English','Maths'],
    }
    
}
result={}
for i, j in student.items():
    if j not in result.values():
        result[i]=j
print(result)