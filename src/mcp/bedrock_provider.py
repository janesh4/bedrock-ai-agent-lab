import boto3
import json
from config.model_config import ModelConfig


class BedrockProvider:

    def __init__(self):
        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=ModelConfig.REGION
        )

    def invoke_llm(self, prompt):

        payload = {
            "prompt": prompt,
            **ModelConfig.DEFAULT_PARAMS
        }

        response = self.client.invoke_model(
            modelId=ModelConfig.MODEL_ID,
            body=json.dumps(payload),
            contentType="application/json",
            accept="application/json"
        )

        result = json.loads(response["body"].read())

        return result["completion"]
