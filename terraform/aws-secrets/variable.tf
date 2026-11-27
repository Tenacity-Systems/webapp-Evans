variable "region" {
  type    = string
  default = "us-east-2"
}

variable "eso_user_name" {
  type    = string
  default = "eso-tenacity"
}

variable "parameter_path" {
  type    = string
  default = "/tenacity/mongo"
}
