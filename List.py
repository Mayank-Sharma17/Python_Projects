# collection of iteams or collection of premitive data types
marks = [95, 98, 97]
print(marks)
print(marks[0]) # 0th index pr jo marks hai agar vo print karan ho
print(marks[-1]) # '-'piche ke ginte shure kar rahe hai yaha 97 print hoga
# agar shuraat ke sirf 2 subject ke marks chaea
print(marks[0:2]) # 2th index vala exclude hai 95 98 print hoga

for score in marks:
    print(score)

# like operations on string
marks.append(99)
print(marks)

marks.insert(0, 99) # 0th index pr 99 marks store kara de
print(99 in marks) # check if the element exists in marks or not here it is true

print(len(marks)) # length of marks list

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

# agar pure list ko kahale karna hai
marks.clear()
print(marks)