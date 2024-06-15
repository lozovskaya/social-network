package config

import (
	"fmt"
	"log"
	"os"

	"gopkg.in/yaml.v3"
)

const pathToConfig = "config.yml"

type Config struct {
	GRPCPort string `yaml:"grpc_port"`
	DatabaseUrl string `yaml:"database_url"`
}

func Init() (cfg Config, err error) {
	rawYaml, err := os.ReadFile(pathToConfig)
	if err != nil {
		return cfg, fmt.Errorf("read config file: %w", err)
	}

	err = yaml.Unmarshal(rawYaml, &cfg)
	if err != nil {
		return cfg, fmt.Errorf("parse config file: %w", err)
	}
	log.Print("Reading stats config succeeded")
	return cfg, nil
}
