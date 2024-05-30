FROM golang:latest

ADD ./ /grpc-posts-server
WORKDIR /grpc-posts-server

RUN go build ./cmd/app/main.go

EXPOSE 50052

CMD ["./main"]
