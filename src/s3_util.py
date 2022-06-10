import logging
import boto3
from botocore.exceptions import ClientError

def get_s3_client(profile_name, region_name):
    print('get_s3_client: profile_name=%s, region_name=%s' % (profile_name, region_name))

    session = boto3.Session(profile_name=profile_name)
    s3 = session.client('s3',
        region_name=region_name)
    return s3


def get_s3_bucket_names(profile_name, region_name):
    s3_bucket_names = []

    s3 = get_s3_client(profile_name, region_name)
    if s3 is None:
        print('get_s3_bucket_names: Failed to get s3 client.')
        return s3_bucket_names

    try:
        response = s3.list_buckets()
        print('DEBUG: get_s3_bucket_names: s3.list_buckets() response: %s' % (response))
        if 'Buckets' in response:
            for bucket in response['Buckets']:
                s3_bucket_names.append(bucket['Name'])
        
    except ClientError as e:
        logging.error("get_s3_bucket_names: unexpected error: ")
        logging.exception(e)
        return s3_bucket_names

    return s3_bucket_names

