resource "azurerm_resource_group" "birk-rg" {
  name     = var.rg-name
  location = var.region
  tags = {
    Application = "ctfd-demo"
  }
}

resource "azurerm_container_group" "birk-cg" {
  name                = var.container_name
  location            = azurerm_resource_group.birk-rg.location
  resource_group_name = azurerm_resource_group.birk-rg.name
  ip_address_type     = "Public"
  dns_name_label      = var.dns_label
  os_type             = "Linux"

  container {
    name   = var.container_name
    image  = var.image
    cpu    = "4"
    memory = "4"

    ports {
      port     = var.port
      protocol = "TCP"
    }
  }
  tags = {
    environment = "dev"
  }
}