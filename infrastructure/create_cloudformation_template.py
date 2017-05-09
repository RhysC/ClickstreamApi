import jinja2
import os
import string

script_dir = os.path.dirname(os.path.realpath(__file__))
params = {}
with open(script_dir + '/swagger.yaml.j2') as swagger_j2File:
    swagger_template = jinja2.Template(swagger_j2File.read())
    swagger_def = swagger_template.render(params=params)
    # Convert the pretty swagger file to a nested yaml node in the CF template.
    # To do this we need to appropriately indent
    swagger_def = string.replace(swagger_def, "\n", "\n        ")
    params["swagger_def"] = swagger_def

with open(script_dir + '/Clickstream.cf.yaml.j2') as cf_j2File:
    cf_template = jinja2.Template(cf_j2File.read())
    result = cf_template.render(params=params)

    with open(script_dir + '/Clickstream.cf.yaml', 'w') as yamlFile:
        yamlFile.write(result)
