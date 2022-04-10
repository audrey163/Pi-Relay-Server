# Pi-Relay-Server
allows relay  to be controlled by get requests

## turn light on
`curl http://localhost:420/high?ch=1`
## turn light off
`curl http://localhost:420/low?ch=1`

## Setup
`sudo cp server.service /etc/systemd/system/`
`sudo systemctl daemon-reload`
`sudo systemctl enable server.service`
`sudo systemctl start server.service`
`sudo systemctl status server.service`
