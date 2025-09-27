# 🚀 AWS Quick Start & Development Setup

**For Development, Testing, and Learning**

Complete guide to quickly setting up AWS services for development and experimentation with the Global Market Research Agents project.

> 💡 **For Production Deployment**: See [AWS_DEPLOYMENT_GUIDE.md](./AWS_DEPLOYMENT_GUIDE.md) for enterprise-grade deployment using CDK and container orchestration.

## 📋 Prerequisites

- AWS Account with billing enabled
- AWS CLI installed and configured
- Administrative or sufficient IAM permissions
- Python 3.8+ installed locally

## 🔧 Required AWS Services

### Core Services
- **Amazon Bedrock** - Foundation models (Claude 3)
- **Amazon SageMaker** - ML platform and notebooks
- **AWS IAM** - Identity and access management
- **Amazon S3** - Storage for models and data

### Optional Services
- **AWS Lambda** - Serverless deployment
- **Amazon API Gateway** - REST API endpoints
- **Amazon CloudWatch** - Monitoring and logging
- **AWS CloudFormation** - Infrastructure as code

## 🚀 Step-by-Step Setup

### Step 1: Enable Amazon Bedrock

#### 1.1 Request Model Access
```bash
# Navigate to Bedrock console
aws bedrock list-foundation-models --region us-east-1
```

**In AWS Console:**
1. Go to **Amazon Bedrock** → **Model access**
2. Click **Request model access**
3. Select **Anthropic Claude 3 Sonnet**
4. Select **Anthropic Claude 3 Haiku** (optional, for cost optimization)
5. Submit request (usually approved within minutes)

#### 1.2 Verify Access
```bash
# Test Bedrock access
aws bedrock-runtime invoke-model \
  --model-id anthropic.claude-3-sonnet-20240229-v1:0 \
  --body '{"messages":[{"role":"user","content":"Hello"}],"max_tokens":100}' \
  --cli-binary-format raw-in-base64-out \
  output.json
```

### Step 2: Setup Amazon SageMaker

#### 2.1 Create SageMaker Execution Role
```bash
# Create trust policy
cat > trust-policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "sagemaker.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

# Create the role
aws iam create-role \
  --role-name SageMakerExecutionRole \
  --assume-role-policy-document file://trust-policy.json

# Attach required policies
aws iam attach-role-policy \
  --role-name SageMakerExecutionRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerFullAccess

aws iam attach-role-policy \
  --role-name SageMakerExecutionRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess

aws iam attach-role-policy \
  --role-name SageMakerExecutionRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
```

#### 2.2 Create Custom Policy for Bedrock
```bash
# Create Bedrock policy
cat > bedrock-policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ListFoundationModels",
        "bedrock:GetFoundationModel"
      ],
      "Resource": "*"
    }
  ]
}
EOF

# Create and attach the policy
aws iam create-policy \
  --policy-name BedrockInvokePolicy \
  --policy-document file://bedrock-policy.json

aws iam attach-role-policy \
  --role-name SageMakerExecutionRole \
  --policy-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):policy/BedrockInvokePolicy
```

#### 2.3 Create SageMaker Notebook Instance
```bash
# Create notebook instance
aws sagemaker create-notebook-instance \
  --notebook-instance-name market-research-agents \
  --instance-type ml.t3.medium \
  --role-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/SageMakerExecutionRole \
  --default-code-repository https://github.com/your-repo/global-market-research-agents
```

**Or via AWS Console:**
1. Go to **SageMaker** → **Notebook instances**
2. Click **Create notebook instance**
3. **Name**: `market-research-agents`
4. **Instance type**: `ml.t3.medium` (or larger for better performance)
5. **IAM role**: Select the `SageMakerExecutionRole` created above
6. **Git repositories**: Add your project repository
7. Click **Create notebook instance**

### Step 3: Setup S3 Storage

