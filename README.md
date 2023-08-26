# tokyo-opendata-hackathon2023-TOKYOQUEST


## 実行方法
```
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
        "location": {
            "latitude": 緯度(float),
            "longitude": 経度(float)
        },    
        "media" : イベント掲載媒体(string),
        "detail" : イベント内容(string),
        "people" : 過去のイベント規模 人の人数(int)
    },
    {
        "date" : イベントの日付(string, "YYYY-MM-DD"),
        "location": {
            "latitude": 緯度(float),
            "longitude": 経度(float)
        },    
        "media" : イベント掲載媒体(string),
        "detail" : イベント内容(string),
        "people" : 過去のイベント規模 人の人数(int)
    },
]
```

## その他
api → DBへのリクエスト時に過去x日の情報を入れる
