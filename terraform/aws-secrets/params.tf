variable "mongo_password" {
  type      = string
  sensitive = true
  ephemeral = true
}

import {
  to = aws_ssm_parameter.mongo_username
  id = "${var.parameter_path}/username"
}

resource "aws_ssm_parameter" "mongo_username" {
  name  = "${var.parameter_path}/username"
  type  = "SecureString"
  value = "admin"
}

resource "aws_ssm_parameter" "mongo_password" {
  name             = "${var.parameter_path}/password"
  type             = "SecureString"
  value_wo         = var.mongo_password
  value_wo_version = 1
}

resource "aws_ssm_parameter" "mongo_uri" {
  name             = "${var.parameter_path}/uri"
  type             = "SecureString"
  value_wo         = "mongodb://admin:${var.mongo_password}@mongo:27017/pki_cloud?authSource=admin"
  value_wo_version = 1
}
