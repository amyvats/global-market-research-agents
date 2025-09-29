# 🧹 Cleanup Guide - Post-Execution Resources

This guide helps you clean up AWS resources and temporary files after using the Global Market Research Agents platform to avoid unnecessary costs and maintain security.

## 🚨 Critical AWS Resources to Clean Up

### 💰 Cost-Generating Resources (Clean up immediately)

#### SageMaker Resources
```bash
# Stop SageMaker notebook instances
aws sagemaker stop-notebook-instance --notebook-instance-name market-research-agents

# Delete SageMaker endpoints (if deployed)
aws sagemaker delete-endpoint --endpoint-name market-research-endpoint
aws sagemaker delete-endpoint-config --endpoint-config-name market-research-config
aws sagemaker delete-model --model-name market-research-model
```

#### EC2 Instances (if using custom deployment)
```bash
# List running instances
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"

# Terminate instances (replace with actual instance IDs)
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
```

#### ECS Services (if using containerized deployment)
```bash
# Stop ECS services
aws ecs update-service --cluster market-research-cluster --service market-research-service --desired-count 0

# Delete ECS services and clusters
aws ecs delete-service --cluster market-research-cluster --service market-research-service
aws ecs delete-cluster --cluster market-research-cluster
```

### 🗄️ Storage Resources

#### S3 Buckets
```bash
# List buckets created for the project
aws s3 ls | grep market-research

# Empty and delete buckets (replace with actual bucket names)
aws s3 rm s3://market-research-data-bucket --recursive
aws s3 rb s3://market-research-data-bucket

# Clean up RAG vector stores
aws s3 rm s3://your-rag-bucket/market_research_vectorstore/ --recursive
```

#### EBS Volumes (orphaned volumes)
```bash
# List available (unattached) volumes
aws ec2 describe-volumes --filters "Name=status,Values=available"

# Delete orphaned volumes (replace with actual volume IDs)
aws ec2 delete-volume --volume-id vol-1234567890abcdef0
```

### 🔐 Security Resources

#### IAM Roles and Policies (if created specifically for project)
```bash
# List roles created for the project
aws iam list-roles | grep -i market-research

# Detach policies and delete roles (be careful with existing roles)
aws iam detach-role-policy --role-name MarketResearchSageMakerRole --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerFullAccess
aws iam delete-role --role-name MarketResearchSageMakerRole
```

#### Security Groups
```bash
# List security groups
aws ec2 describe-security-groups --filters "Name=group-name,Values=*market-research*"

# Delete custom security groups (replace with actual group IDs)
aws ec2 delete-security-group --group-id sg-1234567890abcdef0
```

## 📁 Local File Cleanup

### Temporary Files and Caches
```bash
# Remove Python cache files
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -name "*.pyc" -delete
find . -name "*.pyo" -delete

# Remove Jupyter checkpoint files
find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +

# Remove temporary data files
rm -rf market_data/
rm -rf *.json
rm -rf rag_infrastructure_config.json
rm -rf market_research_vectorstore/
rm -rf *.faiss
rm -rf *.pkl
```

### Generated Reports and Logs
```bash
# Remove generated PDF reports (keep if needed)
rm -rf reports/
rm -rf *.pdf

# Remove log files
rm -rf logs/
rm -rf *.log
```

### Environment Files (Security Critical)
```bash
# Remove any accidentally committed environment files
rm -f .env
rm -f .env.local
rm -f .env.production
rm -f aws-exports.js

# Remove AWS credential files (if accidentally created locally)
rm -rf .aws/
```

## 🔍 Verification Commands

### Check for Running Resources
```bash
# Check SageMaker instances
aws sagemaker list-notebook-instances --status-equals InService

# Check EC2 instances
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running,pending"

# Check ECS services
aws ecs list-services --cluster market-research-cluster

# Check S3 buckets
aws s3 ls | grep -i market

# Check for unattached EBS volumes
aws ec2 describe-volumes --filters "Name=status,Values=available"
```

### Cost Monitoring
```bash
# Check current month costs (requires Cost Explorer API access)
aws ce get-cost-and-usage \
  --time-period Start=2024-01-01,End=2024-01-31 \
  --granularity MONTHLY \
  --metrics BlendedCost \
  --group-by Type=DIMENSION,Key=SERVICE
```

## 📊 Cleanup Checklist

### Immediate Actions (Cost-Critical)
- [ ] Stop all SageMaker notebook instances
- [ ] Delete SageMaker endpoints and models
- [ ] Terminate EC2 instances
- [ ] Stop ECS services
- [ ] Empty and delete S3 buckets
- [ ] Delete unattached EBS volumes

### Security Actions
- [ ] Remove local environment files
- [ ] Delete temporary AWS credentials
- [ ] Remove custom IAM roles (if safe)
- [ ] Delete custom security groups
- [ ] Clear browser saved passwords/tokens

### Local Cleanup
- [ ] Remove Python cache files
- [ ] Delete Jupyter checkpoints
- [ ] Clean up temporary data files
- [ ] Remove generated reports (if not needed)
- [ ] Clear log files

### Verification
- [ ] Confirm no running instances
- [ ] Verify S3 buckets are deleted
- [ ] Check AWS billing dashboard
- [ ] Confirm local files are cleaned

## 💡 Best Practices for Future Use

### Cost Management
1. **Set up billing alerts** before running the project
2. **Use SageMaker auto-stop** for notebook instances
3. **Tag all resources** for easy identification and cleanup
4. **Monitor costs daily** during active development

### Security
1. **Never commit credentials** to version control
2. **Use IAM roles** instead of access keys when possible
3. **Regularly rotate** access keys and tokens
4. **Enable CloudTrail** for audit logging

### Resource Management
1. **Use consistent naming** conventions for easy identification
2. **Document custom resources** in your deployment notes
3. **Automate cleanup** with scripts or Lambda functions
4. **Regular cleanup schedule** (weekly/monthly)

## 🆘 Emergency Cleanup

If you need to quickly stop all costs:

```bash
#!/bin/bash
# Emergency cleanup script - USE WITH CAUTION

echo "🚨 Emergency AWS cleanup starting..."

# Stop all SageMaker notebook instances
aws sagemaker list-notebook-instances --status-equals InService --query 'NotebookInstances[].NotebookInstanceName' --output text | xargs -I {} aws sagemaker stop-notebook-instance --notebook-instance-name {}

# Terminate all running EC2 instances (BE VERY CAREFUL)
# aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query 'Reservations[].Instances[].InstanceId' --output text | xargs -I {} aws ec2 terminate-instances --instance-ids {}

echo "✅ Emergency cleanup completed. Check AWS console to verify."
```

## 📞 Support

If you encounter issues during cleanup:

1. **AWS Support**: Use AWS Support Center for billing or resource issues
2. **Documentation**: Check AWS service-specific cleanup guides
3. **Community**: AWS forums and Stack Overflow for technical questions

---

**⚠️ Important: Always verify resource deletion in the AWS Console and monitor your billing dashboard for 24-48 hours after cleanup to ensure all charges have stopped.**