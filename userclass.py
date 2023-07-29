import nvalid, pvalid, emailvalidator, valogin, boto3, hashlib
aws_session = boto3.Session(
    region_name = 'eu-west-3',
    aws_access_key_id='AKIA5MPJEYM3D7JA2ZMH',
    aws_secret_access_key='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'
)


dynamodb_client = aws_session.client("dynamodb")

table_name = 'UsersTable'



class User:
    SECRET_KEY = "secretpd"


    def __init__(self,nickname,password):
        self._nickname = nickname
        self._password = password

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self,value):
        self._nickname = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,value):
        self._password = value

    def action(self):
        while True:
            print("What do you want to do?")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            do = input("Enter the number of your choice.")


            if do == "1":
                self.register()
            elif do == "2":
                self.login()
            elif do == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.Try again.")


    def register(self):
        nickname = nvalid.new_nickname()
        email = emailvalidator.test_email()
        password = pvalid.test_password()
        print(password)
        hashed_password = hashlib.sha256((password + self.SECRET_KEY).encode()).hexdigest()

        response = dynamodb_client.put_item(
            TableName = table_name,
            Item = {'nickname': {'S' : nickname}, 'email':{'S':email}, 'password': {'S': hashed_password}}
        )


        print("You are registered successfully!")



    def login(self):
        nickname = input("Enter your nickname: ")
        password = input("Enter your password: ")

        result = valogin.test_data(nickname,password)

        if result:
            print("Logged in successfuly!")
            print(password)
        else:
            print("Invalid nickname or password")




user = User("","")
user.action()
