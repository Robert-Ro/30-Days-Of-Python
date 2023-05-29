## build image
```sh
docker build . -t liutsing/30python:<version>
```

## use image
```sh
docker run -it --rm  -v ${PWD}:/app/source  liutsing/30python:<version>
```

## 先打开文件进行分析，再进行针对性的提取