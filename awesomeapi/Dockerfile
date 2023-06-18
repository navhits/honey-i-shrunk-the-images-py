FROM python:3.9-slim as build
RUN apt-get update && apt-get install build-essential patchelf locales scons curl -y
WORKDIR /build
COPY . /build

# No difference at this stage
FROM build as build-env
RUN pip install .
RUN pip install pyinstaller
RUN pip install staticx
RUN pyinstaller -F awesomeapi/entrypoint.py --name awesomeapi --clean --strip
RUN staticx dist/awesomeapi app --strip
RUN mkdir tmp

FROM scratch
COPY --from=build-env /build/app /awesomeapi
# pyinstaller needs a /tmp to exist
COPY --from=build-env /build/tmp /tmp
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
EXPOSE 8080
ENTRYPOINT ["./awesomeapi"]

LABEL maintainer="dev@navs.page"
LABEL org.opencontainers.image.source=https://github.com/navhits/honey-i-shrunk-the-images-py
LABEL org.opencontainers.image.description="An experiment to shrink the size of the Python containers"
