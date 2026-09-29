# Script to upload the code over SSH
# Make sure sshpass is installed before running this
if [ $# -eq 0 ]; then
  echo "Pass in the robot ip as an argument"
  exit 1
fi

sshpass -p "maker" scp -r ./* robot@$1:~/cmput312-lab-2

