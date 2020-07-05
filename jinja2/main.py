"""
Jinja2 Example
"""
from os.path import join, dirname
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape

# create essential path variables
working_directory = dirname(__file__)
templates_path = join(working_directory, "templates")
data_path = join(working_directory, "data/test-data.json")
meta_path = join(working_directory, "data/meta-data.json")

# load test-data from json file
with open(data_path, "r") as json_file:
    test_data = json.load(json_file)

# load meta-data from json file
with open(meta_path, "r") as json_file:
    meta_data = json.load(json_file)

# add more meta-data
test_data.update(meta_data)

# create the environment
env = Environment(
    loader=FileSystemLoader(templates_path),
    autoescape=select_autoescape(["html", "xml"]),
)

# get the template
template = env.get_template("page.html")

# render the template and pass in data
# get the output
output = template.render(test_data)

# write output to file
output_file = join(working_directory, "output/output.html")
with open(output_file, "w") as writer:
    writer.write(output)
