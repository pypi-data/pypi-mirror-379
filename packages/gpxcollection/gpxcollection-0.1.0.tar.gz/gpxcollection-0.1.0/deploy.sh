#!/bin/sh -x

rm -rf output
uv run gpxcollection \
    --mapbox_outdoor_token 'pk.eyJ1IjoicGV0ZXJob2ZmbWFubiIsImEiOiJjanpmZzY5bXIwYnJuM2Nxa2psZHJ6cGF6In0.ci0rbidkerqwNyPtjcp9pQ' \
    --mapbox_satellite_token 'pk.eyJ1IjoicGV0ZXJob2ZmbWFubiIsImEiOiJjbDlib2MwdHgxa2FrM29sbWk0YWh3NW51In0.wQFm2QX__7NgeAzyhpMPDQ' \
    input/ output/

(sleep 1 && open "http://localhost:8000/output") &

uv run python -m http.server
