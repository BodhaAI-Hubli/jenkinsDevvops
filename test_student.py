from student import student_details
def test_student_details():
    s = student_details("Anu", "1XX23CS001", "ABC College", "Hubballi", "anu@example.com")
    assert s["name"] == "Anu"
    assert s["USN"] == "1XX23CS001"
    assert s["collage"] == "ABC College"
    assert s["city"] == "Hubballi"
    assert s["email"] == "anu@example.com"

    def test_student_without_email():
        s = student_details("Raj", "1XX23CS002", "XYZ College", "Dharwad")
        assert s["email"] is None