curl -X 'POST' \
  'http://gc3a.stg.g123.jp.private/v1/translation/translate-text-batch' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d @batch1.json \
  -w "Total time: %{time_total}\n"