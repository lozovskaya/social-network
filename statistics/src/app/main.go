package main

import (
	"database/sql"
	"grpc-stats/internal/config"
	"grpc-stats/internal/service"
	"grpc-stats/internal/domain"
	"grpc-stats/internal/repository/clickhouse"
	"log"
	"net"

	pb "grpc-stats/api"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
	_ "github.com/ClickHouse/clickhouse-go/v2"
)

func main() {
	cfg, err := config.Init()
	if err != nil {
		log.Fatalln("ERR: ", err)
	}

	// Connecting to database & creating a repository:
	var conn *sql.DB
	conn, err = sql.Open("clickhouse", cfg.DatabaseUrl)
	if err != nil {
		log.Fatal(err)
	}
	if err := conn.Ping(); err != nil {
		log.Fatal(err)
	}
	// Create a TCP socket
	lis, err := net.Listen("tcp", cfg.GRPCPort)
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	// Create & register the server
	server := grpc.NewServer()
	reflection.Register(server)
	model := domain.NewModel(clickhouse.New(conn))
	pb.RegisterStatsServiceServer(server, stats_service.New(model))

	log.Printf("Server listening to %v", lis.Addr())

	if err = server.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
