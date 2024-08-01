import boto3

# Initialize IAM client
iam = boto3.client('iam')

# List of users to delete
users = [
    'user-1',
    'user-2',
    # Add more users here
]

def delete_user_resources(user):
    try:
        print(f"Processing user: {user}")

        # Delete access keys
        print(f"Deleting access keys for user: {user}")
        access_keys = iam.list_access_keys(UserName=user).get('AccessKeyMetadata', [])
        for key in access_keys:
            iam.delete_access_key(UserName=user, AccessKeyId=key['AccessKeyId'])
            print(f"Deleted access key {key['AccessKeyId']} for user: {user}")

        # Detach managed policies
        print(f"Detaching managed policies for user: {user}")
        managed_policies = iam.list_attached_user_policies(UserName=user).get('AttachedPolicies', [])
        for policy in managed_policies:
            iam.detach_user_policy(UserName=user, PolicyArn=policy['PolicyArn'])
            print(f"Detached policy {policy['PolicyArn']} from user: {user}")

        # Remove inline policies
        print(f"Removing inline policies for user: {user}")
        inline_policies = iam.list_user_policies(UserName=user).get('PolicyNames', [])
        for policy in inline_policies:
            iam.delete_user_policy(UserName=user, PolicyName=policy)
            print(f"Removed inline policy {policy} from user: {user}")

        # Remove user from groups
        print(f"Removing user from groups for user: {user}")
        groups = iam.list_groups_for_user(UserName=user).get('Groups', [])
        for group in groups:
            iam.remove_user_from_group(GroupName=group['GroupName'], UserName=user)
            print(f"Removed user: {user} from group: {group['GroupName']}")

        # Delete login profile if it exists
        print(f"Deleting login profile for user: {user}")
        try:
            iam.delete_login_profile(UserName=user)
            print(f"Deleted login profile for user: {user}")
        except iam.exceptions.NoSuchEntityException:
            print(f"No login profile to delete for user: {user}")

        # Finally, delete the IAM user
        print(f"Deleting user: {user}")
        iam.delete_user(UserName=user)
        print(f"Deleted user: {user}")

    except Exception as e:
        print(f"Error deleting user {user}: {e}")

# Iterate over each user and delete their resources
for user in users:
    delete_user_resources(user)