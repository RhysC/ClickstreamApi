# ClickstreamApi
AWS Api gateway with kinesis stream to accept click events of http SAMPLE


## Get Started:

Optionally create a python virtual environment (see http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) and load up the required dependencies
``
mkvirtualenv clickstreamapi
workon clickstreamapi
pip install -r requirements.txt
``

To create the stack in AWS just run
``
infrastructure/CreateStack.sh
``



## Assumptions
You are working in the eu-west-1 (Ireland) region. Kinesis Firehose is in a limited number of regions at time of writing this


## Notes
To generate the CloudFormation file without deploying, run:
``
python infrastructure/create_cloudformation_template.py
``

This CloudFormation script can be used to create the stack via the CLI or the AWS web console

## References
see docs
http://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-kinesis.html
