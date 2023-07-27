import boto3

aws_session = boto3.Session(
    region_name = 'eu-west-3',
    aws_access_key_id='AKIA5MPJEYM3EF3DRD42',
    aws_secret_access_key='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'
)


dynamodb_client = boto3.client("dynamodb")

table_name = 'UsersTable'

response = dynamodb_client.put_item(
    TableName = table_name,
    Item = {
        'nickname':{"S":'nickname'},
        'password':{"S":'hashed_password'},
    },
)
print(response)
