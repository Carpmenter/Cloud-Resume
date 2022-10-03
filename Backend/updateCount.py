import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    
    countTable = dynamodb.Table('website-counter')
    countId = event['countId']
    eventDateTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    try:
        countTable.put_item(
                Item={
                    'countID' : countId,
                    'datetime' : eventDateTime
                }
            )
        return {
        'statusCode': 200,
        'body': json.dumps('Succesfully inserted count!')
        }
    except:
        print('Closing lambda function')
        return {
                'statusCode': 400,
                'body': json.dumps('Error saving the count')
        }