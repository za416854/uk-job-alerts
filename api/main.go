package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"time"

	"github.com/gofiber/fiber/v2"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

// 職缺資料結構
type Job struct {
	Title    string `json:"title"`
	Company  string `json:"company"`
	Location string `json:"location"`
	URL      string `json:"url"`
}

func main() {
	// 1️⃣ 連接 MongoDB
	mongoURI := os.Getenv("MONGO_URI")
	if mongoURI == "" {
		log.Fatal("請設定 MONGO_URI 環境變數")
	}

	client, err := mongo.NewClient(options.Client().ApplyURI(mongoURI))
	if err != nil {
		log.Fatal(err)
	}
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	err = client.Connect(ctx)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Disconnect(ctx)

	db := client.Database("job_alerts")
	coll := db.Collection("uk_jobs")

	// 2️⃣ 啟動 Fiber App
	app := fiber.New()

	// 3️⃣ GET /jobs 支援 keyword 搜尋
	app.Get("/jobs", func(c *fiber.Ctx) error {
		keyword := c.Query("keyword")
		filter := bson.M{}

		if keyword != "" {
			filter = bson.M{
				"$or": []bson.M{
					{"title": bson.M{"$regex": keyword, "$options": "i"}},
					{"company": bson.M{"$regex": keyword, "$options": "i"}},
				},
			}
		}

		cur, err := coll.Find(ctx, filter)
		if err != nil {
			return c.Status(500).SendString("資料查詢失敗")
		}
		defer cur.Close(ctx)

		var jobs []Job
		for cur.Next(ctx) {
			var job Job
			if err := cur.Decode(&job); err != nil {
				log.Println("資料解碼失敗:", err)
				continue
			}
			jobs = append(jobs, job)
		}

		return c.JSON(jobs)
	})

	// 4️⃣ 啟動服務
	fmt.Println("🚀 Go API is running at http://localhost:3000/jobs")
	log.Fatal(app.Listen(":3000"))
}
