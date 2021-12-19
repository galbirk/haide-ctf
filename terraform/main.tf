resource "azurerm_resource_group" "default" {
  name     = "${var.rg-name}"
  location = var.region

  tags = {
    Application = "CTFAKS"
  }
}

resource "azurerm_kubernetes_cluster" "default" {
  name                = "${var.prefix}-aks"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  dns_prefix          = "${var.prefix}-k8s"

  default_node_pool {
    name            = "default"
    node_count      = 2
    vm_size         = "Standard_B4ms"
    os_disk_size_gb = 30
  }

  
  identity {
    type = "SystemAssigned"
  }
  role_based_access_control {
    enabled = true
  }

  tags = {
    Application = "CTFAKS"
  }
}


# provider "helm" {
#   kubernetes {
#     config_path = "./.kube/config"
#   }
# }

# resource "helm_release" "ctfRelease" {
#   name       = "ctf-release"
#   chart      = "../ctf-helm"
# }