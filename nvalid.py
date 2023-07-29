import boto3
from boto3.dynamodb.conditions import Key
aws_session = boto3.Session(
    region_name = 'eu-west-3',
    aws_access_key_id='AKIA5MPJEYM3D7JA2ZMH',
    aws_secret_access_key='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'
)


dynamodb_client = aws_session.client("dynamodb")

table_name = 'UsersTable'

def validator(func):
    def wrapper(nickname=None):
        if nickname is None:
            nickname = input("Type your nickname?")

        response = dynamodb_client.get_item(
            TableName = table_name,
            Key = {'nickname': {'S': str(nickname)}}
        )
        item = response.get('Item')
        print(item)

        if not item:
            return func(nickname)
        else:
            print(f"Nickname {nickname} already exists,chose another")
            return wrapper()

        return func(nickname)
    return wrapper

@validator
def new_nickname(nickname):
    print("Nickname is valid:")
    return nickname

if __name__ == '__main__':
    new_nickname()
