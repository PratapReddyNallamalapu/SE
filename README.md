# SE
Sure, I'll outline a step-by-step process to accomplish the tasks using AWS Cloud9, DynamoDB, Lambda, API Gateway, and testing the application.

Step 1: Set Up AWS Cloud9
1. Create an AWS Cloud9 Environment:
   - Go to the AWS Management Console and search for "Cloud9".
   - Click "Create Environment", provide a name, and choose the settings that suit your needs.
   - Click "Next Step" and then "Create Environment".

2. Open the Cloud9 Environment:
   - Once the environment is created, open it in the AWS Cloud9 IDE.

 Step 2: Create a DynamoDB Table
1. Open AWS DynamoDB:
   - Go to the AWS Management Console, search for "DynamoDB", and open it.

2. Create a Table:
   - Click "Create table".
   - Set the table name as "properties".
   - Define the primary key, for example, "pid" as the partition key.
   - Configure other settings as needed and click "Create".

Step 3: Create a Lambda Function
1. Create a Lambda Function:
   - Go to the AWS Management Console and search for "Lambda".
   - Click "Create function".
   - Choose "Author from scratch".
   - Give your function a name and select the runtime .
   - Click "Create function".

2. Code Your Lambda Function:
   - In the Lambda function editor, paste the code you want to run. 
   - Configure the function handler and required permissions.
   - Save the function.

 Step 4: Create a REST API with API Gateway
1. Create an API:
   - Go to the AWS Management Console, search for "API Gateway", and open it.
   - Click "Create API".
   - Choose the type of API (REST ).
   - Select "New API" and give it a name.

2. Create a Resource and Method:
   - Define a resource and method for your API.
   - Configure the integration with your Lambda function to handle the respective method.

3. Deploy the API:
   - Deploy the API to a stage to make it live.
   - Obtain the endpoint URL.



