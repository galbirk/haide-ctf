# variable "appId" {
#   description = "Azure Kubernetes Service Cluster service principal"
# }

# variable "password" {
#   description = "Azure Kubernetes Service Cluster password"
# }

variable "rg-name" {
    description = "Azure Resource Group to Create the Cluster in"
    type = string
    default = "terraform-managed-for-aks-rg"
}

variable "prefix" {
    description = "AKS Cluster Prefix"
    type = string
    default = "ctf"
}