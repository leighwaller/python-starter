from moto import mock_s3

import handler

BUCKET = "some-bucket"
KEY = "incoming/transaction-0001.txt"


@mock_s3
def test_handler():
    event = create_s3_event(BUCKET, KEY)

    handler.handle(event, None)

    # todo some assertions


def create_s3_event(bucket_name, key):
    return {
      "Records": [
        {
          "eventVersion": "2.0",
          "eventTime": "1970-01-01T00:00:00.000Z",
          "requestParameters": {
            "sourceIPAddress": "127.0.0.1"
          },
          "s3": {
            "configurationId": "testConfigRule",
            "object": {
              "eTag": "0123456789abcdef0123456789abcdef",
              "sequencer": "0A1B2C3D4E5F678901",
              "key": key,
              "size": 1024
            },
            "bucket": {
              "arn": "bucketarn",
              "name": bucket_name,
              "ownerIdentity": {
                "principalId": "EXAMPLE"
              }
            },
            "s3SchemaVersion": "1.0"
          },
          "awsRegion": "ap-southeast-2",
          "eventName": "ObjectCreated:Put",
          "userIdentity": {
            "principalId": "EXAMPLE"
          },
          "eventSource": "aws:s3"
        }
      ]
    }
