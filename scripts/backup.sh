#!/bin/bash

echo "Taking MongoDB backup..."

docker exec mongodb mongodump --out /data/backup

echo "Backup completed successfully"