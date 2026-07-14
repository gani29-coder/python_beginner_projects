# # phone_details = {"ram":8,"storage":525,"mp":64}
# # print(phone_details["ram"])

# #student grading system
# student_grades = {"anjali":30,"satish":99,"ganesh":100,"nandini":100}
# for name,marks in student_grades.items():
#     if marks >=35:
#        print("pass")
#     else:
#        print("fail")

#vowels counter
word = "hyderabad"
vowels =["a","e","i","o","u"]
count = 0
for letter in word:
    if letter in vowels:
        count += 1
print(count) 
