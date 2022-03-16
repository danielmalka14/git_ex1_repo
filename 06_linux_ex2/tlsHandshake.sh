sudo apt install -y aiohttp-wsgi-serve
sudo apt install -y jq
curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2","message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello -o response.json | jq -r '.serverCert' response.json >cert.pem
SESSION_ID=$(jq -r '.sessionID' response.json)
wget https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem --no-check-certificate
#VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )
#if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
#  echo "Server Certificate is invalid."
#  exit 1
#fi
openssl rand -base64 23 >masterKey.txt
MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)
curl -X POST -H 'Content-Type: application/json' -d '{"sessionID": "'$SESSION_ID'","masterKey": "'$MASTER_KEY'","sampleMessage": "Hi server, please encrypt me and send to client!"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange