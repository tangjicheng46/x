package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	// 创建一个Gin引擎
	r := gin.New()

	// 设置Gin模式为发布模式
	gin.SetMode(gin.ReleaseMode)

	// 定义一个路由，对 "/hello" 返回 "hello, world!" 并返回 200 OK
	r.GET("/hello", func(c *gin.Context) {
		c.String(200, "hello, world!")
	})

	// 启动Gin服务器，默认监听在 ":8080" 端口
	r.Run(":8000")
}
