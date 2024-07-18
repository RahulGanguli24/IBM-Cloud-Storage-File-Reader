import pandas as pd
import ibm_boto3
from ibm_botocore.client import Config, ClientError
#print("Hello, World!")

df = pd.read_csv('Data/Municipality Contact Details.csv')

#print(df) 

def main(params):
  name = params.get("name", "world")
  bucket = params.get("bucket", "s3")
  greeting = "Hello " + name + "!"

  bucketstring = get_buckets()
  
  df = pd.read_csv('Data/Municipality Contact Details.csv')

  return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": "Total Rows: " + str(pd.options.display.max_rows)+ " --> " + greeting + " --> " +bucket + " --> " + bucketstring,
  }

def get_cos_client():
    # Constants for IBM COS values
    COS_ENDPOINT = "https://s3.us-east.cloud-object-storage.appdomain.cloud" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
    COS_API_KEY_ID = "MMj-A6kBsqzIfOTAs8HUWXrL0h6Miv9EJe0GX41i1zHb" # eg "W00YixxxxxxxxxxMB-odB-2ySfTrFBIQQWanc--P3byk"
    COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/3e2d7f0ac149488f932eeb418173ca33:7026d0c9-ae1b-4691-a28c-2a93f07efec9::" # eg "crn:v1:bluemix:public:cloud-object-storage:global:a/3bf0d9003xxxxxxxxxx1c3e97696b71c:d6f04d83-6c4f-4a62-a165-696756d63903::"

    # Create client
    cos_client = ibm_boto3.client("s3",
        ibm_api_key_id=COS_API_KEY_ID,
        ibm_service_instance_id=COS_INSTANCE_CRN,
        config=Config(signature_version="oauth"),
        endpoint_url=COS_ENDPOINT
    )
    return cos_client

def get_buckets():
    print("Retrieving list of buckets")
    cos_client = get_cos_client()
    try:
        bucketstring = "Buckets: "
        buckets = cos_client.list_buckets()
        for bucket in buckets["Buckets"]:
            print("Bucket Name: {0}".format(bucket["Name"]))
            bucketstring = bucket["Name"] + " "
        return bucketstring
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve list buckets: {0}".format(e))
      
#print ( main({"name": "world"}) )
