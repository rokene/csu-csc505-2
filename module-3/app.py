#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import os

def get_diagram_file_list():
    # List all files in the current directory
    all_files = os.listdir('.')

    # Filter the list to include only files that end with ".uxf"
    uxf_files = [file for file in all_files if file.endswith('.uxf')]

    return uxf_files

def analyze_diagram(diagram_filepath):
    with open(diagram_filepath, 'r') as file:
        xml_content = file.read()

    use_case_name = diagram_filepath.split('.', 1)[0]
    use_case_name = use_case_name.replace("use-case-", "")
    root = ET.fromstring(xml_content)
    stakeholders = set()
    communication_paths = 0
    communication_steps = []
    entities = []

    for element in root.findall('element'):
        element_type = element.find('id').text
        if element_type in ['UMLActor']:
            stakeholders.add(element.find('panel_attributes').text)
        elif element_type == 'Relation':
            communication_paths += 1
            text = element.find('panel_attributes').text
            text = text.replace("lt=->>", "")
            text = text.strip()
            communication_steps.append(text)
        elif element_type == "UMLClass":
            entities.append(element.find('panel_attributes').text)

    return stakeholders, communication_paths, communication_steps, use_case_name, entities

if __name__ == "__main__":
    for diagram_file in get_diagram_file_list():
        stakeholders, communication_paths, communication_steps, use_case_name, entities = analyze_diagram(diagram_file)
        print(f"###### Use Case: {use_case_name}")
        print()

        print(f"Stakeholders: {', '.join(stakeholders)}")
        print()

        print(f"Number of Entities: {len(entities)}")
        print("Entities:")
        for entity in entities:
            print(entity)
        print()

        print(f"Number of communication pathways: {communication_paths}")
        print("Communication Steps:")
        for step in communication_steps:
            print(step)
        print()
