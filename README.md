### Скачать репозиторий протоколов:
```
git clone git@github.com:wrs-news/node-protocol.git proto
```
### Скомпилировать protos в python:
```
python -m grpc_tools.protoc -I./proto/core --python_out=pkg/proto/core --grpc_python_out=pkg/proto/core ./proto/core/error.proto

python -m grpc_tools.protoc -I./proto/user --python_out=./pkg/proto/user --grpc_python_out=./pkg/proto/user ./proto/user/user-microservice.proto

python -m grpc_tools.protoc -I./proto/parser --python_out=./pkg/proto/parser --grpc_python_out=./pkg/proto/parser ./proto/parser/tass/tass-parser.proto

```