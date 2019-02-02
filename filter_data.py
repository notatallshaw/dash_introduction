# Standard Library
import os
import csv
from datetime import datetime

# Third Party Libraries
import pandas as pd


# Originally got data from: https://nycopendata.socrata.com/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9
# Export > CSV
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(CURRENT_DIRECTORY, '311_Service_Requests_from_2010_to_Present.csv')
FIELDS = ['Created Date',
          'Agency Name',
          'Complaint Type',
          'Descriptor',
          'Location Type',
          'Incident Zip',
          'Latitude',
          'Longitude']


def typifier(value, fieldname):
    if not value:
        return None
    if 'Date' in fieldname:
        return datetime.strptime(value, '%m/%d/%Y %H:%M:%S %p')
    elif fieldname in ('Latitude', 'Longitude'):
        return float(value)
    return value


def gen_2017_records(file_path):
    with open(file_path, 'r', encoding='ascii', errors='ignore') as f:
        reader = csv.DictReader(f)
        for record in reader:
            if '/2017 ' not in record['Created Date']:
                continue
            yield dict((f, typifier(record[f], f)) for f in FIELDS)


def main():
    three_one_one_df = pd.DataFrame.from_records(gen_2017_records(CSV_FILE_PATH))
    three_one_one_df.dropna(inplace=True)
    three_one_one_df.to_msgpack('311_2017.msgpack')


if __name__ == '__main__':
    main()
