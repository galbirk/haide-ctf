variable "rg-name" {
  description = "Azure Resource Group to Create the Cluster in"
  type        = string
  default     = "terraform-managed-for-aks-rg"
}

variable "prefix" {
  description = "AKS Cluster Prefix"
  type        = string
  default     = "ctf"
}

variable "region" {
  description = "Azure Region"
  type        = string
  default     = "West Europe"
}

variable "teams" {
  description = "Number of teams"
  type        = number
  default     = 3
}

variable "win_vm_image" {
  description = "Windows Image Information"
  type = object(
    {
      publisher = string
      offer     = string
      sku       = string
      version   = string
    }
  )
  default = {
    publisher = "MicrosoftWindowsServer"
    offer     = "WindowsServer"
    sku       = "2019-Datacenter"
    version   = "latest"
  }
}