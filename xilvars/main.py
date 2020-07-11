"""
Jinja2 Example
"""
from os.path import join, dirname
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape

working_directory = dirname(__file__)

env = Environment(
    loader=FileSystemLoader(working_directory),
    autoescape=select_autoescape(["html", "xml"]),
)

dataraw = {
    "data": [
        "Pdu_Name/Signal_Name/Feature/Port/PortType",
        "Pdu_Name/Signal_Name/Feature/Port/PortType",
        "Pdu_Name/Signal_Name/Feature/Port/PortType",
        "Pdu_Name/Signal_Name/Feature/Port/PortType",
        "Pdu_Name/Signal_Name/Feature/Port/PortType",
    ]
}

data = [d.split("/") for d in dataraw["data"]]

template = env.get_template("page.html")
output = template.render({"data":data})

output_file = join(working_directory, "output.html")
with open(output_file, "w") as writer:
    writer.write(output)
