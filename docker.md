## build image
```sh
docker build . -t liutsing/30python:<version>
```

## use image
```sh
docker run -it --rm  -v ${PWD}:/app/source  liutsing/30python:<version>
```