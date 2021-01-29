import boto3
region = 'ap-south-1'

TableName = "aws_dynamodb_table1"
Primary_Column_Name = 'name'
columns=["name","gender", "mail", "phone"]

db = boto3.resource('dynamodb', region_name=region)
table = db.Table(TableName)

response = table.put_item(
Item={
    columns[0]: "Abdul Jaseem",
    columns[1] :"M",
    columns[2]: "vpjaseem@gmail.com",
    columns[3]: "+919495860708"
    }
)

status = response["ResponseMetadata"]["HTTPStatusCode"]
print("Status code", status)
print("Successfully updated DynamoDB Table")
