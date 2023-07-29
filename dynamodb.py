import boto3

aws_session = boto3.Session(
    region_name = 'eu-west-3',
    aws_access_key_id='AKIA5MPJEYM3D7JA2ZMH',
    aws_secret_access_key='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'
)


dynamodb_client = boto3.client("dynamodb")

table_name = 'UsersTable'

response = dynamodb_client.put_item(
    TableName = table_name,
    Item = {
        'nickname':{"S":'nickname'},
        'email':{"S":'email'},
        'password':{"S":'hashed_password'},
    },
)
print(response)
