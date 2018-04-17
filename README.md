# URL Shortener (AWS Chalice)

Project to create URL Shortener using:
* AWS Chalice
* AWS Lambda
* AWS DynamoDB

## Prerequisites
* AWS Account
* AWS IAM Role with Access Keys and appropriate policies attached
* Python 2.7.x or 3.6.x

## Create DyanmoDB table
* Open the [DynamoDB console](https://console.aws.amazon.com/dynamodb/)
* Choose **Create Table**
* In the Create DynamoDB table screen, do the following:
    * In the **Table name** field, type ```url-shortener```
    * For the **Primary key**, in the **Partition key** field, type ```token```. Set the data type to String.
* Click **Create**.

## Creating AWS Chalice Virtual Environment
```
mkdir aws-chalice
cd aws-chalice
python3 -m venv chalice
source chalice/bin/activate
```

## Installing AWS Chalice and boto3
```
pip3 install chalice
pip3 install boto3
```

### Configuring AWS credentials
```
touch ~/.aws/config
echo "[default]" >> ~/.aws/config
echo "aws_access_key_id=AK123" >> ~/.aws/config
echo "aws_secret_access_key=abc123" >> ~/.aws/config
echo "region=us-east-1" >> ~/.aws/config
```

## Cloning this application from github
```
git clone https://github.com/skipluck/url-shortener-chalice
```

## Running the application locally

AWS Chalice allows you to spin up a local HTTP server that mimics AWS API gateway. This is helpful for testing applications prior to deploying to AWS.
```
chalice local
```

Open a new terminal window and use curl to test
```
curl -H "Content-Type: application/json" -X POST -d '{"url":"https://www.google.com"}' http://localhost:8000/
```

Even while running the application locally it will make entries in DynamoDB on AWS.

## Deploying the application to AWS
```
chalice deploy
```

## Deleting the application from AWS
```
chalice delete
```
