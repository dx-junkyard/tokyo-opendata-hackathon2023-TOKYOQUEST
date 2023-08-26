# tokyo-opendata-hackathon2023-TOKYOQUEST


## 実行方法
```
docker-compose down
docker-compose build
docker-compose up

```

## request parameter
なし

## response field
json形式
```
[
    {
        "date" : イベントの日付(string, "YYYY-MM-DD"),
        "address": 住所(string),    
        "media" : イベント掲載媒体(string),
        "detail" : イベント内容(string),
        "people" : 過去のイベント規模 人の人数(int)
    },
    {
        "date" : イベントの日付(string, "YYYY-MM-DD"),
        "address": 住所(string),    
        "media" : イベント掲載媒体(string),
        "detail" : イベント内容(string),
        "people" : 過去のイベント規模 人の人数(int)
    },
]
```

## 住所のdecode方法
Python
```python
decoded_string = "\u6771\u4eac\u90fd\u65b0\u5bbf\u533a\u897f\u65b0\u5bbf\u4e8c\u4e01\u76ee8\u756a1\u53f7".encode('utf-16', 'surrogatepass').decode('utf-16')
print(decoded_string)
```

## その他
api → DBへのリクエスト時に過去x日の情報を入れる
