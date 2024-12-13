#!/bin/bash
# Script to invoke the AWS Lambda function and test it.

# Input number for testing
TEST_NUMBER=5

# Invoke the Lambda function using AWS CLI
RESPONSE=$(aws lambda invoke \
    --function-name calculateSquare \
    --payload "{\"number\": $TEST_NUMBER}" \
    output.json && cat output.json)

# Display response
echo "Response from Lambda:"
echo "$RESPONSE"

# Clean up
rm -f output.json