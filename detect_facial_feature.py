import boto3
import json


imageFile = "images/kamal.jpg"
carimage="images/car.jpg"
ACCESS_KEY='AKIAIBJ3HF7QA3NO32EA'
SECRET_KEY='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'
region="us-west-2"
client=client= boto3.client("rekognition", region,aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY)

def detectface(imagefile):

    with open(imageFile, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()},Attributes=['ALL'])

    print('Detected faces for Input image')
    for faceDetail in response['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
            + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        print('Gender of detected face is  ' + str(faceDetail['Gender']['Value']))
        c=0
        t=''
        for x in faceDetail['Emotions']:
            if(x['Confidence']>c):
                c=x['Confidence']
                t=x['Type']
        print("Emotions is "+ str(t))
        #print('Here are the other attributes:')
        #print(json.dumps(faceDetail, indent=4, sort_keys=True))




def createcollection(id):
    response=client.create_collection( CollectionId=id)
    print(response['StatusCode'])




def serachFaceInCollection(collection,image1):
    with open(image1, 'rb') as image:
        response = client.search_faces_by_image(CollectionId=collection,
             Image={'Bytes': image.read()},MaxFaces=1,FaceMatchThreshold=70)
    if(len(response["FaceMatches"])<1):
        print(len(response["FaceMatches"]))
        print("This person do not find in collection")
        index_faces(collection,image1)
    else:
        print(response)


def index_faces(collection_id,image2):
    with open(image2, 'rb') as image:
        response = client.index_faces(
            Image={'Bytes': image.read()},
            CollectionId=collection_id,
            ExternalImageId='Unknown',
            DetectionAttributes=['ALL']
        )
    print("Gender: " + response["FaceRecords"][0]["FaceDetail"]["Gender"]["Value"])
    print("AGE:" + str(((response["FaceRecords"][0]["FaceDetail"]["AgeRange"]["Low"]+response["FaceRecords"][0]["FaceDetail"]["AgeRange"]["High"])/2)))
    a=response["FaceRecords"][0]["FaceDetail"]["Emotions"]
    value=''
    for emo in a:
        min=0
        
        if(emo['Confidence']>min):
            value=emo['Type']
    print("Emotions:"+ value)   
    
    print("date:" +response["ResponseMetadata"]["HTTPHeaders"]["date"])
   

if __name__ == "__main__":
    #detectface(imageFile)
    #detectText(carimage)
    #createcollection('shubham')
    #addfaceToCollection('sammed',imageFile)
    serachFaceInCollection('shubham',imageFile)