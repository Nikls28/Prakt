from flask import Flask, render_template, request

app = Flask(__name__)

def load_students(file_path):
    """Загружает студентов из файла и возвращает список словарей."""
    students = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:  # пропустить пустые строки
                    # Ожидается, что строка имеет формат "id,имя"
                    parts = line.split(",", 1)
                    if len(parts) == 2:
                        student_id, name = parts
                        # Приводим id к целому числу, если это возможно
                        try:
                            student_id = int(student_id.strip())
                        except ValueError:
                            continue  # если id не число, пропускаем
                        students.append({"id": student_id, "name": name.strip()})
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    return students

# Загружаем студентов из файла students.txt
students = load_students("students.txt")

@app.route("/search")
def search():
    query = request.args.get("query", "").strip()
    highlighted_student = None

    if query:
        # Если запрос состоит из цифр, ищем по id
        if query.isdigit():
            for student in students:
                if str(student["id"]) == query:
                    highlighted_student = student
                    break
        else:
            # Ищем по имени (без учёта регистра)
            for student in students:
                if query.lower() in student["name"].lower():
                    highlighted_student = student
                    break

    return render_template("search.html",
                           students=students,
                           highlighted_student=highlighted_student,
                           query=query)

if __name__ == "__main__":
    app.run(debug=True)