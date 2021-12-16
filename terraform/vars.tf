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

variable "region" {
    description = "Azure Region"
  type = string
  default = "West Europe"
}