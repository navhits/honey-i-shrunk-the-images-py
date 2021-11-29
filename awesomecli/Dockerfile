FROM python:3.9-slim as build
# This time we install locales package as our CLI depends on Click that needs locales to check for UTF-8 support
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
RUN pyinstaller -F awesomecli/entrypoint.py --name awesomecli --clean
RUN staticx dist/awesomecli app --strip

FROM scratch
COPY --from=build-env /build/app /awesomecli
COPY --from=build-env /tmp /tmp
# This time we copy few linux dependencies that Python dependency will need. 
# In our context it is `click` which is used by Typer in the backend
# This is a hacky approach and not recommneded. But until I or someone figures out, we'll keep it this way. 
COPY --from=build-env /usr/lib/locale /usr/lib/locale
# We also need to set few environment variables so Click can verify that locale is set for LC_ALL and LANG
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENTRYPOINT ["./awesomecli"]