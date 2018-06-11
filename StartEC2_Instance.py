import boto3

#define the connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    # Use the filter() method of the instances collection to retrieve
    # all running EC2 instances.
    filters = [{
            'Name': 'tag:Company',
            'Values': ['','']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['stopped']
        }
    ]
    
    #filter the instances
    instances = ec2.instances.filter(Filters=filters)

    #locate all running instances
    StoppedInstances = [instance.id for instance in instances]
    
    #make sure there are actually instances to shut down. 
    if len(StoppedInstances) > 0:
        #perform the shutdown
        StartingIn = ec2.instances.filter(InstanceIds=StoppedInstances).start()
        print StartingIn
    else:
        print "Nothing to see here man"