import aws_cdk as core
import aws_cdk.assertions as assertions

from testen.testen_stack import TestenStack

# example tests. To run these tests, uncomment this file along with the example
# resource in testen/testen_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TestenStack(app, "testen")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
