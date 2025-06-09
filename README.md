# UK Job Alert Bot (Line Notify + Python + MongoDB + GitLab CI)

每天自動爬取英國職缺網站（Reed），過濾職缺後推播至 Line。

## 技術棧
- Python: 網頁爬蟲 + 推播
- Go 寫一個 REST API，可以透過網頁查詢 MongoDB 裡抓到的職缺資料。
- MongoDB Atlas: 儲存職缺
- GitLab CI: 每日定時執行
- Line Notify: 發送通知


## Getting started
```
python -m venv venv
venv\Scripts\activate (windows) or source venv/bin/activate(linux)



pip install requests beautifulsoup4 
or 
pip install --no-user requests beautifulsoup4 (for replit)


python -m pip install "pymongo[srv]" 
or 
python -m pip install --no-user "pymongo[srv]" (for replit)

pip install requests
or 
pip install --no-user requests (replit)

pip install python-dotenv

pip freeze > requirements.txt

前往 https://go.dev/dl/  安裝 Golang（如果你還沒裝）
then test prompt: go version

建立 Go API 專案（在 api/ 資料夾）
cd api
go mod init uk-job-alerts

go get github.com/gofiber/fiber/v2
or
go install github.com/gofiber/fiber/v2

請運行以下prompt: 
python -m crawler.fetch_jobs

```


## 開debug模式
```
首先ctrl + shift + D 開 launch.json，再來configurations參數更改如下:
"configurations": [
        {
            "name": "Python: fetch_jobs (by module)",
            "type": "debugpy",
            "request": "launch",
            "module": "crawler.fetch_jobs",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        }
    ]
```
## 如何使用
1. 建立 .env 檔，填入 LINE_NOTIFY_TOKEN
2. 設定 GitLab CI 排程
3. 每天早上就會收到 UK 新職缺！

## 專案結構
- crawler/fetch_jobs.py：爬取職缺資料
- notifier/line_notify.py：發送 Line 通知
- .gitlab-ci.yml：自動排程腳本
