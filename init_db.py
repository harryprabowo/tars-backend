from app import db
from models.dtc import DTC
from models.history import History
import os
import csv
from datetime import datetime

def init_db():
    db.drop_all()
    db.create_all()
    dtc_db()
    history_db()
    db.session.commit()

def dtc_db():
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

def history_db():
    with open('histories.csv', mode='r') as his_file:
        hist_reader = csv.reader(his_file)
        line_count = 0
        for row in hist_reader:
            if line_count == 0:
                line_count += 1
            else:
                his = History(
                    car_id=row[0],
                    lat=row[1],
                    long=row[2],
                    fuel_level=row[3],
                    dtc=row[4],
                    timestamp=datetime.strptime(row[5], '%d-%m-%y  %H:%M:%S'),
                    engine_temp=row[6],
                    oil_temp=row[7],
                    odometer=row[8]
                )
                db.session.add(his)