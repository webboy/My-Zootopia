import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animal_info(animals_data):
    """Generates a string with animal information"""
    info_list = []
    for animal in animals_data:
        info = []
        if 'name' in animal:
            info.append(f"Name: {animal['name']}")

        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            info.append(f"Diet: {animal['characteristics']['diet']}")

        if 'locations' in animal and len(animal['locations']) > 0:
            info.append(f"Location: {animal['locations'][0]}")

        if 'characteristics' in animal and 'type' in animal['characteristics']:
            info.append(f"Type: {animal['characteristics']['type']}")

        if info:
            info_list.append("\n".join(info))

    return "\n\n".join(info_list)


def generate_html(template_path, output_path, animals_info):
    """Generates an HTML file by replacing a placeholder in the template"""
    with open(template_path, "r") as template_file:
        template_content = template_file.read()

    html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open(output_path, "w") as output_file:
        output_file.write(html_content)


# Main execution
animals_data = load_data('animals_data.json')
animals_info = generate_animal_info(animals_data)
generate_html('animals_template.html', 'animals.html', animals_info)
