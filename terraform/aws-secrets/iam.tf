data "aws_caller_identity" "current" {}

locals {
  account_id = data.aws_caller_identity.current.account_id
  policy_arn = "arn:aws:iam::${local.account_id}:policy/eso-tenacity-read"
}

import {
  to = aws_iam_user.eso
  id = var.eso_user_name
}

import {
  to = aws_iam_policy.eso_read
  id = local.policy_arn
}

import {
  to = aws_iam_user_policy_attachment.eso
  id = "${var.eso_user_name}/${local.policy_arn}"
}

resource "aws_iam_user" "eso" {
  name = var.eso_user_name
}

resource "aws_iam_policy" "eso_read" {
  name = "eso-tenacity-read"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["ssm:GetParameter", "ssm:GetParameters"]
      Resource = "arn:aws:ssm:${var.region}:${local.account_id}:parameter${var.parameter_path}/*"
    }]
  })
}

resource "aws_iam_user_policy_attachment" "eso" {
  user       = aws_iam_user.eso.name
  policy_arn = aws_iam_policy.eso_read.arn
}
