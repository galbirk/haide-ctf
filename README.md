# haide-ctf
CTFD based capture the flag application, deployed on AKS.

## Table of Contents
- [Requirements](#Requirements)
  * [Install terraform](#Install-terraform)
  * [Install kubectl](#install-kubectl)
- [Deploy CTFD Platform](#Deploy-CTFD-Platform)
  * [Clone git repository](#Clone-git-repository)
  * [Config terraform](#Config-terraform)
  * [Deploy AKS Cluster with terraform](#deploy-aks-cluster-with-terraform)
  * [Get kubeconfig](#get-kubeconfig)
  * [Deploy CTFD and Challenges Helm Chart](#deploy-ctfd-and-challenges-helm-chart)
    * [Create secrets](#create-secrets)
    * [Important vaules in ./ctf-helm/values.yaml](#important-vaules-in-ctf-helmvaluesyamlctf-helmvaluesyaml)
    * [Install helm chart](#install-helm-chart)
- [Docker Hub Images](#Docker-Hub-Images)
- [Contributers](#contributers)

# Requirements
## Install terraform
[terraform installation documentation](https://learn.hashicorp.com/tutorials/terraform/install-cli)<br>
## Install kubectl
[kubectl installation documentation](https://kubernetes.io/docs/tasks/tools/)<br>
# Deploy CTFD Platform

## Clone git repository
```bash
git clone https://github.com/galbirk/haide-ctf.git
cd haide-ctf/terraform
```
## Config terraform
- create terraform.tfvars in [./terraform](./terrafrom) to customize your environment
- enter your azure subscription id in [terraform/providers.tf](./terraform/providers.tf) file.
## Deploy AKS Cluster with terraform
```bash
# in haide-ctf/terraform
terraform init
terraform plan 
terraform apply
```
## Get kubeconfig
```bash
# you can get it from terrafrom or from az cli

# terraform
terrafrom output kube_config

# az cli
az account set --subscription <subscription_id>
az aks get-credentials --resource-group <cluster_resource_group>--name <cluster_name>
```
## Deploy CTFD and Challenges Helm Chart
### Create secrets
*secrets names mentioned in [./ctf-helm/values.yaml](./ctf-helm/values.yaml)
```bash
# create db secret
kubectl create secret generic <db_secret_name_in_values.yaml> --from-literal=MYSQL_DATABASE=<db_name> --from-literal=MYSQL_PASSWORD=<db_password> --from-literal=MYSQL_ROOT_PASSWORD=<root_password> --from-literal=MYSQL_USER=<db_username> --dry-run=client -o json > ./ctf-helm/db-secret.yaml

# create app secret
kubectl create secret generic <app_secret_name_in_values.yaml> --from-literal=dbURL=mysql+pymysql://<db_username>:<db_password>@<db_service_name>/ctfd --dry-run=client -o json > ./ctf-helm/app-secret.yaml
```
### Important vaules in [./ctf-helm/values.yaml](./ctf-helm/values.yaml)
* numberOfTeams - number of teams participating in the ctf (we recommend to number the teams from 0 onwards).
* ctfd.secretName - the name of the app secret.
* mariadb.secretName - the name of the db secret.
### Install helm chart
```bash
cd ./ctf-helm
# change your settings in values.yaml
cd ..
helm install <release-name> ./ctf-helm

# get ctfd ip address
kubectl get svc ctf-svc -o jsonpath="{.status.loadBalancer.ingress[0].ip}"

# get to ctfd url
echo -n http://$(kubectl get svc ctf-svc -o jsonpath="{.status.loadBalancer.ingress[0].ip}")

# get hodor challenge ip
kubectl get svc hodor-svc -o jsonpath="{.status.loadBalancer.ingress[0].ip}"

# get jailbreak challenge ip
kubectl get svc jail-svc -o jsonpath="{.status.loadBalancer.ingress[0].ip}"

# get path not taken challenge ip
kubectl get svc path-not-taken-svc -o jsonpath="{.status.loadBalancer.ingress[0].ip}"

# get 2048 challenge ip
kubectl get svc twentyfortyeight-svc -o jsonpath="{.status.loadBalancer.ingress[0].ip}"
```

# Docker Hub Images
#### The images are published in Docker Hub:
* [jailbreak image repository](https://hub.docker.com/repository/docker/galbirk/jail)
* [hodor image repository](https://hub.docker.com/repository/docker/galbirk/hodor)
* [2048 image repository](https://hub.docker.com/repository/docker/galbirk/twentyfortyeight)
* [path not taken image repository](https://hub.docker.com/repository/docker/galbirk/path)

# Contributers

<b>Gal Birkman, DevOps Engineer.</b><br>
<b>email:</b> galbirkman@gmail.com<br>
<b>GitHub:</b> https://github.com/galbirk