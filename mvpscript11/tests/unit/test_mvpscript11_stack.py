import aws_cdk as core
import aws_cdk.assertions as assertions

from mvpscript11.mvpscript11_stack import Mvpscript11Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in mvpscript11/mvpscript11_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Mvpscript11Stack(app, "mvpscript11")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
