# Honey I shrunk the images - Python edition

This is an experiment to shrink size of the docker images for Python projects. We will take this step by step from simple programs to runnning CLI tools, APIs, and other interesting experiments.

Note: I don't yet recommend this build types for production. For now feel free to play with and see how we can improve this overtime.

## What these experiments will cover?

The experiments will look at the major challenges in packing python projects into binaries and run them in a Scratch container. Basically the binary will be the base image by itself.

## What is Scratch in Docker?

Scratch is a Docker image that is used to build base or parent images. Or in Docker's words, `An explicitly empty image, especially for building images "FROM scratch".`

Although its present in Docker Hub we cannot pull and use it. It's basically a reserved keyword in Docker which says that it will be an empty. You can check this by creating a Dockerfile like this.

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
