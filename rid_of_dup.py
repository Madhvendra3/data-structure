student_data = {"id1":{"name": "bob","class":"6","subjectintegrate":"English,science,math"},
"id2": {"name":"Madhav","class":"10","subjectintegrate":"English,science,math"},}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["name"],details["class"],details["subjectintegrate"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
     print(k,":", v)        