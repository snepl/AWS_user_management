1. How to create & delete IAM Users using AWS SDK (Boto3 for Python)

This script (iamusercreate.py) will create IAM users, assign them to specified groups, generate passwords for AWS Management Console access, and create access keys for programmatic access, saving all credentials in a CSV file.

Another script (iamuserdelete.py) will detach managed policy, remove inline policies, delete access key and remove from groups and delete users.

If you’re comfortable with programming, you can use the AWS SDKs (like Boto3 for Python) to automate this process. Here’s a basic example using Boto3:

Note: Before this, install AWS CLI client and configure your access. Documentation: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html . 

AWS Credentials Configuration: You need to configure AWS credentials to allow boto3 to authenticate and make API calls. 
IAM Permissions: Ensure that the IAM user or role associated with the credentials has the necessary permissions to create users, groups, and manage access keys in AWS IAM.

2. Write Your Python Code
You can write Python code using any text editor (like Notepad, VS Code, Sublime Text, etc.). Save your code with a .py file extension. For example, script.py.
3. Execute Python Code
Here’s how you can execute Python code depending on your environment:
Using Command Line Interface (CLI):
•	Windows:
1.	Open Command Prompt or PowerShell.
2.	Navigate to the directory where your Python script is located using the cd command.
3.	Run the script by typing:

python script.py


Using an Integrated Development Environment (IDE):
•	Visual Studio Code (VS Code):
1.	Open VS Code.
2.	Install the Python extension if you haven’t already.
3.	Open your Python file in VS Code.
4.	Press Ctrl+F5 (or Cmd+F5 on macOS) to run the code, or use the green play button in the top right corner.
•	PyCharm:
1.	Open PyCharm.
2.	Create or open a Python project.
3.	Open your Python file.
4.	Right-click inside the editor and select Run 'script', or use the green play button.

