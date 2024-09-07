import csv
import os

def pnt_to_csv(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w', newline='') as f_out:
        csv_writer = csv.writer(f_out)
        
        header = ['Latitude', 'Longitude']
        num_months = len(next(f_in).split()) - 2
        header.extend([f'Month_{i+1}' for i in range(num_months)])
        csv_writer.writerow(header)
        
        # Reset file pointer
        f_in.seek(0)
        
        # Convert data
        for line in f_in:
            data = line.split()
            csv_writer.writerow(data)

input_file = input('input filepath/filename:')
output_file = input('output filepath/filename:')
pnt_to_csv(input_file, output_file)