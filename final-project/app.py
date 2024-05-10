#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import os

def get_diagram_file_list():
    # List all files in the current directory
    all_files = os.listdir('.')

    # Filter the list to include only files that end with ".uxf"
    uxf_files = [file for file in all_files if file.endswith('.uxf')]

    return uxf_files


def analyze_diagram_1(diagram_filepath):
    with open(diagram_filepath, 'r') as file:
        xml_content = file.read()

    use_case_name = diagram_filepath.split('.', 1)[0]
    root = ET.fromstring(xml_content)
    stakeholders = set()
    communication_paths = 0
    communication_steps = []
    entities = []
    use_cases = []
    i=1
    for element in root.findall('element'):
        element_type = element.find('id').text
        
        if element_type in ['UMLActor']:
            continue
        elif element_type == 'Relation':
            continue
        elif element_type == "UMLState":
            text = element.find('panel_attributes').text
        elif element_type == "UMLSpecialState":
            text = element.find('panel_attributes').text
            if text == "type=initial":
                text = "start"
            elif text == "type=final":
                text = "end"
            else:
                text = text.split("decision")[-1]
        elif element_type == "UMLUseCase":
            continue
        entities.append(text.strip())
        i = i + 1
        
    entities.append("end")
    entities.insert(7, entities[12])
    del entities[9:]
    return stakeholders, communication_paths, communication_steps, use_case_name, entities, use_cases

def analyze_diagram_2(diagram_filepath):
    with open(diagram_filepath, 'r') as file:
        xml_content = file.read()

    use_case_name = diagram_filepath.split('.', 1)[0]
    root = ET.fromstring(xml_content)
    stakeholders = set()
    communication_paths = 0
    communication_steps = []
    entities = []
    use_cases = []
    i=1
    for element in root.findall('element'):
        element_type = element.find('id').text
        
        if element_type in ['UMLActor']:
            continue
        elif element_type == 'Relation':
            continue
        elif element_type == "UMLState":
            text = element.find('panel_attributes').text
        elif element_type == "UMLSpecialState":
            text = element.find('panel_attributes').text
            if text == "type=initial":
                text = "start"
            elif text == "type=final":
                continue
            else:
                text = text.split("decision")[-1]
        elif element_type == "UMLUseCase":
            continue
        entities.append(text.strip())
        i = i + 1
        
    entities.append("end")
    del entities[4:7]
    entities.pop(6)
    return stakeholders, communication_paths, communication_steps, use_case_name, entities, use_cases


def analyze_diagram_3(diagram_filepath):
    with open(diagram_filepath, 'r') as file:
        xml_content = file.read()

    use_case_name = diagram_filepath.split('.', 1)[0]
    root = ET.fromstring(xml_content)
    stakeholders = set()
    communication_paths = 0
    communication_steps = []
    entities = []
    use_cases = []
    i=1
    for element in root.findall('element'):
        element_type = element.find('id').text
        
        if element_type in ['UMLActor']:
            continue
        elif element_type == 'Relation':
            continue
        elif element_type == "UMLState":
            text = element.find('panel_attributes').text
        elif element_type == "UMLSpecialState":
            text = element.find('panel_attributes').text
            if text == "type=initial":
                text = "start"
            elif text == "type=final":
                continue
            else:
                text = text.split("decision")[-1]
        elif element_type == "UMLUseCase":
            continue
        entities.append(text.strip())
        i = i + 1
        
    entities.append("end")
    del entities[4:7]
    entities.pop(7)
    return stakeholders, communication_paths, communication_steps, use_case_name, entities, use_cases


def print_1d_list(item_type_name, items):
    print(f"######## {item_type_name} number steps: {len(items)}")
    i=1
    for item in items:
        print()
        print(i)
        print(item)
        i = 1+i
    print()

if __name__ == "__main__":
    for diagram_file in get_diagram_file_list():
        print(f"analyzing: {diagram_file}")

        stakeholders, communication_paths, communication_steps, use_case_name, entities, use_cases = analyze_diagram_1(diagram_file)
        print()
        print("######## Path 1 Description: Entering the wrong pin and exeeding the allowed failed attempts.")
        print_1d_list("Path 1", entities)

        stakeholders, communication_paths, communication_steps, use_case_name, entities, use_cases = analyze_diagram_2(diagram_file)
        print()
        print("######## Path 2 Description: Entering the correct pin and has a balance on the account.")
        print_1d_list("Path 2", entities)

        stakeholders, communication_paths, communication_steps, use_case_name, entities, use_cases = analyze_diagram_3(diagram_file)
        print()
        print("######## Path 3 Description: Entering the correct pin and has a zero balance on the account.")
        print_1d_list("Path 3", entities)
