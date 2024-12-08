import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animal_info(animals_data):
    """Generates a string with animal information in HTML"""
    output = ""
    for animal in animals_data:
        output += '<li class="cards__item">'
        if 'name' in animal:
            output += f'  <div class="card__title">{animal["name"]}</div>\n'

        output += '  <p class="card__text">\n'
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f'      <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

        if 'locations' in animal and len(animal['locations']) > 0:
            output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f'      <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

        output += '  </p>\n'
        output += '</li>'

    return output


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
