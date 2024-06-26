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
        method = event.get("requestContext").get("http").get("method")
        path = event.get("requestContext").get("http").get("path")

        if method == "GET" and path == "/hello":
            return json.dumps({
                    'statusCode': 200,
                    'message': 'Hello from Lambda'
                })
        return json.dumps({
            "statusCode": 400,
            "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
        })
        

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)