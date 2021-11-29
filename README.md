# Honey I shrunk the images - Python edition [![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

This is an experiment to shrink the size of the docker images for Python packages. We will take this step by step from simple programs to runnning CLI tools, APIs, and other interesting experiments.

## Inspiration

The inspiration came from a casual conversation with by friend [@shibme](https://github.com/shibme). This [blog](https://medium.com/analytics-vidhya/dockerizing-a-rest-api-in-python-less-than-9-mb-and-based-on-scratch-image-ef0ee3ad3f0a) pointed me out to the right direction. And it deserves a lot of appreciation. Well its atleast good to know that I'm not the first one to try this out.

The [Google Distroless](https://github.com/GoogleContainerTools/distroless) made a lot of sense to use as its very stable and fast. However I wanted to try to build `FROM scratch`!

## Downsides

Packing Python packages into a single binary will be slower than usual as it has to unpack itself before execution due to Python's nature. Also its highly possible that some of the python dependencies will rely on system libraries. In such cases we will have to either pack them along or add them to the working directory. This prevents us from having a standard template to build images. But I'm eager to try this.

## What these experiments will cover?

The experiments will look at the major challenges in packing python packages into binaries and run them in a Scratch container. Basically the binary will be the base image by itself.

## What is Scratch in Docker?

Scratch is a Docker image that is used to build base or parent images. Or in Docker's words, `An explicitly empty image, especially for building images "FROM scratch".`

Although its present in Docker Hub we cannot pull and use it. It's basically a reserved keyword in Docker which says that it will be an empty image. You can check this by creating a Dockerfile like this.

```dockerfile
FROM scratch
```

Now run `docker build -t empty .` and `docker image ls`.
The result will look like this.

```sh
REPOSITORY                        TAG             IMAGE ID       CREATED        SIZE
empty                             latest          71de1148337f   N/A            0B
```

Let's look at the size of the base images we commonly use for python images.

```sh
REPOSITORY                        TAG             IMAGE ID       CREATED        SIZE
alpine                            latest          c059bfaa849c   4 days ago     5.59MB
python                            3.9-slim        3ba8c1c68e98   11 days ago    122MB
debian                            buster-slim     cad9ce16f840   12 days ago    69.3MB
debian                            bullseye-slim   66b2aecdb9f0   12 days ago    80.4MB
```

> Note: I don't yet recommend this build types for production. For now feel free to play with and see how we can improve this overtime.
