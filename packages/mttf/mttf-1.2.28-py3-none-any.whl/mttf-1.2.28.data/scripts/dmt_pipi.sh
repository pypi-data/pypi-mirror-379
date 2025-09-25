#/!bin/bash
if [ $(id -u) -ne 0 ]; then
  echo "WARNING: As of 2025-04-20, it is not safe to install wml packages locally."
  wml_nexus.py pip3 install --trusted-host localhost --extra-index https://localhost:5443/repository/minhtri-pypi-dev/simple/ --upgrade $@
else
  wml_nexus.py uv pip install -p /usr/bin/python3 --system --break-system-packages --prerelease allow --allow-insecure-host localhost --index https://localhost:5443/repository/minhtri-pypi-dev/simple/ --index-strategy unsafe-best-match $@
fi
