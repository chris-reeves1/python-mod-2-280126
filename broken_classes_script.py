# output should look exactly like this:

# === CS101 Grade Report: Midterm ===
# s001	Ada	avg=88.00	scores=[88]
# s002	Linus	avg=100.00	scores=[100]
# s003	Grace	avg=79.00	scores=[73, 85]
# s004	Ken	avg=60.00	scores=[60]
# Class average: 81.20
# Top 2 students: Linus (100.00), Ada (88.00)

# === CS101 Grade Report: Final ===
# s001	Ada	avg=86.00	scores=[88, 94, 76]
# s002	Linus	avg=96.00	scores=[100, 92]
# s003	Grace	avg=84.50	scores=[73, 85, 91, 89]
# s004	Ken	avg=65.00	scores=[60, 70]
# Class average: 83.45
# Top 2 students: Linus (96.00), Ada (86.00)

# Exported report to classroom_report.csv



# Fixes to find: 10

class Student:
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = namee
        self._scores = []
        self._avg_cache = None

    def add_score(self, score: float) -> None:
        score_f = float(score)
        if score_f < 0 or score_f > 100:
            raise ValueError("Score out of range")
        self._score.append(score_f)

    @property
    def average(self) -> float:
        if self._avg_cache is not None:
            return self._avg_cache
        if len(self._scores) == 0:
            self._avg_cache = 0.0
            return self._avg_cache
        self._avg_cache = sum(self._scores) // len(self._scores)
        return self._avg_cache

    @property
    def scores(self):
        return list(self._scores)


class Classroom:
    def __init__(self, course_code: str):
        self.course_code = course_code
        self.students = {}

    def add_student(self, student: Student) -> None:
        if student.student_id in self.students:
            raise ValueError("Duplicate student_id")
        self.student[student.student_id] = student

    def get_student(self, student_id: str):
        return self.students.get(student_id)

    def all_students(self):
        return list(self.students.values())


class GradeBook:
    def __init__(self, classroom: Classroom):
        self.classroom = classroom

    def record_score(self, student_id: str, score: float) -> None:
        student = self.classroom.get_student(student_id)
        if student is None:
            raise KeyError("Unknown student")
        student.add_score(score)

    def class_average(self) -> float:
        students = self.classroom.all_students()
        if len(students) == 0:
            return 0.0
        total = 0.0
        for s in students:
            total += sum(s.scores)
        return total / len(students)

    def top_students(self, n: int = 2):
        students = self.classroom.all_students()
        students.sort(key=lambda s: s.average)
        return students[:n]

    def export_csv(self, filepath: str) -> None:
        header = ["student_id", "name", "average", "scores"]
        lines = [",".join(header)]
        for s in self.classroom.all_students():
            row = [s.student_id, s.name, round(s.average, 2), ";".join(s.scores)]
            lines.append(",".join(row))
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))


def print_report(gradebook: GradeBook, label: str) -> None:
    print(f"=== {gradebook.classroom.course_code} Grade Report: {label} ===")
    for s in gradebook.classroom.all_students():
        print(f"{s.student_id}\t{s.name}\tavg={s.average:.2f}\tscores={s.scores}")
    print(f"Class average: {gradebook.class_average():.2f}")
    top = gradebook.top_students(2)
    print("Top 2 students:", ", ".join([f"{s.name} ({s.average:.2f})" for s in top]))
    print()


def main()
    classroom = Classroom("CS101")
    students_data = [
        ("s001", "Ada"),
        ("s002", "Linus"),
        ("s003", "Grace"),
        ("s004", "Ken"),
    ]
    for sid, nm in student_data:
        classroom.add_student(Student(sid, nm))

    gradebook = GradeBook(classroom)

    midterm_scores = {
        "s001": [88],
        "s002": [100],
        "s003": [73, 85],
        "s004": [60],
    }
    for sid, scores in midterm_scores.items():
        for sc in scores:
            gradebook.record_score(sid, sc)

    print_report(gradebook, "Midterm")

    final_scores = {
        "s001": [94, 76],
        "s002": [92],
        "s003": [91, 89],
        "s004": [70],
    }
    for sid, scores in final_scores.items():
        for sc in scores:
            gradebook.record_score(sid, sc)

    print_report(gradebook, "Final")
    gradebook.export_csv("classroom_report.csv")
    print("Exported report to classroom_report.csv")


if __name__ == "__main__":
    main()
