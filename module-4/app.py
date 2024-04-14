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
            communication_steps.append(text)
        elif element_type == "UMLClass":
            text = element.find('panel_attributes').text
            textSplit = text.split('--')
            entities.append(textSplit[0].strip())

    return stakeholders, communication_paths, communication_steps, use_case_name, entities

def getNameFromUMLArrow(arrow):

    switcher = {
        "lt=<<<<-": "aggregates",
        "lt=<<-": "generalizes",
        "lt=<-": "includes",
    }
    
    return switcher.get(arrow, "undefined")  # Default case if argument not found

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
        
        for i in range(len(entities)-1):
            entity = entities[i]
            try:
                entityNext = entities[i+1]
            except IndexError:
                entityNext = "end"
            try:
                arrowName = getNameFromUMLArrow(communication_steps[i])
            except IndexError:
                arrowName = "end"
            if(i < len(entities)-4):
                print(f'{entityNext} {arrowName} {entity}')
            elif(i < len(entities)-5):
                print(f'{entity} {arrowName} {entityNext}')
            else:
                print(f'trait includes {entityNext}')
