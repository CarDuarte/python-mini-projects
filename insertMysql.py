import csv
import mysql.connector
from datetime import datetime, date

# 🔧 Update with your MySQL credentials
config = {
    'host': 'x',
    'user': 'x',
    'password': 'x',
    'database': 'x'
}

# 📄 Path to your CSV file
csv_file_path = 'tts_dev.csv'

# Connect to MySQL
def parse_nullable(value: str):
    value = value.strip().lower()
    return None if value == 'null' or value == '' else value

def parse_time_field(value: str):
    try:
        return datetime.combine(date.today(), datetime.strptime(value.strip(), '%H:%M:%S').time())
    except Exception:
        return None

# Connect to MySQL
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

with open('tts_dev.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        try:
            studentid = row['studentid'].strip()
            firstname = parse_nullable(row['firstname'])
            lastname = parse_nullable(row['lastname'])
            username = parse_nullable(row['username'])
            email = parse_nullable(row['email'])
            campus = parse_nullable(row['campus'])
            program = parse_nullable(row['program'])
            randtoken = parse_nullable(row['randtoken'])
            emailsent = parse_nullable(row['emailsent'])
            comment = parse_nullable(row['comment'])
            phone = parse_nullable(row['phone'])
            new_student = parse_nullable(row['newStudent'])

            tech = int(row['techOnboardingCompleted']) if row['techOnboardingCompleted'].isdigit() else 0
            tts = int(row['ttsCompleted']) if row['ttsCompleted'].isdigit() else 0
            follow = int(row['followUpNeeded']) if row['followUpNeeded'].isdigit() else 0

            created = parse_time_field(row['created'])
            regcompleted = parse_time_field(row['regcompleted'])

            sql = """
            INSERT INTO tts_dev (
                studentid, firstname, lastname, username, email,
                techOnboardingCompleted, ttsCompleted, followUpNeeded,
                created, campus, program, randtoken, emailsent,
                regcompleted, phone, comment, newStudent
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                firstname = VALUES(firstname),
                lastname = VALUES(lastname),
                username = VALUES(username),
                email = VALUES(email),
                techOnboardingCompleted = VALUES(techOnboardingCompleted),
                ttsCompleted = VALUES(ttsCompleted),
                followUpNeeded = VALUES(followUpNeeded),
                created = VALUES(created),
                campus = VALUES(campus),
                program = VALUES(program),
                randtoken = VALUES(randtoken),
                emailsent = VALUES(emailsent),
                regcompleted = VALUES(regcompleted),
                phone = VALUES(phone),
                comment = VALUES(comment),
                newStudent = VALUES(newStudent)
            """

            values = (
                studentid, firstname, lastname, username, email,
                tech, tts, follow, created, campus, program,
                randtoken, emailsent, regcompleted, phone,
                comment, new_student
            )

            cursor.execute(sql, values)

        except Exception as e:
            print(f"❌ Failed to insert studentid={row.get('studentid', 'UNKNOWN')}: {e}")

conn.commit()
cursor.close()
conn.close()

print("✅ CSV import complete.")