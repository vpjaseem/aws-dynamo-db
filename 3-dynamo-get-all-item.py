import boto3
from boto3.dynamodb.conditions import Key, Attr
region = 'ap-south-1'

TableName = "aws_dynamodb_table1"
Primary_Column_Name = 'name'
columns=["name","gender", "mail", "phone"]

db = boto3.resource('dynamodb', region_name=region)
table = db.Table(TableName)

response = table.scan(
    FilterExpression=Attr('name').gte('')
    )
for x in response["Items"]:
    print(x)

status = response["ResponseMetadata"]["HTTPStatusCode"]
print("Status code", status)
print("Successfully retrieved all data from DynamoDB")




