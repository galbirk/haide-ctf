resource "azurerm_resource_group" "default" {
  name     = var.rg-name
  location = var.region

  tags = {
    Application = "CTFAKS"
  }
}

resource "azurerm_virtual_network" "main" {
  name                = "${azurerm_resource_group.default.name}-network"
  address_space       = ["10.3.0.0/16"]
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
}

resource "azurerm_subnet" "internal" {
  name                 = "${azurerm_resource_group.default.name}-sn"
  resource_group_name  = azurerm_resource_group.default.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.3.1.0/24"]
}

## AKS Cluster
resource "azurerm_kubernetes_cluster" "default" {
  name                = "${var.prefix}-aks"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  dns_prefix          = "${var.prefix}-k8s"

  default_node_pool {
    name       = "default"
    node_count = 4
    # 4/5
    vm_size = "Standard_F16s_v2"
    # Standard_B4ms
    os_disk_size_gb = 80
  }


  identity {
    type = "SystemAssigned"
  }
  # role_based_access_control {
  #   enabled = true
  # }

  tags = {
    Application = "CTFAKS"
  }
}

####### Windows VMS #########
resource "random_password" "admin_password" {
  length      = 10
  special     = false
  min_numeric = 1
  min_lower   = 1
  min_upper   = 1
}

resource "azurerm_public_ip" "winPublic" {
  count               = var.teams
  name                = "team-${count.index}-ip"
  resource_group_name = azurerm_resource_group.default.name
  location            = azurerm_resource_group.default.location
  allocation_method   = "Static"
  tags = {
    Application = "CTF"
  }
}

resource "azurerm_network_interface" "winMain" {
  count               = var.teams
  name                = "team-${count.index}-nic"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name

  ip_configuration {
    name                          = "team-${count.index}-ipcfg"
    subnet_id                     = azurerm_subnet.internal.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = element(azurerm_public_ip.winPublic.*.id, count.index)
  }
}

resource "azurerm_virtual_machine" "winVm" {
  count                            = var.teams
  name                             = "team${count.index}-vm"
  location                         = azurerm_resource_group.default.location
  resource_group_name              = azurerm_resource_group.default.name
  network_interface_ids            = [element(azurerm_network_interface.winMain.*.id, count.index)]
  vm_size                          = "Standard_B4ms"
  delete_os_disk_on_termination    = true
  delete_data_disks_on_termination = true
  storage_image_reference {
    publisher = var.win_vm_image.publisher
    offer     = var.win_vm_image.offer
    sku       = var.win_vm_image.sku
    version   = var.win_vm_image.version
  }
  storage_os_disk {
    name              = "team${count.index}-vm"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }
  os_profile {
    computer_name  = "team${count.index}-vm"
    admin_username = "ctf"
    admin_password = random_password.admin_password.result
  }
  os_profile_windows_config {
    # need this for vm extensions
    provision_vm_agent = true
  }

  tags = {
    Application = "CTF"
  }
  depends_on = [
    azurerm_public_ip.winPublic
  ]
}


# vars to use for scripts
locals {
  define_wireshark_url = "$wireshark_url = 'https://1.as.dl.wireshark.org/win64/Wireshark-win64-3.6.5.exe'"
  download_wireshark   = "Invoke-WebRequest -Uri $wireshark_url -OutFile C:/Packages/Wireshark-win64-3.6.5.exe"
  install_choco        = "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
  install_usbpcap      = "choco install usbpcap -y"
  install_wireshark    = "C:/Packages/Wireshark-win64-3.6.5.exe /S /desktopicon=yes /quicklaunchicon=yes /EXTRACOMPONENTS=sshdump,udpdump,ciscodump,randpktdump"
  install_chrome = "$Installer = $env:TEMP + '/chrome_installer.exe'; Invoke-WebRequest 'http://dl.google.com/chrome/install/375.126/chrome_installer.exe' -OutFile $Installer; Start-Process -FilePath $Installer -Args '/silent /install' -Verb RunAs -Wait; Remove-Item $Installer"
  powershell_command   = "${local.define_wireshark_url}; ${local.download_wireshark}; ${local.install_choco}; ${local.install_usbpcap}; ${local.install_wireshark}; ${local.install_chrome}"
}

# WireShark Installation
resource "azurerm_virtual_machine_extension" "InstallWireshark" {
  count                      = var.teams
  name                       = "install-wireshark-${count.index}"
  virtual_machine_id         = element(azurerm_virtual_machine.winVm.*.id, count.index)
  publisher                  = "Microsoft.Compute"
  type                       = "CustomScriptExtension"
  type_handler_version       = "1.10"
  auto_upgrade_minor_version = true

  settings = <<SETTINGS
    {
        "commandToExecute": "powershell.exe -Command \"${local.powershell_command}\""
    }
SETTINGS
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