#### 3.1 Create S3 Bucket
```bash
# Create bucket for project data
aws s3 mb s3://market-research-agents-$(aws sts get-caller-identity --query Account --output text)

# Enable versioning
aws s3api put-bucket-versioning \
  --bucket market-research-agents-$(aws sts get-caller-identity --query Account --output text) \
  --versioning-configuration Status=Enabled
```

#### 3.2 Setup Bucket Policy
```bash
# Create bucket policy
cat > bucket-policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/SageMakerExecutionRole"
      },
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::market-research-agents-$(aws sts get-caller-identity --query Account --output text)",
        "arn:aws:s3:::market-research-agents-$(aws sts get-caller-identity --query Account --output text)/*"
      ]
    }
  ]
}
EOF

# Apply bucket policy
aws s3api put-bucket-policy \
  --bucket market-research-agents-$(aws sts get-caller-identity --query Account --output text) \
  --policy file://bucket-policy.json
```

### Step 4: Configure Environment

#### 4.1 Set Environment Variables
```bash
# Add to ~/.bashrc or ~/.zshrc
export AWS_DEFAULT_REGION=us-east-1
export BEDROCK_MODEL_ID=anthropic.claude-3-sonnet-20240229-v1:0
export SAGEMAKER_ROLE_ARN=arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/SageMakerExecutionRole
export S3_BUCKET=market-research-agents-$(aws sts get-caller-identity --query Account --output text)
```

#### 4.2 Test Configuration
```bash
# Test AWS CLI access
aws sts get-caller-identity

# Test Bedrock access
aws bedrock list-foundation-models --region us-east-1

# Test SageMaker access
aws sagemaker list-notebook-instances

# Test S3 access
aws s3 ls s3://market-research-agents-$(aws sts get-caller-identity --query Account --output text)
```

## 🔒 Security Configuration

### IAM Best Practices

#### 1. Principle of Least Privilege
```bash
# Create minimal policy for production
cat > minimal-bedrock-policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel"
      ],
      "Resource": [
        "arn:aws:bedrock:*::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0",
        "arn:aws:bedrock:*::foundation-model/anthropic.claude-3-haiku-20240307-v1:0"
      ]
    }
  ]
}
EOF
```

#### 2. Enable CloudTrail Logging
```bash
# Create CloudTrail for API logging
aws cloudtrail create-trail \
  --name market-research-agents-trail \
  --s3-bucket-name market-research-agents-$(aws sts get-caller-identity --query Account --output text) \
  --s3-key-prefix cloudtrail-logs/ \
  --include-global-service-events \
  --is-multi-region-trail
```

### Network Security

#### 1. VPC Configuration (Optional)
```bash
# Create VPC for SageMaker (optional for enhanced security)
aws ec2 create-vpc --cidr-block 10.0.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=market-research-vpc}]'
```

#### 2. Security Groups
```bash
# Create security group for SageMaker
aws ec2 create-security-group \
  --group-name sagemaker-sg \
  --description "Security group for SageMaker notebook instances"
```

## 💰 Cost Optimization

### 1. Instance Sizing
- **Development**: `ml.t3.medium` ($0.05/hour)
- **Production**: `ml.m5.large` ($0.10/hour)
- **Heavy workloads**: `ml.c5.xlarge` ($0.20/hour)

### 2. Bedrock Model Selection
- **Claude 3 Haiku**: $0.25/1K input tokens, $1.25/1K output tokens
- **Claude 3 Sonnet**: $3/1K input tokens, $15/1K output tokens
- **Use Haiku for simple queries, Sonnet for complex analysis**

### 3. Auto-stopping
```bash
# Configure notebook auto-stop (via lifecycle config)
cat > auto-stop-script.sh << 'EOF'
#!/bin/bash
# Auto-stop after 1 hour of inactivity
echo "*/5 * * * * /opt/ml/bin/idle-check.sh" | crontab -
EOF
```

