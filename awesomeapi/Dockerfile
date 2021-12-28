FROM python:3.9-slim as build
RUN apt-get update && apt-get install build-essential patchelf locales curl -y
RUN curl -sSL https://install.python-poetry.org | python -
WORKDIR /build
COPY . /build
ENV PATH="/root/.local/bin:$PATH"
RUN poetry export -f requirements.txt -o requirements.txt

# No difference at this stage
FROM build as build-env
RUN pip install -r requirements.txt
RUN pip install pyinstaller staticx
RUN pyinstaller -F awesomeapi/entrypoint.py --name awesomeapi --clean
RUN staticx dist/awesomeapi app --strip

FROM scratch
COPY --from=build-env /build/app /awesomeapi
COPY --from=build-env /tmp /tmp
# COPY --from=build-env /usr/lib/locale /usr/lib/locale
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
EXPOSE 8080
ENTRYPOINT ["./awesomeapi"]