import boto3
import pandas as pd
import random
import string
import os

# Initialize a session using Amazon IAM
iam_client = boto3.client('iam')

# Define users and groups
users_groups = {
    'user1': ['existing_group_A', 'existing_group_B'],
    'user2': ['existing_group_A'],
    'user3': ['existing_group_B'],
    
}

# Generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Create users, set passwords, and assign them to groups
def create_users_and_assign_to_groups(users_groups):
    user_credentials = []

    for user, groups in users_groups.items():
        try:
            # Create user
            iam_client.create_user(UserName=user)
            print(f"User '{user}' created successfully.")
        except iam_client.exceptions.EntityAlreadyExistsException:
            print(f"User '{user}' already exists.")
        
        # Set console password
        password = generate_password()
        iam_client.create_login_profile(UserName=user, Password=password, PasswordResetRequired=True)
        print(f"Password set for user '{user}'.")
        
        # Add user to groups
        for group in groups:
            try:
                iam_client.add_user_to_group(UserName=user, GroupName=group)
                print(f"User '{user}' added to group '{group}'.")
            except iam_client.exceptions.NoSuchEntityException:
                print(f"Group '{group}' does not exist.")
        
        # Create access keys for the user
        response = iam_client.create_access_key(UserName=user)
        access_key = response['AccessKey']
        user_credentials.append({
            'UserName': user,
            'AccessKeyId': access_key['AccessKeyId'],
            'SecretAccessKey': access_key['SecretAccessKey'],
            'ConsolePassword': password  # Include console password in the credentials
        })

    return user_credentials

# Save each user's credentials to a separate CSV file
def save_credentials_to_individual_csv(credentials):
    if not os.path.exists('credentials'):
        os.makedirs('credentials')
    
    for cred in credentials:
        user = cred['UserName']
        df = pd.DataFrame([cred])
        filename = f'credentials/{user}_credentials.csv'
        df.to_csv(filename, index=False)
        print(f"Credentials for user '{user}' saved to {filename}")

# Main script execution
user_credentials = create_users_and_assign_to_groups(users_groups)
save_credentials_to_individual_csv(user_credentials)
