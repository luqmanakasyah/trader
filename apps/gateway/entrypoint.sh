#!/bin/bash
set -e

# Source env file
source /env.gateway

# Start IB Gateway with IBC (headless)
cd /opt/ibkr
xvfb-run -a ./IBC/IBC.sh gateway &

wait
