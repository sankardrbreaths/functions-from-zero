[![Python CI](https://github.com/sankardrbreaths/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/sankardrbreaths/functions-from-zero/actions/workflows/main.yml)

# functions-from-zero
live training


### To call Microservice
```bash
curl -X 'POST' \
  'https://curly-space-succotash-jjj44wrq59xq3rx-8000.app.github.dev/predict' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft",
  "length": 10
}'
```