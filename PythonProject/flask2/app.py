from flask import Flask, render_template, request, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        # Получаем данные из формы
        name = request.form.get("name")
        q1 = request.form.get("q1")
        q2 = request.form.getlist("q2")  # Для чекбоксов

        # Генерируем PDF в памяти
        pdf_buffer = generate_pdf(name, q1, q2)
        return send_file(pdf_buffer, as_attachment=True, download_name="survey_results.pdf", mimetype="application/pdf")

    return render_template("survey.html")

def generate_pdf(name, q1, q2):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    # Регистрация шрифта с поддержкой кириллицы
    pdfmetrics.registerFont(TTFont('DejaVuSans', 'C:/Users/Student/PycharmProjects/PythonProject/.venv/Lib/site-packages/reportlab/fonts/DejaVuSans.ttf'))
    pdf.setFont("DejaVuSans", 12)

    pdf.drawString(100, 750, "Опросник - Результаты")
    pdf.drawString(100, 730, f"Имя: {name}")
    pdf.drawString(100, 710, f"Вопрос 1: {q1}")
    pdf.drawString(100, 690, f"Вопрос 2: {', '.join(q2) if q2 else 'Не выбрано'}")

    pdf.save()
    buffer.seek(0)
    return buffer

if __name__ == "__main__":
    app.run(debug=True)