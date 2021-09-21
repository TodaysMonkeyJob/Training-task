#!/bin/bash

# adjust these
INPUT_PLUGIN="/usr/local/lib/mjpg-streamer/input_uvc.so";
FRAMES="30";
RESOLUTION="1280x720";

OUTPUT_PLUGIN="/usr/local/lib/mjpg-streamer/output_http.so";
PORT="8085";

# the following are defaults and should not need to be changed
EXEC="/usr/local/bin/mjpg_streamer"
WEB_DIR="/usr/local/share/mjpg-streamer/www";

# mjgp_streamer often does not start on first try
start_streamer(){
${EXEC} -i "${INPUT_PLUGIN} -n -f ${FRAMES} -r ${RESOLUTION}" -o "${OUTPUT_PLUGIN} -p ${PORT} -w ${WEB_DIR}"  > /dev/null 2>&1
if pgrep mjpg_streamer > /dev/null
then
  echo "mjpg_streamer started"
else
  echo "couldn't start mjpg_streamer"
fi
}

if pgrep mjpg_streamer > /dev/null
then
    echo "mjpg_streamer already running"
else
    start_streamer
fi