### 4. S3 Lifecycle Policies
```bash
# Create lifecycle policy for S3
cat > lifecycle-policy.json << EOF
{
  "Rules": [
    {
      "ID": "DeleteOldObjects",
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "STANDARD_IA"
        },
        {
          "Days": 90,
          "StorageClass": "GLACIER"
        }
      ],
      "Expiration": {
        "Days": 365
      }
    }
  ]
}
EOF

aws s3api put-bucket-lifecycle-configuration \
  --bucket market-research-agents-$(aws sts get-caller-identity --query Account --output text) \
  --lifecycle-configuration file://lifecycle-policy.json
```

## 📊 Monitoring and Logging

### 1. CloudWatch Metrics
```bash
# Enable detailed monitoring
aws logs create-log-group --log-group-name /aws/sagemaker/NotebookInstances/market-research-agents
```

### 2. Cost Monitoring
```bash
# Create billing alarm
aws cloudwatch put-metric-alarm \
  --alarm-name "High-AWS-Bill" \
  --alarm-description "Alarm when AWS bill exceeds $100" \
  --metric-name EstimatedCharges \
  --namespace AWS/Billing \
  --statistic Maximum \
  --period 86400 \
  --threshold 100 \
  --comparison-operator GreaterThanThreshold \
  --dimensions Name=Currency,Value=USD \
  --evaluation-periods 1
```

## 🚀 Deployment Options

### Option 1: SageMaker Notebook (Recommended for Development)
- **Pros**: Easy setup, integrated environment, good for experimentation
- **Cons**: Always-on costs, manual scaling
- **Best for**: Development, testing, small-scale usage

### Option 2: SageMaker Endpoints (Production)
- **Pros**: Auto-scaling, high availability, production-ready
- **Cons**: More complex setup, higher minimum costs
- **Best for**: Production deployments, high-volume usage

### Option 3: Lambda + API Gateway (Serverless)
- **Pros**: Pay-per-use, automatic scaling, no infrastructure management
- **Cons**: Cold starts, execution time limits
- **Best for**: Sporadic usage, cost-sensitive deployments

## 🔧 Troubleshooting

### Common Issues

#### 1. Bedrock Access Denied
```bash
# Check model access status
aws bedrock get-model-invocation-logging-configuration --region us-east-1

# Verify IAM permissions
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/SageMakerExecutionRole \
  --action-names bedrock:InvokeModel \
  --resource-arns "*"
```

#### 2. SageMaker Permission Issues
```bash
# Check role trust relationship
aws iam get-role --role-name SageMakerExecutionRole

# List attached policies
aws iam list-attached-role-policies --role-name SageMakerExecutionRole
```

#### 3. S3 Access Issues
```bash
# Test S3 access
aws s3 ls s3://market-research-agents-$(aws sts get-caller-identity --query Account --output text) --region us-east-1

# Check bucket policy
aws s3api get-bucket-policy --bucket market-research-agents-$(aws sts get-caller-identity --query Account --output text)
```

### Performance Issues

#### 1. Slow Model Responses
- Check region proximity to Bedrock endpoints
- Consider using Claude 3 Haiku for faster responses
- Implement response caching

#### 2. Notebook Performance
- Upgrade instance type
- Monitor CPU/memory usage in CloudWatch
- Consider using SageMaker Studio for better performance

## 📞 Support Resources

- **AWS Documentation**: https://docs.aws.amazon.com/
- **Bedrock User Guide**: https://docs.aws.amazon.com/bedrock/
- **SageMaker Developer Guide**: https://docs.aws.amazon.com/sagemaker/
- **AWS Support**: Create support case for technical issues
- **AWS Forums**: https://forums.aws.amazon.com/

## ✅ Setup Verification Checklist

- [ ] AWS CLI configured and working
- [ ] Bedrock model access approved and tested
- [ ] SageMaker execution role created with proper permissions
- [ ] SageMaker notebook instance running
- [ ] S3 bucket created and accessible
- [ ] Environment variables configured
- [ ] Test notebook execution successful
- [ ] Cost monitoring alerts configured

**🎉 Setup complete! You're ready to start using the Global Market Research Agents.**