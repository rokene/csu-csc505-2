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
    use_cases = []

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
        elif element_type == "UMLUseCase":
            text = element.find('panel_attributes').text
            use_cases.append(text.strip())

    return stakeholders, communication_paths, communication_steps, use_case_name, entities, use_cases

def get_name_from_uml_arrow(arrow):

    switcher = {
        "lt=<<<<-": "aggregates",
        "lt=<<-": "generalizes",
        "lt=<-": "includes",
    }
    
    return switcher.get(arrow, "undefined")  # Default case if argument not found

def print_1d_list(item_type_name, items):
    print(f"Number of {item_type_name}: {len(items)}")
    for item in items:
        print(item)
    print()

def print_use_cases(use_cases):
    print(f"Number of Use Cases: {len(use_cases)}")
    for use_case in use_cases:
        print(f"{use_case} - {print_usecase_description(use_case)}")
    print()

def print_usecase_description(use_case):
    switcher = {
        "Login": "The case where we authenticate a user.",
        "Report Potholes": "The case where a user reports potholes.",
        "Main Menu": "The case where the user views the main menu/landing page that aggregates information and functions.",
        "Create Account": "The case where a new user creates an account in the system.",
        "Manage Account": "The case where an existing user manages its account.",
        "Admin Menu": "The case where an admin user views the admin menu that aggregates admin information and functions.",
        "Admin Accounts": "The case where an admin user administers user accounts on the system.",
        "Manage Work Orders": "The case where users can manage work orders.",
        "View Damage Files": "The case where admin users view 'damage files/logs'",
    }
    
    return switcher.get(use_case, "undefined")  # Default case if argument not found

def get_description():
    return """
        The PHTRS System enables citizens to report potholes in the city and city maintainers to track and manage repairs.
    """

if __name__ == "__main__":
    for diagram_file in get_diagram_file_list():
        stakeholders, communication_paths, communication_steps, use_case_name, entities, use_cases = analyze_diagram(diagram_file)
        print(f"###### Use Case: {use_case_name}")
        print(f"Description: {get_description()}")
        print()

        print_1d_list("Actors", stakeholders)
        print_1d_list("Entities", entities)
        print_use_cases(use_cases)
        
