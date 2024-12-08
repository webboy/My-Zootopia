import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_available_skin_types(animals_data):
    """Extracts a list of unique skin types from the animals data"""
    skin_types = set()
    for animal in animals_data:
        if 'characteristics' in animal and 'skin_type' in animal['characteristics']:
            skin_types.add(animal['characteristics']['skin_type'])
    return sorted(skin_types)


def filter_animals_by_skin_type(animals_data, selected_skin_type):
    """Filters animals by the selected skin type"""
    return [animal for animal in animals_data if
            'characteristics' in animal and animal['characteristics'].get('skin_type') == selected_skin_type]


def generate_animal_info(animals_data):
    """Generates a string with animal information in HTML"""
    output = ""
    for animal in animals_data:
        output += '<li class="cards__item">'
        if 'name' in animal:
            output += f'  <div class="card__title">{animal["name"]}</div>\n'

        output += '  <p class="card__text">\n'
        output += '    <ul class="card__list">\n'
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f'      <li class="card__list-item">Diet: {animal["characteristics"]["diet"]}</li>\n'

        if 'locations' in animal and len(animal['locations']) > 0:
            output += f'      <li class="card__list-item">Location: {animal["locations"][0]}</li>\n'

        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f'      <li class="card__list-item">Type: {animal["characteristics"]["type"]}</li>\n'

        if 'characteristics' in animal and 'lifespan' in animal['characteristics']:
            output += f'      <li class="card__list-item">Lifespan: {animal["characteristics"]["lifespan"]}</li>\n'

        if 'characteristics' in animal and 'color' in animal['characteristics']:
            output += f'      <li class="card__list-item">Color: {animal["characteristics"]["color"]}</li>\n'

        if 'characteristics' in animal and 'distinctive_feature' in animal['characteristics']:
            output += f'      <li class="card__list-item">Distinctive Feature: {animal["characteristics"]["distinctive_feature"]}</li>\n'

        output += '    </ul>\n'
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

# Get available skin types
skin_types = get_available_skin_types(animals_data)
print("Available skin types:")
for skin_type in skin_types:
    print(f"- {skin_type}")

# Prompt user for a skin type
selected_skin_type = input("Enter a skin type from the list above: ")

# Filter animals by the selected skin type
filtered_animals = filter_animals_by_skin_type(animals_data, selected_skin_type)

if not filtered_animals:
    print(f"No animals found with skin type '{selected_skin_type}'. Generating an empty website.")

# Generate HTML with filtered animals
generate_html('animals_template.html', 'animals.html', generate_animal_info(filtered_animals))
print("Website generated: animals.html")
