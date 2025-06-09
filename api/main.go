package main

import (
	"context"
	"log"
	"time"

	"github.com/gofiber/fiber/v2"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type Job struct {
	Title    string `json:"title"`
	Company  string `json:"company"`
	Location string `json:"location"`
	URL      string `json:"url"`
}

func main() {
	app := fiber.New()

	client, err := mongo.NewClient(options.Client().ApplyURI("你的Mongo URI"))
	if err != nil {
		log.Fatal(err)
	}
	ctx, _ := context.WithTimeout(context.Background(), 10*time.Second)
	err = client.Connect(ctx)
	if err != nil {
		log.Fatal(err)
	}
	collection := client.Database("job_alerts").Collection("uk_jobs")

	app.Get("/jobs", func(c *fiber.Ctx) error {
		cursor, err := collection.Find(context.TODO(), map[string]interface{}{})
		if err != nil {
			return c.Status(500).SendString("DB Error")
		}
		var results []Job
		if err := cursor.All(context.TODO(), &results); err != nil {
			return c.Status(500).SendString("Parse Error")
		}
		return c.JSON(results)
	})

	log.Fatal(app.Listen(":3000"))
}
