import csv

report = [

  {
    'first_name': 'Bill',
    'last_name': 'Lumbergh',
    'job_title': 'Vice President',
    'hire_date': '1985',
    'performance_review': 'excellent'
  },
  {
    'first_name': 'Michael',
    'last_name': 'Bolton',
    'job_title': 'Programmer',
    'hire_date': '1995',
    'performance_review': 'poor'
  },
  {
    'first_name': 'Peter',
    'last_name': 'Gibbons',
    'job_title': 'Programmer',
    'hire_date': '1989',
    'performance_review': 'poor'
  },
  {
    'first_name': 'Samir',
    'last_name': 'Nagheenanajar',
    'job_title': 'Programmer',
    'hire_date': '1974',
    'performance_review': 'fair'
  },
  {
    'first_name': 'Milton',
    'last_name': 'Waddams',
    'job_title': 'Collator',
    'hire_date': '1974',
    'performance_review': 'Does he even work here?'
  },
  {
    'first_name': 'Bob',
    'last_name': 'Porter',
    'job_title': 'Consultant',
    'hire_date': '1999',
    'performance_review': 'excellent'
  },
  {
    'first_name': 'Bob',
    'last_name': 'Slydell',
    'job_title': 'Consultant',
    'hire_date': '1999',
    'performance_review': 'excellent'
  }

]

for person in report:
    person['finished_review'] = 'yes'
    if person['job_title'] == 'Consultant' or person['first_name'] == 'Bill':
        person['performance_review'] = 'poor'



keys = report[0].keys()

with open('tps_report.csv', 'w', newline='') as csvfile:
  writer = csv.DictWriter(csvfile, keys)
  writer.writeheader()
  writer.writerows(report)