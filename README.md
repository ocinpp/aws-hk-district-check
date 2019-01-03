# HK District Check (AWS Lambda)

AWS Lambda function (deployed by serverless) to check the district in Hong Kong of a given GPS coordinate

## Usage

GPS coordinates (latitude, longitude) will be checked against the district boundaries defined using the data from https://data.gov.hk/en-data/dataset/hk-had-json1-hong-kong-administrative-boundaries

Please note that in GML, the format is (longitude, latitude)

## Requirement

- [serverless framework](https://serverless.com/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

## Deployment

To be added

## Reference

### Handle Lambda Errors in API Gateway

https://docs.aws.amazon.com/apigateway/latest/developerguide/handle-errors-in-lambda-integration.html
