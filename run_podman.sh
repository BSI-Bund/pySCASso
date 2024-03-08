#!/bin/bash
# if the image does not exist we have to rebuild
if [[ "$(podman images -q pyscasso:latest 2> /dev/null)" == "" ]]; then
    echo "Building pyscasso docker image. This will take a while..."
    podman build . -t pyscasso
fi

podman run --rm --cap-add=NET_RAW --cap-add=NET_ADMIN --mount type=bind,src=$(pwd),target=/pyscasso -it pyscasso:latest "$@"
