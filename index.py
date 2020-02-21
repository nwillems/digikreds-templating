
import argparse
import sys
import csv
import os.path

from docxtpl import DocxTemplate

def read_data(input_file):
    dialect = csv.Sniffer().sniff(input_file.read(1024))
    input_file.seek(0)
    for row in csv.DictReader(input_file, dialect=dialect):
        yield row
    return

def render_document(template, filename, data):
    print(data)
    doc = DocxTemplate(template)
    context = data # Possibly do some sanitizing
    doc.render(context)
    doc.save(filename)

def main(args):
    # Read input data
    data = read_data(args.input)

    for entry in data:
        print("Rendering document for:", entry)
        # Read template file
        # Create resulting files
        output_path = os.path.join(args.target, entry['filename']) + '.docx'
        render_document(args.template, output_path, entry)
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input',  nargs='?', type=argparse.FileType('r', encoding='utf-8-sig'), default=sys.stdin)
    parser.add_argument('target',  nargs='?', default='./')
    parser.add_argument('--template')
    args = parser.parse_args()
    main(args)
