# Ingestion Lag Runbook

## Alert
**Name**: IngestionLagHigh  
**Severity**: Critical  
**Threshold**: Ingestion lag > 1000 ledgers

## Symptoms
- Ingestion is behind by more than 1000 ledgers
- Data freshness degraded
- Potential data loss if lag continues to grow

## Immediate Actions

1. **Check Ingestion Status**
   ```bash
   # Check ingestion pods
   kubectl get pods -n mega-header-astroml -l app=mega-header-astroml-ingestion
   
   # Check ingestion metrics
   kubectl exec -n mega-header-astroml deployment/mega-header-astroml-ingestion -- curl localhost:8000/metrics | grep ingestion_lag
   ```

2. **Check Stellar Network Status**
   ```bash
   # Check if Stellar network is experiencing issues
   curl https://horizon.stellar.org/metrics
   
   # Check ledger sequence
   curl https://horizon.stellar.org/ledgers?order=desc&limit=1
   ```

3. **Check Rate Limiting**
   ```bash
   # Check for rate limit backoff
   kubectl logs -n mega-header-astroml deployment/mega-header-astroml-ingestion --tail=100 | grep "rate limit"
   ```

## Common Causes

### 1. Stellar Network Issues
- Horizon API down or slow
- Network connectivity issues
- Stellar network congestion

**Resolution**:
```bash
# Test Horizon connectivity
curl -I https://horizon.stellar.org

# Check Horizon status
curl https://horizon.stellar.org/
```

### 2. Rate Limiting
- Exceeding Stellar API rate limits
- Persistent backoff due to throttling

**Resolution**:
```bash
# Check rate limit status
kubectl logs -n mega-header-astroml deployment/mega-header-astroml-ingestion --tail=200 | grep -i "rate"

# Consider reducing ingestion rate or adding API keys
```

### 3. Resource Constraints
- CPU/memory limits reached
- Database write bottlenecks

**Resolution**:
```bash
# Check resource usage
kubectl top pods -n mega-header-astroml -l app=mega-header-astroml-ingestion

# Scale up if needed
kubectl scale deployment mega-header-astroml-ingestion -n mega-header-astroml --replicas=3
```

### 4. Database Write Performance
- Slow database writes
- Lock contention
- Insufficient database resources

**Resolution**:
```bash
# Check database performance
kubectl exec -n mega-header-astroml postgres-0 -- psql -U mega-header-astroml -d mega-header-astroml -c "
SELECT count(*) FROM normalized_transactions WHERE timestamp > NOW() - INTERVAL '1 hour';
"
```

## Recovery

1. **Resume Ingestion**
   ```bash
   # Restart ingestion service
   kubectl rollout restart deployment/mega-header-astroml-ingestion -n mega-header-astroml
   
   # Monitor recovery
   kubectl logs -f -n mega-header-astroml deployment/mega-header-astroml-ingestion
   ```

2. **Catch-up Strategy**
   - If lag is significant, consider backfill mode
   - Increase ingestion rate temporarily
   - Scale horizontally for faster catch-up

## Prevention

- Monitor ingestion lag continuously
- Set up alerts for smaller lag thresholds (e.g., 500 ledgers)
- Implement automatic scaling based on lag
- Add multiple Horizon endpoints for redundancy
