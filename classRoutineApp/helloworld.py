from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors
from classRoutineApp.models import ClassRoutine
from syllabusApp.models import Course

width, height = A4
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
styleN.alignment = TA_LEFT
styleBH = styles["Normal"]
styleBH.alignment = TA_CENTER

results = []
courseList = Course.objects.all()
for a in courseList:
    if a.course_code[4] == "1":
        results.append(a.id)
fullRoutine = ClassRoutine.objects.filter(course_Id_Fk__in=results)

for foo in fullRoutine:
    if foo.classTime_Id_Fk_id == 1 and foo.dayOfWeek == 'Sat':
        sat1var = foo.course_Id_Fk - foo.assignedTeacher_Fk


def coord(x, y, unit=1):
    x, y = x * unit, height - y * unit
    return x, y


# Headers
day = Paragraph('''&nbsp''', styleBH)
nineToTen = Paragraph('''<b>9.00-10.20</b>''', styleBH)
tenToEleven = Paragraph('''<b>10.20-11.25</b>''', styleBH)
elevenTo12 = Paragraph('''<b>11.25-1.00</b>''', styleBH)
twelveTo13 = Paragraph('''<b>2.00-4.00</b>''', styleBH)

# Texts

satDay = Paragraph('Saturday', styleN)
sat1 = Paragraph(sat1var, styleN)
sat2 = Paragraph('', styleN)
sat3 = Paragraph('', styleN)
sat4 = Paragraph('', styleN)

# Texts
sunDay = Paragraph('Saturday', styleN)
sun1 = Paragraph('', styleN)
sun2 = Paragraph('', styleN)
sun3 = Paragraph('', styleN)
sun4 = Paragraph('', styleN)

data = [[day, nineToTen, tenToEleven, elevenTo12, twelveTo13],
        [satDay, sat1, sat2, sat3, sat4],
        [sunDay, sun1, sun2, sun3, sun4],
        [satDay, sat1, sat2, sat3, sat4],
        [sunDay, sun1, sun2, sun3, sun4],
        [satDay, sat1, sat2, sat3, sat4],
        [sunDay, sun1, sun2, sun3, sun4],
        [satDay, sat1, sat2, sat3, sat4]
        ]

table = Table(data, colWidths=[2.05 * cm, 2.7 * cm, 5 * cm,
                               3 * cm, 3 * cm])

table.setStyle(TableStyle([
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
]))

c = canvas.Canvas("a.pdf", pagesize=A4)
table.wrapOn(c, width, height)
table.drawOn(c, *coord(1.8, 9.6, cm))
c.save()
