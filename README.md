serverless-codebuild-trigger
==

This is an example serverless project for triggering CodeBuild on
CodeCommit pushes. For some reason there is no trigger for that in AWS.


Usage
--

1. Install requirements:

    npm install -g serverless
    npm install serverless-python-requirements


2. Copy serverless.template.yml into serverless.yml

Fill in the custom variables at the top.

* project and projectArn refer to the CodeBuild project
* repoArn refers to the CodeCommit repository from which to build

Those should already exist. This only generates a lambda and the triggers.


3. Run ´serverless deploy´.

After that any commit to the CodeCommit repository will start a CodeBuild.

If you only want to act on a single branch (e.g. master), you can set it
in custom variables.
