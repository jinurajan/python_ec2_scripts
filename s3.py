import boto
import boto.s3.connection


class S3(object):
    """docstring for S3"""
    def __init__(self, access_key, secret_key, host, is_secure=True):
        self.aws_access_key_id = access_key
        self.aws_secret_access_key = secret_key
        self.conn = boto.connect_s3(
            aws_access_key_id = access_key,
            aws_secret_access_key = secret_key,
            host = host,
            is_secure = is_secure,
            calling_format = boto.s3.connection.OrdinaryCallingFormat()
            )


    def list_buckets(self):
        for bucket in self.conn.get_all_buckets():
            print "{name}\t{created}".format(
                    name = bucket.name,
                    created = bucket.creation_date,
            )

    def create_bucket(self, bucket_name):
        try:
            self.conn.create_bucket(bucket_name)
        except boto.exception.S3CreateError:
            print "Creation Failed For Bucket: {0} ".format(bucket_name)
            raise S3CreateError(response.status, response.reason)

    def delete_bucket(self, bucket_name):
        self.conn.delete_bucket(bucket_name)


    def list_bucket_content(self, bucket_name):
        for key in bucket.list():
            print "{name}\t{size}\t{modified}".format(
                    name = key.name,
                    size = key.size,
                    modified = key.last_modified,
                    )


# how to use
# s3 = S3(aws_access_key_id=CHANGEME, aws_secret_access_key=CHANGEME, HOST)
# s3.list_buckets()
# s3.create_bucket(give_bucket_name_here)
# s3.delete_bucket(give_bucket_name_here)