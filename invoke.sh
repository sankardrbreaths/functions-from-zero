
#!/usr/bin/env bash
set -e

BASE_URL="http://localhost:8000"

echo "Testing root endpoint..."
curl -sS -f "$BASE_URL/"
echo

echo "Testing addition endpoint..."
curl -sS -f "$BASE_URL/add/5/10"
echo

echo "Testing Wikipedia prediction endpoint..."
curl -sS -f -X POST "$BASE_URL/predict" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Microsoft",
        "length": 2
    }'
echo
