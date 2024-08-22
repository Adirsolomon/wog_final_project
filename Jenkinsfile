pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = credentials("dockerhub")
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker compose up --build -d'
            }
        }

        stage('Test') {
            steps {
                sh 'docker exec -d selenium_cont python tests.py'
            }
        }
    }

    post {
        always {
            sh 'docker stop $(docker ps -q)'
        }
        success {
            script {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'

                    def services = ['wog_final-intro', 'wog_final-gamepicker', 'wog_final-savegame', 'wog_final-memorygame', 'wog_final-guessgame', 'wog_final-currency_roulette', 'wog_final-selenium_tests']

                    services.each { service ->
                        def imageName = "${DOCKER_USERNAME}/${service}"
                        sh "docker tag ${service}:latest ${imageName}:latest"
                        sh "docker push ${imageName}:latest"
                    }
                }
            }
        }
    }
}

