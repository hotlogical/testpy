import boto3

def pushfile():
    s3_resource = boto3.resource('s3')
    s3_resource.Bucket('genesis-bton').upload_file(
        Filename='toast.txt', Key='toast.txt')

    print('Got here')

if __name__ == '__main__':
    pushfile()