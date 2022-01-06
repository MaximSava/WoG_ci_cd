pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                    git branch: 'main', url: 'https://github.com/MaximSava/WoG_ci_cd.git'
                    sh """
                           echo "==========Checkout=============="
                       """
            }
        }
        stage('Build') {
            steps {
                sh """
                     pwd
                     ls
                     echo "================Build================"
                     sudo chmod +x ./build/create_container_image.sh
                     sudo ./build/create_container_image.sh wog build_$BUILD_TAG
                """

                }
        }

        stage('Run') {
            steps {
                sh """
                    echo "==============Run docker-compose================="
                    sudo docker-compose up --detach
                    sleep 2
                    sudo docker network connect wog_ci_cd_default selenium-chrome
                    sleep 2
                   """
            }
        }

        stage('Test') {
            steps {
                sh """
                    echo "==============TEST================="
                    sudo docker exec worldofgames python e2e.py
                   """
            }
        }

        stage('Finalize') {
            steps {
                sh """
                    sudo chmod +x ./deploy/deploy_docker_image.sh
                    sudo ./deploy/deploy_docker_image.sh $BUILD_TAG

                   """
            }
        }
    }
 }