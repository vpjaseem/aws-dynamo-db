import boto3
region = 'ap-south-1'

TableName = "aws_dynamodb_table1"
Primary_Column_Name = 'name'
columns=["name","gender", "mail", "phone"]

db = boto3.resource('dynamodb', region_name=region)
table = db.Table(TableName)

Primary_Key = 'Abdul Jaseem'
response = table.delete_item(
    Key={
        Primary_Column_Name: Primary_Key
        }
    )

status = response["ResponseMetadata"]["HTTPStatusCode"]
print("Status code", status)
print("Successfully deleted value from DynamoDB")



