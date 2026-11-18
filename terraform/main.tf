terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_network" "app_network" {
  name = "app_network"
}

resource "docker_image" "postgres" {
  name = "postgres:15"
}

resource "docker_container" "postgres" {
  name  = "tf-postgres"
  image = docker_image.postgres.image_id

  env = [
    "POSTGRES_USER=myuser",
    "POSTGRES_PASSWORD=mypassword",
    "POSTGRES_DB=mydb"
  ]

  networks_advanced {
    name = docker_network.app_network.name
  }

  ports {
    internal = 5432
    external = 5433
  }
}
