# First we use a build environment to perform all our necessary actions
FROM python:3.9-slim as build-env
# To build the binaries we will need some packages
RUN apt-get update && apt-get install build-essential patchelf -y
# Although we don't need a work dir, we create one to keep our build environment clean so copying becomes easy later
WORKDIR /build
COPY . /build
RUN pip install staticx pyinstaller
# Since there are no requirements for this project, we can just build the binaries 
RUN pyinstaller -F helloworld/main.py -n binary --clean
RUN staticx dist/binary dist/app --strip

# Actual image instructions starts from here.
FROM scratch
# We copy the necessary files from the previous context to the actual image
COPY --from=build-env /build/dist/app /app
# Scratch image will not have the ability to create folders. Hence addin /tmp folder This is a workaround.
COPY --from=build-env /tmp /tmp
# Specifying an entrypoint means nothing except this command will be executed when the image is run
# Since this is also a scratch image, we cannot enter the CLI when run as a container
ENTRYPOINT ["./app"]
