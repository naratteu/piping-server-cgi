#!/bin/bash

mkdir ppng
fifo=ppng/$QUERY_STRING

mkfifo $fifo

case $REQUEST_METHOD in
GET)
	cat < $fifo
;;
POST)
	echo Content-Type: text/event-stream && echo
	(echo Content-Type: ${CONTENT_TYPE-text/event-stream} && echo && cat) > $fifo
	echo done!
;;
esac

rm $fifo