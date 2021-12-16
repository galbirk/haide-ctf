# We strongly recommend using the required_providers block to set the
# Azure Provider source and version being used
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=2.46.0"
    }
  }
}

data "azurerm_kubernetes_cluster" "cluster" {
  name                = azurerm_kubernetes_cluster.default.name
  resource_group_name = var.rg-name
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}
  subscription_id = "adf09ed2-68bb-45df-b407-c5df02db378b"
} 

# Configure the Kubernetes Provider
provider "kubernetes" {
  host                   = "${data.azurerm_kubernetes_cluster.cluster.kube_config.0.host}"
  client_certificate     = "${base64decode(data.azurerm_kubernetes_cluster.cluster.kube_config.0.client_certificate)}"
  client_key             = "${base64decode(data.azurerm_kubernetes_cluster.cluster.kube_config.0.client_key)}"
  cluster_ca_certificate = "${base64decode(data.azurerm_kubernetes_cluster.cluster.kube_config.0.cluster_ca_certificate)}"
}
