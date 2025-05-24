#!/bin/bash

mkfifo $QUERY_STRING

case $REQUEST_METHOD in
GET)
	cat < $QUERY_STRING
;;
POST)
	echo Content-Type: text/event-stream && echo
	(echo Content-Type: ${CONTENT_TYPE-text/event-stream} && echo && cat) > $QUERY_STRING
;;
esac