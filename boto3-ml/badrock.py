import boto3 
import pprint
import json
question = 'What is the capital of Tajikistan'
body = json.dumps({'inputText': 'Tell me a story about magic forest.',
                   })
# print(type(body))
bedrock = boto3.client(service_name='bedrock', region_name='us-east-1') # info about what servicess are aveailable in badrock
# pprint.pp(bedrock.list_foundation_models())
# pprint.pp(bedrock.get_foundation_model(modelIdentifier='amazon.titan-text-express-v1'))



bedrock_runtime = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')
# pprint.pp(bedrock_runtime)

responce = bedrock_runtime.invoke_model(body=body, modelId='amazon.titan-text-express-v1')
# pprint.pp(responce)
responce_body = json.loads(responce.get('body').read())
crean_responce = (responce_body['results'][0]['outputText'])
print(crean_responce)
