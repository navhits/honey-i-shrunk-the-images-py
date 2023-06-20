# This time we have 3 stages for our build.
# The base image will install necessary libraries
FROM python:3.9-slim as build
RUN apt-get update && apt-get install build-essential patchelf locales scons curl -y
# Setting the workdir although we don't need it here. But this will help add a file to the workdir that will needed in the next step.
WORKDIR /build
COPY . /build

# In this tage we pack and build the binnary
FROM build as build-env
RUN pip install .
RUN pip install pyinstaller
RUN pip install staticx
RUN pyinstaller -F pycurl/pycurl.py -n binary --clean --strip
RUN staticx dist/binary dist/app --strip
RUN mkdir tmp

# And our magical stage that will run the binary
FROM scratch
COPY --from=build-env /build/dist/app /app
COPY --from=build-env /build/tmp /tmp
ENTRYPOINT ["./app"]

LABEL maintainer="dev@navs.page"
LABEL org.opencontainers.image.source=https://github.com/navhits/honey-i-shrunk-the-images-py
LABEL org.opencontainers.image.description="An experiment to shrink the size of the Python containers"
