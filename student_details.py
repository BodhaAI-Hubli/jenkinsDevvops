def student_details(name, USN, college, city, email=None):
    return {
        "name": name,
        "USN" : USN,
        "College" : college,
        "city" : city,
        "email" : email

    }

if __name__ == "__main__":
    name = input("Enter the name: ")
    usn = input("Enter USN: ")
    college = input("Enter college: ")
    city = input("Enter city: ")
    email = input("Enter email: ")
    print(student_details(name, usn, college, city, email))
