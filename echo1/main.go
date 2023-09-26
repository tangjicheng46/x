package main

import (
	"github.com/labstack/echo/v4"
	"net/http"
)

func main() {
	// 创建一个Echo实例
	e := echo.New()

	// 将Echo设置为release模式
	e.Debug = false

	// 定义路由
	e.GET("/hello", func(c echo.Context) error {
		return c.String(http.StatusOK, "hello, world!")
	})

	// 启动Echo服务并绑定到8000端口
	e.Start(":8000")
}

