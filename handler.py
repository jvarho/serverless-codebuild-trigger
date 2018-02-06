import boto3
import json
import os


REGION=os.environ['region']
PROJECT=os.environ['project']
BRANCH=os.environ.get('branch')


codebuild = boto3.client('codebuild', region_name=REGION)


def build(event, context):
    print(json.dumps(event))
    branch=event['detail']['referenceName']
    commit=event['detail']['commitId']
    print(branch + ':' + commit)
    if BRANCH is None or BRANCH == branch:
        build = codebuild.start_build(projectName=PROJECT, sourceVersion=commit)
        print(json.dumps(build))

