# Line chat bot


## 環境設定

```
# python = 3.7.9
pip install -r requirements.txt

# 開啟flask server
python app.py
````
## 本機測試

下載 ngrok 後執行
```
./ngrok http 8080
````

再把ngrok提供的url 設定到 line 的 Webhook URL
(ngrok 的 port 與 flask server 的 port 要相同)

執行flask
```
python app.py
````

## 自動部署 Heroku

<a href="https://heroku.com/deploy?template=https://github.com/hongyuntw/line-chat-bot/tree/master">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>

Deploy 至 Heroku
```
npm i heroku
heroku login -i
heroku git:remote -a [heroku-app-name]
````

部屬完後設定 line 的 Webhook URL 為 HeroKu 的 Domain 即可
如果有任何更新可以執行
```
sh deploy.sh [commit message] 
````
會自動將更新以及commit message推到github repo 以及 重新 deploy 到 heroku
