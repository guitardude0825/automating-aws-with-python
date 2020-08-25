# coding: utf-8
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:126765536570:handleLabelDetectionTopic:ac908fb6-3e12-4660-a8b8-e21553754cbc', 'Sns': {'Type': 'Notification', 'MessageId': '0341ace1-3266-515d-bf2b-fb5e1b1e9bff', 'TopicArn': 'arn:aws:sns:us-east-1:126765536570:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"8ddc63533d8396a12d400fb6478f6274f1755461913365a3120555ced82d3ab9","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1598367544028,"Video":{"S3ObjectName":"flowerfloat.mp4","S3Bucket":"tcoyle0825videolyzer08242020"}}', 'Timestamp': '2020-08-25T14:59:04.087Z', 'SignatureVersion': '1', 'Signature': 'ZyOUC1qsiq9uPGhtwlnbeu6uHp10Uu0bjGJK/rq8RzXXkKhEWvpwk0fb4M2JMZwXTXgAea+7IkzNnQiZVIKLm3KkfnM9Ikwn7XkZMTaoheWKEBttxUK4GRY5njgb4gnpM+QCa62MO5GZrEhLdK3teIGdmLjNK/mZr9HrbyWVUvL016QjptCS3W3T9rvkgx/w7vZUA5lwkiDlXaBClAqHyTOgf4OKDV0U+TLCA68Q+xUEWVK4YTbi830y3ZWGUd1knllpqlj/qVPQzk2cSLhyXNdEkqAH1MEwS2Au6qx7DLIT/1ZebLEHDmjKN9URNl3bMGz1U+hP9gWhfBXzs/bvhg==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-a86cb10b4e1f29c941702d737128f7b6.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:126765536570:handleLabelDetectionTopic:ac908fb6-3e12-4660-a8b8-e21553754cbc', 'MessageAttributes': {}}}]}
event
event['Records'][0].keys()
event['Records'][0]['EventSource']
event['Records'][0]['EventVersion']
event['Records'][0]['EventSubscriptionArn']
event['Records'][0]['Sns']
event['Records'][0]['Sns']['Message']
event['Records'][0]['Sns']['Message']['JobId']
type(event['Records'][0]['Sns']['Message']['JobId'])
import json
json.loads(event['Records'][0]['Sns']['Message'])
