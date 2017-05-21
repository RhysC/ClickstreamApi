#/bin/sh
set -e
echo "Deleting Clickstream stack"


# deploy the newly created CF template
STACK_NAME="clickstream-api-kinesis-cfs"
echo "StackName: $STACK_NAME"
aws cloudformation delete-stack \
    --stack-name $STACK_NAME \
    --profile rhysc \
    --region eu-west-1

aws cloudformation wait stack-delete-complete \
    --stack-name $STACK_NAME \
    --profile rhysc \
    --region eu-west-1
echo "Delete complete"
