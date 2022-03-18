import aws_cdk as core
import aws_cdk.assertions as assertions

from mvpscript12.mvpscript12_stack import Mvpscript12Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in mvpscript12/mvpscript12_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Mvpscript12Stack(app, "mvpscript12")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
