curl -X 'POST' \
  'http://gc3a.stg.g123.jp.private/v1/translation/translate-text' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d @single_long1.json \
  -w "Total time: %{time_total}\n"