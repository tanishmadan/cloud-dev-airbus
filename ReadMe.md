List of Resources used for this challenge.
1. ec2: instance created via YAML
2. lambda: The lambda is created using YAML, it contains the python code for getting the list of ec2 servers in a region
3. API: Front end interface for the user to request the list of servers running in a region.
4. CodeBuild: It is used to deploy the latest version of the python code from the S3 bucket to the lambda
5. S3 Bucket: An S3 bucket was created to hold the latest python code (get_ec2.zip) for the lambda and the buildspec (codebuild.zip) to be used by the CodeBuild.

https://api-id.execute-api.us-east-2.amazomaws.com/region/name?region=xxx

I have used the query string parameter region (us-east-2/eu-central-1 etc) for which the code returns the list of servers.

Python Code : The python code uses boto3 library. It takes the region from the query string parameter of the api request and return the list of servers in that region of the account.

BuildSpec : The build spec file is created to fetch the latest zipped python code and upload that code to lambda.


