FROM golang:latest

ADD ./ /grpc-stats
WORKDIR /grpc-stats

RUN go build ./app/main.go

EXPOSE 1329
CMD ["./main"]