import boto3
import requests

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")