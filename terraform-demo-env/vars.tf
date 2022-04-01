variable "region" {
    description = "Azure Region"
    type = string
    default = "West Europe"
}

variable "rg-name" {
    description = "Azure Resource Group to Create the Cluster in"
    type = string
    default = "terraform-managed-for-ctfd-demo"
}

variable "dns_label" {
    description = "DNS Name Label"
    type = string
    default = "ctfd-demo"
}

variable "container_name" {
    description = "Container's Name"
    type = string
    default = "ctfd"
}

variable "image" {
    description = "Image for the container"
    type = string
    default = "registry.hub.docker.com/ctfd/ctfd"
}

variable "port" {
    description = "Port to Expose"
    type = number
    default = 8000
}