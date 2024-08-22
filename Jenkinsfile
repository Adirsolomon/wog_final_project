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
                withCredentials(bindings: [usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'

                    // List of services to push to Docker Hub
                    def services = ['intro', 'game_picker', 'savegame', 'memory_game', 'guess_game', 'currency_roulette', 'selenium_tests', 'mysql']
                    
                    // Iterate over each service, tag and push the corresponding Docker image
                    services.each { service ->
                        def imageName = "adiros/${service}"
                        sh "docker tag ${service} ${imageName}:latest"
                        sh "docker push ${imageName}:latest"
                    }
                }
            }
        }
    }
}
