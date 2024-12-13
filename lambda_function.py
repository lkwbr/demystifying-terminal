def lambda_handler(event, context):
    """
    AWS Lambda function that calculates the square of a given number.
    Input: JSON object with a 'number' key.
    Output: JSON object with the squared value.
    """
    try:
        number = event.get("number", None)
        if number is None:
            raise ValueError("Missing 'number' in input.")

        squared = number ** 2
        return {
            "statusCode": 200,
            "body": {"number": number, "squared": squared}
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "error": str(e)
        }