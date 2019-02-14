sh bestoonincome.sh

# please set these variables
TOKEN=your_token
BASE_URL=http://poulbedebestoon.ir


curl --data "token=$TOKEN&amount=$1&text=$2" $BASE_URL/submit/income/
