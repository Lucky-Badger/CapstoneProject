# CapstoneProject
Project for CapitalGroupCapstone

# ssh
ssh -i "keyPair.pem" ec2-user@ec2-54-213-174-160.us-west-2.compute.amazonaws.com

# connecting psql
psql -h capstoneteam-4.ckokfd9swhyk.us-west-2.rds.amazonaws.com -U postgres

# docker
docker build -t team4image.v1 .
docker run --name team4image.v1 #password? -p 5432:5432 -d postgres

### pushing to dockerhub
            docker login (create dockerhub login and use credentials)
            docker tag team4image.v1:latest nw888/dockerhub:myfirstimagepush
            docker push nw888/dockerhub:myfirstimagepush