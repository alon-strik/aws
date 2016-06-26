#!/usr/bin/python
import boto3
import os

s3=boto3.client('s3')
lms_bucket="lms-artifacts"

artifacts=['liquibase','mysql','xml']

list=s3.list_objects(Bucket=lms_bucket)['Contents']

for s3_key in list:
    s3_object = s3_key['Key']

    if not s3_object.endswith("/"):
         if sum([st in s3_object for st in artifacts]) > 0:
           print s3_object
           s3.download_file(lms_bucket, s3_object, s3_object)
    else:
        if not os.path.exists(s3_object):
            os.makedirs(s3_object)
