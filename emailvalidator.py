import re
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
    def wrapper(email=None):
        if email is None:
            email = input("Type your email.")

        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',email):
            print("Invalid nickname format.Please use valid email.")
            return wrapper()



        return func(email)
    return wrapper

@validator
def test_email(email):
    print("Email is valid.")
    return email
if __name__ == '__main__':
    print(test_email())
