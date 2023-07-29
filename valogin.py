import hashlib, boto3
aws_session = boto3.Session(
    region_name = 'eu-west-3',
    aws_access_key_id='AKIA5MPJEYM3D7JA2ZMH',
    aws_secret_access_key='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'
)


dynamodb_client = aws_session.client("dynamodb")

table_name = 'UsersTable'


SECRET_KEY = "secretpd"

def validator(func):
    def wrapper(nickname,password):
        hashed_password = hashlib.sha256((password + SECRET_KEY).encode()).hexdigest()

        response = dynamodb_client.get_item(
            TableName = table_name,
            Key = {'nickname': {'S' : nickname}}
        )
        item = response.get('Item')
        print(item)

        if item:
            return func(nickname,password)
        else:
            return False

    return wrapper

@validator
def test_data(nickname,password):
    return nickname, password
if __name__ == '__main__':
    test_data()
