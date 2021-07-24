
### 実行環境

- python v3.7.3
- pip 18.1 (python 3.7)
- 温湿度センサ DHT11

---

## インストールするもの

```bash
$ pip3 install mongoengine
$ pip3 install dht11
```

### 参考サイト

- Python で MongoDB をつなぐ

https://qiita.com/Syoitu/items/5edf9b422b17699093ac#%E8%A4%87%E6%95%B0%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E4%BF%AE%E6%AD%A3


- DHT11の使い方

https://raspi.taneyats.com/entry/home-electronics-2

---

## 実行

```bash
$ python3 test.py
```

---

## cronの設定

```bash
$ crontab -e
$ sudo systemctl status cron
```

## 5分ごとに test.py を実行。
```bash
*/5 * * * * cd /home/pi/workspace/dht11test/ && python3 test.py
```


