To generate the new proto files:

```bash
protoc --go_out=. --go-grpc_out=. posts.proto 
python3 -m grpc_tools.protoc -I. --python_out=../../../gateway/src/src/protos --pyi_out=../../../gateway/src/src/protos --grpc_python_out=../../../gateway/src/src/protos posts.proto
```