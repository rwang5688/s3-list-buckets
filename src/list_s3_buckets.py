import s3_util


def main():
    print('\nStarting list_s3_buckets.py ...')

    # We would normally set these via config file or env vars
    # Hard coding these to keep the demo simple
    profile_name = 'default'
    region_name = 'us-west-2'

    s3_bucket_names = s3_util.get_s3_bucket_names(profile_name, region_name)
    num_s3_bucket_names = len(s3_bucket_names)

    print("s3_bucket_names: ")
    print(s3_bucket_names)
    print("Total # of S3 Buckets: %d" % num_s3_bucket_names)

    print('\n... Thaaat\'s all, Folks!')


if __name__ == '__main__':
    main()

