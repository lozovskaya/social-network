package main

import (
	"context"
	pb "grpc-posts-server/api"
	"grpc-posts-server/internal/config"
	"grpc-posts-server/internal/domain"
	"grpc-posts-server/internal/repository/postgres"
	"grpc-posts-server/internal/service"
	"log"
	"net"

	"github.com/jackc/pgx/v4/pgxpool"
	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
)

func main() {
	cfg, err := config.Init()
	if err != nil {
		log.Fatalln("ERR: ", err)
	}

	// Connecting to database & creating a repository:
	ctx := context.Background()
	pool, err := pgxpool.Connect(ctx, cfg.DatabaseUrl)
	if err != nil {
		log.Fatalf("Connecting to database: %v", err)
	}
	defer pool.Close()

	repo := postgres.New(pool)

	// Create a TCP socket
	lis, err := net.Listen("tcp", cfg.GRPCPort)
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	// Create & register the server
	server := grpc.NewServer()
	reflection.Register(server)
	model := domain.NewModel(repo)
	pb.RegisterPostServiceServer(server, post_service.New(model))

	log.Printf("Server listening to %v", lis.Addr())

	if err = server.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
