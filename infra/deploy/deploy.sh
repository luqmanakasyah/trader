#!/bin/bash
set -e

# Idempotent deploy script for OVH VPS
# Usage: ./deploy.sh

cd "$(dirname "$0")/../.."

echo "Pulling latest images from GHCR..."
docker-compose pull

echo "Restarting services..."
docker-compose up -d --remove-orphans

echo "Deployment complete."
