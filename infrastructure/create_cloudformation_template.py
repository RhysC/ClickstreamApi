import jinja2
import os
import string

script_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(script_dir, '../src')
params = {}
with open(script_dir + '/swagger.yaml.j2') as swagger_j2File:
    swagger_template = jinja2.Template(swagger_j2File.read())
    swagger_def = swagger_template.render(params=params)
    # Convert the pretty swagger file to a nested yaml node in the CF template.
    # To do this we need to appropriately indent
    swagger_def = string.replace(swagger_def, "\n", "\n        ")
    params["swagger_def"] = swagger_def

with open(src_dir + '/index.js') as lambda_file:
    # change to read each line and warp in double quotes as per:
    # https://forrestbrazeal.com/2016/06/06/aws-lambda-cookbook/#highlighter_861602
    lines = []
    for line in lambda_file.readlines():
        if line.strip() != "":
            line = string.replace(line, "\n", "")
            lines.append("              - \"{}\"".format(line))
    lambda_code = string.join(lines, "\n")
    params["lambda_code"] = lambda_code

with open(script_dir + '/Clickstream.cf.yaml.j2') as cf_j2File:
    cf_template = jinja2.Template(cf_j2File.read())
    result = cf_template.render(params=params)

    with open(script_dir + '/Clickstream.cf.yaml', 'w') as yamlFile:
        yamlFile.write(result)
