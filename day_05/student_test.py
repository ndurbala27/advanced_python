from student_info import Student

# test 1
student_1 = Student('nate', 'durbala', '1276449547')
print(student_1)

# test 2
student_1.set_status('Active')
student_1.set_year('Senior')
print(student_1)

# test 3
student_1.set_courses('Math1', 'Python2', 'Biology')
print(student_1)

# test 4
print(student_1.get_full_name())

# test 5
student_id = student_1.get_ID()
print(student_id)

# test 6
student_1.set_dob('10-27-1985')
student_1.set_phone('515-729-4261')
student_1.set_email('ndurbala27@gmail.com')

student_dob = student_1.get_dob()
student_phone = student_1.get_phone()
student_email = student_1.email

print(student_dob)
print(student_phone)
print(student_email)

print(student_1)