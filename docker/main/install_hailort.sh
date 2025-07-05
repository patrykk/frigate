#!/bin/bash

set -euxo pipefail

hailo_version="4.21.0"

if [[ "${TARGETARCH}" == "amd64" ]]; then
    arch="x86_64"
elif [[ "${TARGETARCH}" == "arm64" ]]; then
    arch="aarch64"
fi

wget -qO- "https://github.com/patrykk/hailort/releases/download/${hailo_version}/hailort-debiantesting-${TARGETARCH}.tar.gz" | tar -C / -xzf -
wget -P /wheels/ "https://github.com/patrykk/hailort/releases/download/${hailo_version}/hailort-${hailo_version}-cp313-cp313-linux_${arch}.whl"
