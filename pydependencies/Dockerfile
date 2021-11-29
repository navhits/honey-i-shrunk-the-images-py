# This time we have 3 stages for our build.
# The base image will install necessary libraries
FROM python:3.9-slim as build
RUN apt-get update && apt-get install build-essential patchelf curl -y
# In this step we install `poetry` - a depenedency managment tool for python
RUN curl -sSL https://install.python-poetry.org | python -
# Setting the workdir although we don't need it here. But this will help add a file to the workdir that will needed in the next step.
WORKDIR /build
COPY . /build
ENV PATH="/root/.local/bin:$PATH"
# Since pip cannot read and install just the dependencies from pyproject.toml, we use poetry to export the requirements alone.
# --without-hashes is used primarily when there are dependencies from a VCS. Although here it doesn't apply, keeping it here.
# But hash verification is recommended.
RUN poetry export -f requirements.txt -o requirements.txt --without-hashes

# In this tage we pack and build the binnary
FROM build as build-env
RUN pip install staticx pyinstaller
RUN pip install -r requirements.txt
RUN pyinstaller -F pydependencies/pydependencies.py -n binary --clean
RUN staticx dist/binary dist/app --strip

# And our magical stage that will run the binary
FROM scratch
COPY --from=build-env /build/dist/app /app
COPY --from=build-env /tmp /tmp
ENTRYPOINT ["./app"]
