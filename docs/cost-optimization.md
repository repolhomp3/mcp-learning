# AWS Cost Optimization for MCP Learning

## Free Tier Services to Focus On

### Always Free
- **Lambda**: 1M requests/month
- **DynamoDB**: 25 GB storage, 25 RCU/WCU
- **S3**: 5 GB storage, 20K GET requests
- **CloudWatch**: 10 metrics, 5 GB logs

### 12-Month Free Tier
- **EC2**: 750 hours t2.micro/t3.micro
- **RDS**: 750 hours db.t2.micro
- **Elastic Load Balancer**: 750 hours

## Bedrock Cost Management

### Cheapest Models (as of 2024)
1. **Amazon Titan Text Lite**: ~$0.0003/1K tokens
2. **Claude Instant**: ~$0.0008/1K tokens  
3. **Cohere Command Light**: ~$0.0015/1K tokens

### Cost Control Strategies
- Limit max_tokens to 100-200 for learning
- Use batch processing when possible
- Monitor usage in AWS Billing Dashboard
- Set up billing alerts at $5, $10 thresholds

## Development Best Practices

### Local First
- Use SQLite instead of RDS for development
- Test MCP servers locally before AWS integration
- Use AWS CLI/SDK for one-off operations

### Monitoring
```bash
# Check AWS costs
aws ce get-cost-and-usage --time-period Start=2024-01-01,End=2024-01-31 --granularity MONTHLY --metrics BlendedCost

# Monitor Bedrock usage
aws bedrock list-model-invocation-jobs --region us-east-1
```

### Emergency Stop
If costs spike:
1. Check AWS Billing Dashboard
2. Stop/terminate running resources
3. Review CloudTrail for unexpected API calls
4. Set up stricter IAM policies