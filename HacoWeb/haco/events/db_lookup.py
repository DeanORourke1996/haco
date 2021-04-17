from django.db import connection

with connection.cursor() as c:
    c.execute(
        'SELECT *'
        'FROM events_event'

        , None
    )

    results = c.fetchall()

for line in results:
    print(line)

print(len(results))
