# coding: utf-8
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2020-08-25T12:15:06.933Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AIDAR3A6QSU5CGJXMDJFM'}, 'requestParameters': {'sourceIPAddress': '72.189.84.198'}, 'responseElements': {'x-amz-request-id': '4E953E75F61455EB', 'x-amz-id-2': 'vw0A0co/7HVopVtagnSR3YFZrsHYgLrv8zulZquDjnnchO4eDUv/HyAP2rxAr2MkqNSPU86AUtvnqznQdoPoNpkf878Qbshi'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '673f0e0a-87fd-41e2-87d5-213c302ea1e5', 'bucket': {'name': 'tcoyle0825videolyzer08242020', 'ownerIdentity': {'principalId': 'A3IAVAM5H8PL8Z'}, 'arn': 'arn:aws:s3:::tcoyle0825videolyzer08242020'}, 'object': {'key': 'flowerfloat.mp4', 'size': 358619, 'eTag': '362ad5ab3d0e89c42cd4bc2a1559b551', 'sequencer': '005F4500CC284FEFE4'}}}]}
event
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
