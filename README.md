# HK District Check (AWS Lambda)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Focinpp%2Faws-hk-district-check.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Focinpp%2Faws-hk-district-check?ref=badge_shield)


AWS Lambda function (deployed by serverless) to check the district in Hong Kong of a given GPS coordinate

## Usage

GPS coordinates (latitude, longitude) will be checked against the district boundaries defined using the data from https://data.gov.hk/en-data/dataset/hk-had-json1-hong-kong-administrative-boundaries

Please note that the data is in [GML](https://en.wikipedia.org/wiki/Geography_Markup_Language), with the format (longitude, latitude)

## Requirement

- [serverless framework](https://serverless.com/)
- [Serverless Python Requirements](https://www.npmjs.com/package/serverless-python-requirements)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

## Pytohn Libraries

- pandas
- matplotlib

## Setup and Deployment

Clone the repository

Install the required npm packages

```bash
npm install
```

Setup AWS Credentials following the article https://serverless.com/framework/docs/providers/aws/guide/credentials/

Create a virtual environment (venv) for developing locally and to have the dependencie separated from other environments

```bash
virtualenv venv --python=python3
```

Generate the file requirements.txt in the virtual environment using the below command

```bash
pip freeze > requirements.txt
```

Deploy to AWS with the below command

```bash
serverless deploy
```

## Example

22.301590, 114.174826 => Yau Tsim Mong

## Remarks



## Reference

[Handle Lambda Errors in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/handle-errors-in-lambda-integration.html)

[How to Handle your Python packaging in Lambda with Serverless plugins](https://serverless.com/blog/serverless-python-packaging/)


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Focinpp%2Faws-hk-district-check.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Focinpp%2Faws-hk-district-check?ref=badge_large)