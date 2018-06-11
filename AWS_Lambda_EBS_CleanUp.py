import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):

    deletedVolumes=[]

    # Get all the volumes
    for vol in ec2.volumes.all():
        if  vol.state=='available':

            vid=vol.id
            v=ec2.Volume(vol.id)
            v.delete()

            deletedVolumes.append({'VolumeId': vol.id,'Status':'Delete Initiated'})
            print "Deleted Volume: {0}".format( vid )

            continue

    if not deletedVolumes:
        deletedVolumes.append({'VolumeId':None,'Status':None})

    return deletedVolumes