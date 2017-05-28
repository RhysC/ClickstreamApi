#/bin/sh
set -e
echo "Deploying Clickstream stack"

# Create Template
python create_cloudformation_template.py

# deploy the newly created CF template
TEMPLATE_NAME='Clickstream.cf.yaml'
STACK_NAME="clickstream-api-kinesis-cfs"
echo "StackName: $STACK_NAME"
aws cloudformation create-stack \
    --stack-name $STACK_NAME \
    --template-body file://$TEMPLATE_NAME \
    --capabilities CAPABILITY_NAMED_IAM \
    --profile rhysc \
    --region eu-west-1 \
    --tags Key=Owner,Value=RhysC Key=Env,Value=Test

aws cloudformation wait stack-create-complete \
    --stack-name $STACK_NAME \
    --profile rhysc \
    --region eu-west-1

echo "ClickStreamApiGatewayEndpoint:"
aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --profile rhysc \
    --region eu-west-1 \
    --query 'Stacks[0].Outputs[?OutputKey==`ClickStreamApiGatewayEndpoint`].OutputValue'

echo "Complete"
