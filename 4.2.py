employees = {
    "Alice": {"department": "HR", "age": 30},
    "Bob": {"department": "IT", "age": 25},
    "Charlie": {"department": "IT", "age": 28},
    "Diana": {"department": "Finance", "age": 35},
}

def specific_department(employees):
    em=[]
    for name,details in employees.items():
        if details['department']=='IT':
            em.append(name)
    return em

print(specific_department(employees))

