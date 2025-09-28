#!/usr/bin/env python3
"""
Quick Bedrock Access Checker
"""
import boto3
import json

def check_bedrock_access():
    try:
        bedrock = boto3.client('bedrock-runtime', region_name='us-west-2')
        
        # Try a minimal request to Titan Text Lite
        body = {
            "inputText": "Hi",
            "textGenerationConfig": {
                "maxTokenCount": 10,
                "temperature": 0.1
            }
        }
        
        response = bedrock.invoke_model(
            modelId='amazon.titan-text-lite-v1',
            body=json.dumps(body),
            contentType='application/json'
        )
        
        print("✅ Bedrock access is working!")
        result = json.loads(response['body'].read())
        print(f"Test response: {result['results'][0]['outputText']}")
        return True
        
    except Exception as e:
        if "AccessDeniedException" in str(e):
            print("⏳ Still waiting for model access approval...")
        else:
            print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    check_bedrock_access()