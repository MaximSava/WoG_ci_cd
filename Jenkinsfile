
pipeline {
    agent any
    environment {

    }

    stages {
        stage('Checkout') {
            steps {
                    git branch: 'WorldofGames', url: 'https://github.com/MaximSava/DevOps-Course.git'
                    sh """

                       """
            }
        }
        stage('Build') {
            steps {
                sh """
                     sudo ./create_container_image
                """

                }
        }

        stage('Run') {
            steps {
                sh """
                    echo "Run docker-compose"
                    sudo docker-compose up
                    sudo docker network connect worldofgames_default selenium-chrome
                   """
            }
        }

        stage('Test') {
            steps {
                sh """
                    sudo docker exec -it worldofgames python e2e.py
                   """
            }
        }
    }
 }