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
                    def services = ['wog_final-intro', 'wog_final-game_picker', 'wog_final-savegame', 'wog_final-memory_game', 'wog_final-guess_game', 'wog_final-currency_roulette', 'wog_final-selenium_tests', 'wog_final-mysql']
                    
                    // Iterate over each service, tag and push the corresponding Docker image
                    services.each { service ->
                        def imageName = "adiros/${service}"
    
                        sh "docker push ${imageName}:latest"
                    }
                }
            }
        }
    }
}
