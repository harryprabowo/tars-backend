from app import db
from models.dtc import DTC
import os
import csv

db.drop_all()
db.create_all()

with open('dtc.csv', mode='r') as dtc_file:
    csv_reader = csv.reader(dtc_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            dtc = DTC(
                dtc_number=row[0],
                dtc_name=row[1],
                desc=row[2],
                system=row[3],
                severity=row[4],
                urgency=row[5]
            )
            db.session.add(dtc)

db.session.commit()
