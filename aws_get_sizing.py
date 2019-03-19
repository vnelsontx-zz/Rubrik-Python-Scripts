
########################################################################################################################################################################
# Start of the script - Description, Requirements & Legal Disclaimer
########################################################################################################################################################################
# Description:
# This script connects to an AWS Account and Region to gather sizing data of EBS volumes tied to EC2 instances for a Rubrik CDM Sizing.
########################################################################################################################################################################
# Requirements:
# - An AWS Account ID, Username, Password, Secret Key, Specified Region, and Already Running Instances in EC2
# - AWS CLI
# - AWS Configure completed with default profile entered
# - Python3 Interpreter
# - AWS Python Module - Boto3
# - Maybe more items??
########################################################################################################################################################################
# Legal Disclaimer:
# This script is written by Brian Nelson, it is not supported under any support program or service. 
# All scripts are provided AS IS without warranty of any kind. 
# The author further disclaims all implied warranties including, without limitation, any implied warranties of merchantability or of fitness for a particular purpose. 
# The entire risk arising out of the use or performance of the sample scripts and documentation remains with you. 
# In no event shall its authors, or anyone else involved in the creation, production, or delivery of the scripts be liable for any damages whatsoever 
# (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) 
# arising out of the use of or inability to use the sample scripts or documentation, even if the author has been advised of the possibility of such damages.
########################################################################################################################################################################

#Modules to Import
import boto3

#AWS Account Details are based off the Default Profile in ~/.aws/credentials

ec2 = boto3.resource('ec2')
volume_iterator = ec2.volumes.all()
for v in volume_iterator:
    for a in v.attachments:
        print (a['InstanceId'], v.id, v.size)



