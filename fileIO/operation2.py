f=open("students'","r")
student=[]
for stud in f:
    student.append(stud.rstrip("\n"))
# print(student)
g=open("fail.py","r")
failed=[]
for fail in g:
    failed.append(fail.rstrip("\n"))
# print(failed)
stpass=set(student)
stfail=set(failed)
# print(stpass)
# print(stfail)
diffe=stpass.difference(stfail)
print(diffe)