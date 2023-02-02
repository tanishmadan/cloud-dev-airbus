import boto3

def lambda_handler(event,context):
    queryparam= event.get("queryStringParameters", {})
    r=queryparam.get("region")
    print(r)
    region = str(r)
    conn = boto3.resource('ec2', region_name=region)
    instances = conn.instances.all()
    a=()
    for instance in instances:
        #if instance.state["Name"] == "running":
        for tag in instance.tags:
            if 'Name'in tag['Key']:
                name = tag['Value']
        #print (instance.id, name, instance.state["Name"], region)
        a = a + ((instance.id, name, instance.state["Name"], region),)
    print(a)
    response=""
    for item in a:
        response += str(item) + "\n"
    print(response)
    return{
        "statusCode":200,
        "body": response
    }
