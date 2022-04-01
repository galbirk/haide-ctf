output "container_ip" {
    value = azurerm_container_group.birk-cg.ip_address
}

output "fqdn" {
    value = azurerm_container_group.birk-cg.fqdn
}