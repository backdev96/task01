from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import json


_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        # todo implement business logic
        method = event.get("requestContext")("http")("method")
        path = event.get("requestContext")("http")("path")

        if method == "GET" and path == "/hello":
            return json.dumps({
                    'statusCode': 200,
                    'message': 'Hello from Lambda'
                })
        return {
            "statusCode": 400,
            "message": "Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
        }
        
    

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
