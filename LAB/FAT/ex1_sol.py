class AttendanceSystem:
    def __init__(self):
        """Initialize an empty attendance record."""
        self.records = {}

    def add_student(self, student_id: str, name: str):
        """Add a new student to the attendance system with error handling."""
        if not student_id or not name:
            print("Student ID and name cannot be empty.")
            return
        if student_id in self.records:
            print(f"Error: Student ID {student_id} already exists.")
        else:
            self.records[student_id] = {'name': name, 'attendance': {}}
            print(f"Student {name} added successfully.")

    def mark_attendance(self, student_id: str, date: str, status: str = "Present"):
        """Mark a student's attendance for a specific date with validation."""
        if student_id not in self.records:
            print(f"Error: Student ID {student_id} not found.")
            return
        if date in self.records[student_id]['attendance']:
            print(f"Error: Attendance for {self.records[student_id]['name']} on {date} is already recorded.")
            return
        if status not in ["Present", "Absent"]:
            print("Error: Status must be 'Present' or 'Absent'.")
            return
        
        self.records[student_id]['attendance'][date] = status
        print(f"Attendance marked for {self.records[student_id]['name']} on {date} as {status}.")

    def get_attendance(self, student_id: str):
        """Retrieve the attendance record of a specific student with validation."""
        if student_id not in self.records:
            print(f"Error: Student ID {student_id} not found.")
            return {}
        return self.records[student_id]['attendance']

    def get_summary(self):
        """Generate a summary of attendance for all students."""
        summary = {}
        for student_id, data in self.records.items():
            total_days = len(data['attendance'])
            present_days = sum(1 for status in data['attendance'].values() if status == "Present")
            summary[student_id] = {
                'name': data['name'],
                'total_days': total_days,
                'present_days': present_days,
                'attendance_percentage': (present_days / total_days * 100) if total_days > 0 else 0.0
            }
        return summary


if __name__ == "__main__":
    attendance = AttendanceSystem()
    attendance.add_student("1", "Gokul")
    attendance.add_student("2", "John")
    attendance.add_student("3", "Doe")
    attendance.mark_attendance("1", "2023-01-01", "Present")
    attendance.mark_attendance("1", "2023-01-02", "Absent")
    attendance.mark_attendance("2", "2023-01-01", "Present")
    attendance.mark_attendance("2", "2023-01-02", "Present")
    attendance.mark_attendance("3", "2023-01-01", "Absent")
    attendance.mark_attendance("3", "2023-01-02", "Present")
    print(attendance.get_summary())