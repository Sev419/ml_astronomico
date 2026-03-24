pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Obteniendo el proyecto'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ml_astronomico .'
            }
        }

        stage('Run Tests and Main Script in Docker') {
            steps {
                sh 'mkdir -p outputs'
                sh 'docker rm -f ml_astronomico_run || true'
                sh 'docker run --name ml_astronomico_run ml_astronomico'
            }
        }

        stage('Copy Outputs From Container') {
            steps {
                sh 'docker cp ml_astronomico_run:/app/outputs/. outputs/'
                sh 'docker rm -f ml_astronomico_run'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'outputs/*', fingerprint: true
            }
        }
    }
}