#!/bin/bash
set -euo pipefail

REGISTRY="${REGISTRY:-ghcr.io}"
REPO="${REPO:-$GITHUB_REPOSITORY}"
IMAGE_TAG="${IMAGE_TAG:-latest}"
NAMESPACE="${NAMESPACE:-mega-header-astroml}"
CANARY_DEPLOYMENT="mega-header-astroml-api-canary"
STABLE_DEPLOYMENT="mega-header-astroml-production"

echo "Promoting canary to stable..."

kubectl set image deployment/${STABLE_DEPLOYMENT} \
  api=${REGISTRY}/${REPO}:${IMAGE_TAG} \
  -n "${NAMESPACE}" --record

kubectl rollout status deployment/${STABLE_DEPLOYMENT} \
  -n "${NAMESPACE}" --timeout=300s

echo "Scaling down canary..."
kubectl scale deployment/${CANARY_DEPLOYMENT} -n "${NAMESPACE}" --replicas=0

echo "Canary promoted successfully"
