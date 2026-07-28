# API Availability Runbook

## Alert
**Name**: ApiAvailabilityLow  
**Severity**: Critical  
**SLO**: API availability 99.9% (error rate <0.1%)

## Symptoms
- API error rate exceeds 0.1% (5xx errors)
- Users experiencing failed requests
- Error budget being consumed

## Immediate Actions

1. **Check Alert Status**
   ```bash
   # Verify current error rate
   kubectl top pods -n mega-header-astroml
   kubectl logs -n mega-header-astroml deployment/mega-header-astroml-api --tail=100
   ```

2. **Check Service Health**
   ```bash
   # Check pod status
   kubectl get pods -n mega-header-astroml -l app=mega-header-astroml-api
   
   # Check service endpoints
   kubectl get endpoints mega-header-astroml-api -n mega-header-astroml
   ```

3. **Check Database Connectivity**
   ```bash
   # Test database connection
   kubectl exec -n mega-header-astroml deployment/mega-header-astroml-api -- python -c "
   from api.database import get_async_session_factory
   factory = get_async_session_factory()
   with factory() as session:
       print('DB connection successful')
   "
   ```

## Common Causes

### 1. Database Issues
- Database connection pool exhausted
- Slow queries causing timeouts
- Database unresponsive

**Resolution**:
```bash
# Check database pods
kubectl get pods -n mega-header-astroml -l app=postgres

# Check database metrics
kubectl exec -n mega-header-astroml postgres-0 -- psql -U mega-header-astroml -d mega-header-astroml -c "
SELECT state, count(*) FROM pg_stat_activity GROUP BY state;
"
```

### 2. Resource Exhaustion
- CPU/memory limits reached
- Pod evictions
- OOM kills

**Resolution**:
```bash
# Check resource usage
kubectl top pods -n mega-header-astroml

# Check pod events
kubectl describe pod <pod-name> -n mega-header-astroml
```

### 3. Application Errors
- Unhandled exceptions
- Dependency failures
- Configuration issues

**Resolution**:
```bash
# Check application logs
kubectl logs -n mega-header-astroml deployment/mega-header-astroml-api --tail=500 --previous

# Check for recent deployments
kubectl rollout history deployment/mega-header-astroml-api -n mega-header-astroml
```

## Escalation

If unable to resolve within 15 minutes:
1. Escalate to on-call engineering lead
2. Consider rolling back recent deployment
3. Enable maintenance mode if necessary

## Rollback Procedure

```bash
# Rollback to previous deployment
kubectl rollout undo deployment/mega-header-astroml-api -n mega-header-astroml

# Verify rollback
kubectl rollout status deployment/mega-header-astroml-api -n mega-header-astroml
```

## Prevention

- Monitor error budget consumption
- Set up synthetic monitoring
- Implement circuit breakers
- Add more comprehensive error handling
