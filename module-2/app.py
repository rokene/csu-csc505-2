#!/usr/bin/env python3

import argparse
import xml.etree.ElementTree as ET

def analyze_diagram(file_path):
    print(f'filepath: {file_path}')
    with open(file_path, 'r') as file:
        xml_content = file.read()

    root = ET.fromstring(xml_content)
    stakeholders = set()
    communication_paths = 0

    for element in root.findall('element'):
        element_type = element.find('id').text
        if element_type in ['UMLActor']:
            stakeholders.add(element.find('panel_attributes').text)
        elif element_type == 'Relation':
            communication_paths += 1

    return stakeholders, communication_paths

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze a UML diagram for stakeholders and communication pathways.')
    parser.add_argument('file_path', type=str, help='Path to the UML diagram file (in XML format).')
    args = parser.parse_args()

    stakeholders, communication_paths = analyze_diagram(args.file_path)
    print(f"Stakeholders: {', '.join(stakeholders)}")
    print(f"Number of communication pathways: {communication_paths}")
