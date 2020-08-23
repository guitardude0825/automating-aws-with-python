# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
as_client = session.client('autoscaling')
as_client.describe_auto_scaling_groups()
as_client.describe_policies()
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Out')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Out')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Out')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Out')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Out')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Out', HonorCooldown=False)
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale In', HonorCooldown=False)
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale In', HonorCooldown=False)
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale In', HonorCooldown=False)
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale In', HonorCooldown=False, MetricValue=15.0, BreachThreshold=20.0)
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Out', HonorCooldown=False, MetricValue=100.0, BreachThreshold=50.0)
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Out', HonorCooldown=False, MetricValue=100.0, BreachThreshold=50.0)
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Out', HonorCooldown=False, MetricValue=90.0, BreachThreshold=50.0)
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale In', HonorCooldown=False)
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Out', HonorCooldown=False)
