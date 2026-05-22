#!/bin/bash
echo "--- INITIALIZING FINTECH PIPELINE ---"
python3 market_watch.py
python3 analyzer.py
echo "--- PIPELINE COMPLETE: LOGS UPDATED ---"
