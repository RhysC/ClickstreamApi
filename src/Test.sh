ECHO "Getting URL"
api_url=$(aws cloudformation describe-stacks \
    --stack-name clickstream-api-kinesis-cfs \
    --profile rhysc \
    --region eu-west-1 \
    --query 'Stacks[0].Outputs[?OutputKey==`ClickStreamApiGatewayEndpoint`].OutputValue' --output text)

ECHO "Calling rest endpoint"
curl -X POST -d @TestEvent.json --header "Content-Type:application/json" $api_url/event
