import boto3

BUCKET = "ishubham-rekognition"
KEY_SOURCE = "image/1.jpg"
KEY_TARGET = "image/4.jpg"
ACCESS_KEY='AKIAIBJ3HF7QA3NO32EA'
SECRET_KEY='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'

def compare_faces(bucket, key, bucket_target, key_target, threshold=80, region="us-west-2"):
	rekognition = boto3.client("rekognition", region,aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY)
	response = rekognition.compare_faces(
	    SourceImage={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		TargetImage={
			"S3Object": {
				"Bucket": bucket_target,
				"Name": key_target,
			}
		},
	    SimilarityThreshold=threshold,
	)
	return response['SourceImageFace'], response['FaceMatches']


source_face, matches = compare_faces(BUCKET, KEY_SOURCE, BUCKET, KEY_TARGET)

# the main source face
print "Source Face ({Confidence}%)".format(**source_face)

# one match for each target face
for match in matches:
	print "Target Face ({Confidence}%)".format(**match['Face'])
	print "  Similarity : {}%".format(match['Similarity'])