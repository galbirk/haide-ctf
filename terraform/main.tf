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
    vm_size         = "Standard_DS2_v2"
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

# resource "azurerm_managed_disk" "pvDisk" {
#   name                 = "aks-pv-disk"
#   location             = var.region
#   resource_group_name  = azurerm_resource_group.default.name
#   storage_account_type = "Standard_LRS"
#   create_option        = "Empty"
#   disk_size_gb         = "50"

#   tags = {
#     Application = "CTFAKS"
#   }
# }


# resource "kubernetes_persistent_volume_v1" "ctfPV" {
#   metadata {
#     name = "ctf-pv"
#   }
#   spec {
#     capacity = {
#       storage = "45Gi"
#     }
#     access_modes = ["ReadWriteOnce"]
#     persistent_volume_source {
#        azure_disk {
#         caching_mode  = "None"
#         data_disk_uri = azurerm_managed_disk.pvDisk.id
#         disk_name     = azurerm_managed_disk.pvDisk.name
#         kind          = "Managed"
#       }
#     }
#   }
# }